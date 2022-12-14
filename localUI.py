import os
import subprocess
import sys
import textwrap

from Class.exceptions import CantAssignItemException, RandomizerExceptions
from List.configDict import locationType

from Module.resources import resource_path
from Module.tourneySpoiler import TourneySeedSaver

# Keep the setting of the environment variable as close to the top as possible.
# This needs to happen before anything Boss/Enemy Rando gets loaded for the sake of the distributed binary.
os.environ["USE_KH2_GITPATH"] = "extracted_data"


import datetime
import json
import random
import re
import string
from pathlib import Path

import pyperclip as pc

import pytz
# from PIL import Image
from PySide6 import QtGui
from PySide6.QtCore import Qt, QThread, Signal, QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QLineEdit, QMenu, QPushButton, QCheckBox, QTabWidget, QVBoxLayout, QHBoxLayout, QWidget, QInputDialog,
    QFileDialog, QMessageBox, QProgressDialog, QProgressBar, QSizePolicy, QDialog, QGridLayout, QListWidget,QSpinBox,QComboBox, QListView
)

from qt_material import apply_stylesheet
from Class import settingkey
from Class.seedSettings import SeedSettings, randomize_settings
from Module.cosmetics import CosmeticsMod, CustomCosmetics
from Module.dailySeed import allDailyModifiers, getDailyModifiers
from Module.generate import generateMultiWorldSeed, generateSeed
from Module.RandomizerSettings import RandomizerSettings
from Module.newRandomize import Randomizer
from Module.seedshare import SharedSeed, ShareStringException
from UI.FirstTimeSetup.firsttimesetup import FirstTimeSetup
from UI.FirstTimeSetup.luabackendsetup import LuaBackendSetupDialog
from UI.Submenus.BossEnemyMenu import BossEnemyMenu
from UI.Submenus.CosmeticsMenu import CosmeticsMenu
from UI.Submenus.HintsMenu import HintsMenu
from UI.Submenus.ItemPlacementMenu import ItemPlacementMenu
from UI.Submenus.ItemPoolMenu import ItemPoolMenu
from UI.Submenus.KeybladeMenu import KeybladeMenu
from UI.Submenus.RewardLocationsMenu import RewardLocationsMenu
from UI.Submenus.SeedModMenu import SeedModMenu
from UI.Submenus.SoraMenu import SoraMenu
from UI.Submenus.StartingMenu import StartingMenu

LOCAL_UI_VERSION = '2.2.0-beta'

class Logger(object):
    def __init__(self, orig_stream):
        self.filename = "log.txt"
        self.orig_stream = orig_stream
    def write(self, data):
        with open(self.filename, "a") as f:
            f.write(str(data))
        self.orig_stream.write(str(data))
    def flush(self):
        self.orig_stream.flush()

logger = Logger(sys.stdout)

sys.stdout = logger
sys.stderr = logger


AUTOSAVE_FOLDER = "auto-save"
PRESET_FOLDER = "presets"



class GenSeedThread(QThread):
    finished = Signal(object)
    failed = Signal(Exception)

    def provideData(self,data,rando_settings):
        self.data=data
        self.rando_settings = rando_settings
        self.zip_file = None

    def run(self):
        try:
            zip_file, spoiler_log, enemy_log = generateSeed(self.rando_settings, self.data)

            custom_executables = self.data.get('customCosmeticsExecutables', [])
            for custom_executable in custom_executables:
                custom_file_path = Path(custom_executable)
                if custom_file_path.is_file():
                    custom_cwd = custom_file_path.parent
                    subprocess.call(custom_file_path,cwd=custom_cwd)

            self.finished.emit((zip_file,spoiler_log,enemy_log))
        except Exception as e:
            self.failed.emit(e)


class MultiGenSeedThread(QThread):
    finished = Signal(object)
    failed = Signal(Exception)

    def provideData(self,data,rando_settings):
        self.data=data
        self.rando_settings = rando_settings
        self.zip_file = None

    def run(self):
        try:
            all_output = generateMultiWorldSeed(self.rando_settings, self.data)
            self.finished.emit(all_output)
        except Exception as e:
            self.failed.emit(e)


class TourneySeedDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tourney Mode")
        self.setMinimumWidth(800)

        grid = QGridLayout()
        row = 0

        explanation = textwrap.dedent('''
Use this screen to generate a set of seeds for a tournament.

The tournament organizer receives a folder containing all of the seed strings, seed hashes, and spoiler logs.
This can be shared with other tournament organizers to make sure everyone has access to all the seeds. 

When participants receive their seeds, they will NOT have access to spoiler logs.
Participants will only be able to customize cosmetics.
        '''.strip())
        grid.addWidget(QLabel(explanation), row, 0, 1, 3)

        row = row + 1
        grid.addWidget(QLabel(''), row, 0)

        row = row + 1
        grid.addWidget(QLabel('Tournament Name'), row, 0)
        name_field = QLineEdit()
        name_field.setToolTip('The name of the tournament.')
        self.name_field = name_field
        grid.addWidget(name_field, row, 1, 1, 2)

        row = row + 1
        tourney_label = QLabel("How many seeds?")
        grid.addWidget(tourney_label, row, 0)

        self.num_seeds = QSpinBox()
        self.num_seeds.setRange(1, 32)
        self.num_seeds.setSingleStep(1)
        self.num_seeds.setValue(1)
        grid.addWidget(self.num_seeds, row, 1, 1, 2)

        row = row + 1
        platform_label = QLabel("Make seeds for")
        grid.addWidget(platform_label, row, 0)
        self.platform = QComboBox()
        self.platform.addItem("PC")
        self.platform.addItem("PCSX2")
        grid.addWidget(self.platform, row, 1, 1, 2)

        row = row + 1
        output_path_field = QLineEdit()
        output_path_field.setToolTip('The location to which to save the generated seeds.')
        self.output_path_field = output_path_field
        output_path_button = QPushButton('Browse')
        output_path_button.clicked.connect(self._choose_output_path)

        grid.addWidget(QLabel('Output location'), row, 0)
        grid.addWidget(output_path_field, row, 1)
        grid.addWidget(output_path_button, row, 2)

        row = row + 1
        cancel_button = QPushButton("Cancel")
        choose_button = QPushButton("Generate Seeds")
        cancel_button.clicked.connect(self.reject)
        choose_button.clicked.connect(self.accept)
        button_layout = QHBoxLayout()
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(choose_button)
        grid.addLayout(button_layout, row, 0, 1, 3)

        box = QVBoxLayout()
        box.addLayout(grid)

        self.setLayout(box)

    def save(self):
        return self.name_field.text(), self.num_seeds.value(), self.platform.currentText(), self.output_path_field.text()

    def _choose_output_path(self):
        output = QFileDialog.getExistingDirectory()
        if output is not None and output != '':
            self.output_path_field.setText(output)


class RandomPresetDialog(QDialog):
    def __init__(self,preset_list):
        super().__init__()
        self.preset_list = preset_list
        self.setWindowTitle("Randomly Pick a Preset")
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)

        box = QGridLayout()

        self.preset_list_widget = QListWidget()
        self.preset_list_widget.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        for c in self.preset_list:
            self.preset_list_widget.addItem(c)
        box.addWidget(self.preset_list_widget,0,0)
        
        select_all_button = QPushButton("Select All Presets")
        select_all_button.clicked.connect(self.select_all_presets_from_list)

        cancel_button = QPushButton("Cancel")
        choose_button = QPushButton("Randomly Pick From Selected Presets")
        cancel_button.clicked.connect(self.reject)
        choose_button.clicked.connect(self.accept)

        box.addWidget(select_all_button,1,0)
        box.addWidget(cancel_button,1,1)
        box.addWidget(choose_button,0,1)

        self.setLayout(box)

    def select_all_presets_from_list(self):
        for index in range(self.preset_list_widget.count()):
            self.preset_list_widget.item(index).setSelected(True)

    def save(self):
        return [p.text() for p in self.preset_list_widget.selectedItems()]


class RandomSettingsDialog(QDialog):
    def __init__(self,settings: SeedSettings):
        super().__init__()
        self.passed_settings = settings
        self.random_choices = self.passed_settings._randomizable
        self.setWindowTitle("Randomized Settings")
        self.setMinimumWidth(800)
        self.setMinimumHeight(800)

        box = QGridLayout()

        self.settings_list_widget = QListWidget()
        self.settings_list_widget.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        self.settings_list_widget.setFlow(QListView.LeftToRight)
        self.settings_list_widget.setResizeMode(QListView.Adjust)
        self.settings_list_widget.setGridSize(QSize(128,128))
        self.settings_list_widget.setSpacing(60)
        self.settings_list_widget.setViewMode(QListView.IconMode)
        for c in self.random_choices:
            self.settings_list_widget.addItem(c.ui_label)
        box.addWidget(self.settings_list_widget,0,0)
        
        select_all_button = QPushButton("Select All Settings")
        select_all_button.clicked.connect(self.select_all_randomizable)
        select_none_button = QPushButton("Select No Settings")
        select_none_button.clicked.connect(self.select_none_randomizable)

        cancel_button = QPushButton("Cancel")
        choose_button = QPushButton("Randomize Selected Settings")
        cancel_button.clicked.connect(self.reject)
        choose_button.clicked.connect(self.accept)

        box.addWidget(select_all_button,1,0)
        box.addWidget(select_none_button,1,1)
        box.addWidget(cancel_button,1,2)
        box.addWidget(choose_button,0,1)

        self.setLayout(box)

    def select_all_randomizable(self):
        for index in range(self.settings_list_widget.count()):
            self.settings_list_widget.item(index).setSelected(True)
    def select_none_randomizable(self):
        for index in range(self.settings_list_widget.count()):
            self.settings_list_widget.item(index).setSelected(False)

    def save(self):
        return [self.random_choices[p.row()].name for p in self.settings_list_widget.selectedIndexes()]

class KH2RandomizerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UTC = pytz.utc
        self.startTime = datetime.datetime.now(self.UTC)
        self.dailySeedName = self.startTime.strftime('%d-%m-%Y')
        self.mods = getDailyModifiers(self.startTime,hard_mode=False,boss_enemy=False)
        self.mods_hard = getDailyModifiers(self.startTime,hard_mode=True,boss_enemy=False)
        self.mods_be = getDailyModifiers(self.startTime,hard_mode=False,boss_enemy=True)
        self.mods_hard_be = getDailyModifiers(self.startTime,hard_mode=True,boss_enemy=True)
        self.progress = None
        self.spoiler_log_output = "<html>No spoiler log generated</html>"
        self.num_tourney_seeds = 0

        self.settings = SeedSettings()
        self.custom_cosmetics = CustomCosmetics()

        if not os.path.exists(AUTOSAVE_FOLDER):
            os.makedirs(AUTOSAVE_FOLDER)
        auto_settings_save_path = os.path.join(AUTOSAVE_FOLDER, 'auto-save.json')
        if os.path.exists(auto_settings_save_path):
            with open(auto_settings_save_path, 'r') as source:
                try:
                    auto_settings_json = json.loads(source.read())
                    self.settings.apply_settings_json(auto_settings_json, include_private=True)
                except Exception:
                    print('Unable to apply last settings - will use defaults')
                    pass

        random.seed(str(datetime.datetime.now()))
        self.setWindowTitle("KH2 Randomizer Seed Generator ({0})".format(LOCAL_UI_VERSION))
        self.setWindowIcon(QIcon(resource_path("Module/icon.png")))
        self.setMinimumWidth(1200)
        self.setup = None
        pagelayout = QVBoxLayout()
        seed_layout = QHBoxLayout()
        progress_layout = QHBoxLayout()
        submit_layout = QHBoxLayout()
        self.tabs = QTabWidget()

        self._configure_menu_bar()

        self.preset_json = {}
        if not os.path.exists(PRESET_FOLDER):
            os.makedirs(PRESET_FOLDER)
        for file in os.listdir(PRESET_FOLDER):
            preset_name, extension = os.path.splitext(file)
            if extension == '.json':
                with open(os.path.join(PRESET_FOLDER, file), 'r') as presetData:
                    settings_json = json.loads(presetData.read())
                    self.preset_json[preset_name] = settings_json

        pagelayout.addLayout(seed_layout)
        pagelayout.addWidget(self.tabs)        
        pagelayout.addLayout(progress_layout)
        pagelayout.addLayout(submit_layout)

        seed_layout.addWidget(QLabel("Seed"))
        self.seedName=QLineEdit()
        self.seedName.setPlaceholderText("Leave blank for a random seed")
        seed_layout.addWidget(self.seedName)

        for x in self.preset_json.keys():
            if x != 'BaseDailySeed':
                self.loadPresetsMenu.addAction(x, lambda x=x: self.usePreset(x))

        self.spoiler_log = QCheckBox("Make Spoiler Log")
        self.spoiler_log.setCheckState(Qt.Checked)
        seed_layout.addWidget(self.spoiler_log)

        # self.tourney_gen_toggle = QCheckBox("Tourney Mode")
        # self.tourney_gen_toggle.setCheckState(Qt.Unchecked)
        # self.tourney_gen_toggle.setToolTip("Allows tourney organizer to make seeds with spoilers, and share seed strings that disable changing settings, but allow cosmetics.")
        # seed_layout.addWidget(self.tourney_gen_toggle)
        

        # self.rando_rando = QCheckBox("Rando Settings (Experimental)")
        # self.rando_rando.setToolTip(getRandoRandoTooltip())
        # self.rando_rando.setCheckState(Qt.Unchecked)
        # seed_layout.addWidget(self.rando_rando)

        self.widgets = [
            RewardLocationsMenu(self.settings),
            SoraMenu(self.settings),
            StartingMenu(self.settings),
            HintsMenu(self.settings),
            KeybladeMenu(self.settings),
            ItemPoolMenu(self.settings),
            ItemPlacementMenu(self.settings),
            SeedModMenu(self.settings),
            BossEnemyMenu(self.settings),
            CosmeticsMenu(self.settings, self.custom_cosmetics),
        ]

        for i in range(len(self.widgets)):
            self.tabs.addTab(self.widgets[i],self.widgets[i].getName())

        
        self.progress_label = QLabel("Progress Placeholder")
        self.progress_label.setAlignment(Qt.AlignCenter)
        self.progress_label.setFixedWidth(360)
        self.progress_bar = QProgressBar()
        progress_layout.addWidget(self.progress_label)
        progress_layout.addWidget(self.progress_bar)

        submit_layout.addWidget(QLabel("Seed Hash"))

        self.hashIconPath = Path(resource_path("static/seed-hash-icons"))
        self.hashIcons = []
        for i in range(7):
            self.hashIcons.append(QLabel())
            self.hashIcons[-1].blockSignals(True)
            submit_layout.addWidget(self.hashIcons[-1])
            
        self.clear_hash_icons()

        submit_layout.addSpacing(16)

        self.emu_button = QPushButton("Generate Seed (PCSX2)")
        self.emu_button.clicked.connect(lambda : self.makeSeed("PCSX2"))
        submit_layout.addWidget(self.emu_button, stretch=1)
        self.emu_button.setVisible(False)

        self.pc_button = QPushButton("Generate Seed (PC)")
        self.pc_button.clicked.connect(lambda : self.makeSeed("PC"))
        submit_layout.addWidget(self.pc_button, stretch=1)
        self.pc_button.setVisible(False)


        self.both_button = QPushButton("Generate Seed (PC/PCSX2)")
        self.both_button.clicked.connect(lambda : self.makeSeed("Both"))
        submit_layout.addWidget(self.both_button, stretch=1)

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

        self.recalculate = False
        settings_keys = self.settings._filtered_settings(True).keys()
        for key in settings_keys:
            self.settings.observe(key,self.get_num_enabled_locations)

    def _configure_menu_bar(self):
        menu_bar = self.menuBar()
        self.presetMenu = QMenu("Preset")
        self.presetMenu.addAction("Open Preset Folder", self.openPresetFolder)
        self.presetMenu.addAction("Save Settings as New Preset", self.savePreset)
        self.loadPresetsMenu = QMenu("Load a Preset")
        self.presetMenu.addMenu(self.loadPresetsMenu)
        self.presetMenu.addAction("Pick a Random Preset", self.randomPreset)
        
        self.seedMenu = QMenu("Share Seed")
        self.seedMenu.addAction("Save Seed to Clipboard", self.shareSeed)
        self.seedMenu.addAction("Load Seed from Clipboard", self.receiveSeed)
        self.config_menu = QMenu('Configure')
        self.config_menu.addAction('LuaBackend Hook Setup (PC Only)', self.show_luabackend_configuration)
        self.config_menu.addAction('Find OpenKH Folder (for randomized cosmetics)', self.openkh_folder_getter)
        menu_bar.addMenu(self.seedMenu)
        menu_bar.addMenu(self.presetMenu)

        self.dailyMenu = QMenu("Daily Seeds")
        self.dailyMenu.addAction("Load Seed", self.loadDailySeed)
        self.dailyMenu.addAction("Load Hard Seed", self.loadHardDailySeed)
        self.dailyMenu.addAction("Load Boss/Enemy Seed", self.loadDailySeedBE)
        self.dailyMenu.addAction("Load Hard Boss/Enemy Seed", self.loadHardDailySeedBE)
        menu_bar.addMenu(self.dailyMenu)
        menu_bar.addAction("Randomize Settings", self.randoRando)

        menu_bar.addAction("Tourney Seeds", self.makeTourneySeeds)
        
        menu_bar.addMenu(self.config_menu)

        menu_bar.addAction("About", self.showAbout)

    def closeEvent(self, e):
        settings_json = self.settings.settings_json(include_private=True)
        with open(os.path.join(AUTOSAVE_FOLDER, 'auto-save.json'), 'w') as presetData:
            presetData.write(json.dumps(settings_json, indent=4, sort_keys=True))

        self.custom_cosmetics.write_file()

        e.accept()

    def dailySeedHandler(self,difficulty,boss_enemy=False):
        self.seedName.setText(self.dailySeedName)
        self.recalculate = False

        #test all daily settings for sanity
        try:
            all_mods = allDailyModifiers()
            for m in all_mods:
                self.settings.apply_settings_json(self.preset_json['StarterSettings'])
                m.local_modifier(self.settings)
                for widget in self.widgets:
                    widget.update_widgets()
        except Exception as e:
            print(f"Error found with one of the options {e}")

        self.settings.apply_settings_json(self.preset_json['StarterSettings'])

        # use the modifications to change the preset
        mod_string = f'Updated settings for Daily Seed {self.startTime.strftime("%a %b %d %Y")}\n\n'
        which_mods = None
        if difficulty=="easy" and not boss_enemy:
            which_mods = self.mods
        elif difficulty=="easy" and boss_enemy:
            which_mods = self.mods_be
        elif difficulty=="hard" and not boss_enemy:
            which_mods = self.mods_hard
        elif difficulty=="hard" and boss_enemy:
            which_mods = self.mods_hard_be
        else:
            raise RandomizerExceptions("Improper Daily Seed Setting")

        for m in which_mods:
            m.local_modifier(self.settings)
            mod_string += m.name + ' - ' + m.description + '\n\n'

        for widget in self.widgets:
            widget.update_widgets()
        self.recalculate = True
        self.get_num_enabled_locations()

        self.fixSeedName()

        message = QMessageBox(text=mod_string)
        message.setWindowTitle('KH2 Seed Generator - Daily Seed')
        message.exec()

    def loadDailySeed(self):
        self.dailySeedHandler(difficulty="easy")

    def loadHardDailySeed(self):
        self.dailySeedHandler(difficulty="hard")

    def loadDailySeedBE(self):
        self.dailySeedHandler(difficulty="easy", boss_enemy=True)

    def loadHardDailySeedBE(self):
        self.dailySeedHandler(difficulty="hard", boss_enemy=True)

    def makeTourneySeeds(self):
        tourney_dialog = TourneySeedDialog()
        if tourney_dialog.exec():
            tourney_name, num_tourney_seeds, seed_platform, output_path = tourney_dialog.save()
            self.num_tourney_seeds = num_tourney_seeds

            self.tourney_seed_path = Path(output_path) / tourney_name
            self.tourney_name = tourney_name

            self.makeSeed(seed_platform)
            self.num_tourney_seeds = 0   

            message = QMessageBox(text=f"Done making seeds")
            message.setWindowTitle("KH2 Seed Generator")
            message.exec()

    def fixSeedName(self):
        new_string = re.sub(r'[^a-zA-Z0-9]', '', self.seedName.text())
        self.seedName.setText(new_string)
        if self.num_tourney_seeds>0:
            self.spoiler_log.setChecked(False)

    def make_rando_settings(self, catch_exception=True):
        if self.num_tourney_seeds>0:
            makeSpoilerLog = False
        else:
            makeSpoilerLog = self.spoiler_log.isChecked()

        # seed
        seedString = self.seedName.text()
        if seedString == "":
            characters = string.ascii_letters + string.digits
            seedString = (''.join(random.choice(characters) for i in range(30)))
            self.seedName.setText(seedString)

        try:
            rando_settings = RandomizerSettings(seedString,makeSpoilerLog,LOCAL_UI_VERSION,self.settings,self.createSharedString())
            # update the seed hash display
            self.update_ui_hash_icons(rando_settings)

            return rando_settings
        except RandomizerExceptions as e:
            if catch_exception:
                self.handleFailure(e)
                return None
            else:
                raise e

    def update_ui_hash_icons(self, rando_settings):
        # self.icons = []
        for index, icon in enumerate(rando_settings.seedHashIcons):
            self.hashIcons[index].setPixmap(QPixmap(str(self.hashIconPath.absolute()) + '/' + icon + '.png'))
            # self.icons.append(icon)

    def clear_hash_icons(self):
        for i in range(7):
            self.hashIcons[i].setPixmap(QPixmap(str(self.hashIconPath.absolute())+"/"+"question-mark.png"))

    def get_num_enabled_locations(self):
        if self.recalculate:
            try:
                rando_settings = self.make_rando_settings()
                dummy_rando = Randomizer(rando_settings,True)
                split_pc_emu = False
                split_pc_emu = split_pc_emu or self.settings.get(settingkey.COMMAND_MENU) != "vanilla"
                split_pc_emu = split_pc_emu or self.settings.get(settingkey.CUPS_GIVE_XP)
                split_pc_emu = split_pc_emu or self.settings.get(settingkey.REMOVE_DAMAGE_CAP)
                split_pc_emu = split_pc_emu or self.settings.get(settingkey.RETRY_DARK_THORN)
                split_pc_emu = split_pc_emu or self.settings.get(settingkey.RETRY_DFX)
                # split_pc_emu = split_pc_emu or self.settings.get(settingkey.BLOCK_COR_SKIP)
                # split_pc_emu = split_pc_emu or self.settings.get(settingkey.BLOCK_SHAN_YU_SKIP)
                split_pc_emu = split_pc_emu or (locationType.Puzzle.name in self.settings.get(settingkey.MISC_LOCATIONS_WITH_REWARDS))
                split_pc_emu = split_pc_emu or (locationType.SYNTH.name in self.settings.get(settingkey.MISC_LOCATIONS_WITH_REWARDS))
                split_pc_emu = split_pc_emu or rando_settings.enemy_options["boss"] != "Disabled"
                split_pc_emu = split_pc_emu or rando_settings.enemy_options["enemy"] != "Disabled"
                # split_pc_emu = split_pc_emu or self.settings.get(settingkey.TT1_JAILBREAK)

                
                disable_emu = False
                disable_emu = disable_emu or rando_settings.enemy_options["enemy"] == "Wild"
                disable_emu = disable_emu or rando_settings.enemy_options["bosses_replace_enemies"]
                disable_emu = disable_emu or rando_settings.enemy_options["combine_enemy_sizes"]
                disable_emu = disable_emu or rando_settings.enemy_options["combine_melee_ranged"]
                # disable_emu = disable_emu or self.settings.get(settingkey.TT1_JAILBREAK)


                self.emu_button.setVisible(split_pc_emu)
                self.pc_button.setVisible(split_pc_emu)
                self.both_button.setVisible(not split_pc_emu)
                self.emu_button.setEnabled(not disable_emu)

            except CantAssignItemException as e:
                pass
            text = f"Items: {dummy_rando.num_available_items} / Locations: {dummy_rando.num_valid_locations}"
            self.progress_bar.setRange(0,dummy_rando.num_valid_locations)
            if dummy_rando.num_valid_locations < dummy_rando.num_available_items:
                self.progress_bar.setValue(dummy_rando.num_valid_locations)
                text = "Too many "+text
            else:
                self.progress_bar.setValue(dummy_rando.num_available_items)
            self.progress_label.setText(text)

    def makeSeed(self,platform):
        self.fixSeedName()
        if self.num_tourney_seeds>0:
            message = QMessageBox(text="Tourney Mode in Use. Spoiler will be generated outside the zip, and cosmetics disabled.")
            message.setWindowTitle("KH2 Seed Generator")
            message.exec()
            # disable all cosmetics, generate a spoiler log, but don't put it in the zip
            data = {
                'platform': platform,
                'cmdMenuChoice': "vanilla",
                'customCosmeticsExecutables': [],
                'tourney': True
            }
            self.genTourneySeeds(data)
        else:
            data = {
                'platform': platform,
                'cmdMenuChoice': self.settings.get(settingkey.COMMAND_MENU),
                'customCosmeticsExecutables': [custom_file for custom_file in self.custom_cosmetics.external_executables],
                'tourney': False
            }

            rando_settings = self.make_rando_settings()
            if rando_settings is not None:
                self.genSeed(data,rando_settings)

        # rando_settings = self.make_rando_settings()
        # self.seedName.setText("")
        # rando_settings2 = self.make_rando_settings()
        # if rando_settings is not None:
        #     self.genMultiSeed(data,[rando_settings,rando_settings2])

    def downloadSeed(self):
        last_seed_folder_txt = Path(AUTOSAVE_FOLDER) / 'last_seed_folder.txt'
        output_file_name = 'randoseed.zip'
        if last_seed_folder_txt.is_file():
            last_seed_folder = Path(last_seed_folder_txt.read_text().strip())
            if last_seed_folder.is_dir():
                output_file_name = str(last_seed_folder / output_file_name)

        saveFileWidget = QFileDialog()
        saveFileWidget.setNameFilters(["Zip Seed File (*.zip)"])
        outfile_name, _ = saveFileWidget.getSaveFileName(self, "Save seed zip", output_file_name, "Zip Seed File (*.zip)")
        spoiler_outfile = outfile_name
        enemy_outfile = outfile_name
        if outfile_name!="":
            if not outfile_name.endswith(".zip"):
                outfile_name+=".zip"
            with open(outfile_name, "wb") as out_zip:
                out_zip.write(self.zip_file.getbuffer())

            last_seed_folder_txt.write_text(str(Path(outfile_name).parent))

        self.zip_file=None
        self.spoiler_log_output=None
        self.enemy_log_output=None

    def handleResult(self,result):
        self.progress.close()
        self.progress = None
        self.zip_file = result[0]
        self.spoiler_log_output = result[1] if result[1] else "<html>No spoiler log generated</html>"
        self.enemy_log_output = result[2]
        self.downloadSeed()

        
    def handleMultiResult(self,result):
        self.progress.close()
        self.progress = None
        for res0,res1,res2 in result:
            self.zip_file = res0
            self.spoiler_log_output = res1 if res1 else "<html>No spoiler log generated</html>"
            self.enemy_log_output = res2
            self.downloadSeed()

    def handleFailure(self, failure: Exception):
        if self.progress is not None:
            self.progress.close()
        self.progress = None
        message = QMessageBox(text=str(repr(failure)))
        message.setTextInteractionFlags(Qt.TextSelectableByMouse)
        message.setWindowTitle("Seed Generation Error")
        message.exec()
        if not isinstance(failure,RandomizerExceptions):
            raise failure

    def genSeed(self,data,rando_settings):
        self.thread = QThread()
        displayedSeedName = rando_settings.random_seed
        self.progress = QProgressDialog(f"Creating seed with name {displayedSeedName}","Cancel",0,0,None)
        self.progress.setWindowTitle("Making your Seed, please wait...")
        # self.progress.setCancelButton(None)
        self.progress.setModal(True)
        self.progress.show()

        self.thread = GenSeedThread()
        self.thread.provideData(data,rando_settings)
        self.thread.finished.connect(self.handleResult)
        self.thread.failed.connect(self.handleFailure)
        
        self.progress.canceled.connect(lambda : self.thread.terminate())
        self.thread.start()

    def genTourneySeeds(self,data):
        self.tourney_seed_path.mkdir(parents=True, exist_ok=True)

        self.tourney_spoilers = TourneySeedSaver(self.tourney_seed_path,self.tourney_name)
        for seed_number in range(0,self.num_tourney_seeds):
            characters = string.ascii_letters + string.digits
            seedString = (''.join(random.choice(characters) for i in range(30)))
            self.seedName.setText(seedString)
            tourney_rando_settings = self.make_rando_settings()
            if tourney_rando_settings is not None:
                self.thread = QThread()
                self.progress = QProgressDialog(f"Creating seed number {seed_number}...","Cancel",0,0,None)
                self.progress.setWindowTitle("Making your Seed, please wait...")
                # self.progress.setCancelButton(None)
                self.progress.setModal(True)
                self.progress.show()
                zip_file, spoiler_log, enemy_log = generateSeed(tourney_rando_settings, data)
                if self.progress:
                    self.progress.close()
                self.progress = None
                self.tourney_spoilers.add_seed(self.createSharedString(),tourney_rando_settings,spoiler_log)
        self.tourney_spoilers.save()

    def genMultiSeed(self,data,rando_settings):
        self.thread = QThread()
        displayedSeedName = rando_settings[0].random_seed
        self.progress = QProgressDialog(f"Creating seed with name {displayedSeedName}","Cancel",0,0,None)
        self.progress.setWindowTitle("Making your Seed, please wait...")
        # self.progress.setCancelButton(None)
        self.progress.setModal(True)
        self.progress.show()

        self.thread = MultiGenSeedThread()
        self.thread.provideData(data,rando_settings)
        self.thread.finished.connect(self.handleMultiResult)
        self.thread.failed.connect(self.handleFailure)
        self.progress.canceled.connect(lambda : self.thread.terminate())
        self.thread.start()

    def savePreset(self):
        preset_name, ok = QInputDialog.getText(self, 'Make New Preset', 'Enter a name for your preset...')
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        preset_name = ''.join(c for c in preset_name if c in valid_chars)
        if ok:
            # add current settings to saved presets, add to current preset list, change preset selection.
            settings_json = self.settings.settings_json()
            self.preset_json[preset_name] = settings_json
            self.loadPresetsMenu.addAction(preset_name, lambda: self.usePreset(preset_name))
            with open(os.path.join(PRESET_FOLDER, preset_name + '.json'), 'w') as presetData:
                presetData.write(json.dumps(settings_json, indent=4, sort_keys=True))

    def randomPreset(self):
        preset_select_dialog = RandomPresetDialog(self.preset_json.keys())
        if preset_select_dialog.exec():
            random_preset_list = preset_select_dialog.save()
            if len(random_preset_list) == 0:
                message = QMessageBox(text="Need at least 1 preset selected")
                message.setWindowTitle("KH2 Seed Generator")
                message.exec()
            else:
                seedString = self.seedName.text()
                if seedString == "":
                    characters = string.ascii_letters + string.digits
                    seedString = (''.join(random.choice(characters) for i in range(30)))
                    self.seedName.setText(seedString)
                random.seed(self.seedName.text())
                selected_preset = random.choice(random_preset_list)
                self.usePreset(selected_preset)
                message = QMessageBox(text=f"Picked {selected_preset}")
                message.setWindowTitle("KH2 Seed Generator")
                message.exec()

    def randoRando(self):
        preset_select_dialog = RandomSettingsDialog(self.settings)
        if preset_select_dialog.exec():
            backup_settings = self.settings.settings_string()
            selected_random_settings = preset_select_dialog.save()
            if len(selected_random_settings) == 0:
                message = QMessageBox(text="No randomized settings chosen, doing nothing")
                message.setWindowTitle("KH2 Seed Generator")
                message.exec()
                return

            valid_seed = False
            invalid_seed_count = 0
            last_exception = None
            while not valid_seed and invalid_seed_count < 10:
                try:
                    #randomize
                    randomize_settings(self.settings,selected_random_settings)
                    self.make_rando_settings(catch_exception=False)
                    valid_seed = True
                except RandomizerExceptions as e:
                    # we got exception, so try again
                    invalid_seed_count+=1
                    self.settings.apply_settings_string(backup_settings)
                    last_exception = e
            
            if valid_seed:
                for widget in self.widgets:
                    widget.update_widgets()
                message = QMessageBox(text=f"Randomized your settings, don't forget to generate your seed.")
                message.setWindowTitle("KH2 Seed Generator")
                message.exec()
            else:
                self.handleFailure(last_exception)

    def openPresetFolder(self):
        os.startfile(PRESET_FOLDER)

    def usePreset(self, preset_name: str):
        settings_json = self.preset_json[preset_name]
        self.recalculate = False
        self.settings.apply_settings_json(settings_json)
        for widget in self.widgets:
            widget.update_widgets()
        self.recalculate = True
        self.get_num_enabled_locations()

    def shareSeed(self):
        output_text = self.createSharedString()

        pc.copy(output_text)
        message = QMessageBox(text="Copied seed to clipboard")
        message.setWindowTitle("KH2 Seed Generator")
        message.exec()

    def createSharedString(self):
        self.fixSeedName()

        # if seed hasn't been set yet, make one
        current_seed = self.seedName.text()
        if current_seed == "":
            characters = string.ascii_letters + string.digits
            current_seed = (''.join(random.choice(characters) for i in range(30)))
            self.seedName.setText(current_seed)

        shared_seed = SharedSeed(
            generator_version=LOCAL_UI_VERSION,
            seed_name=current_seed,
            spoiler_log=self.spoiler_log.isChecked(),
            settings_string=self.settings.settings_string(),
            tourney_gen=self.num_tourney_seeds>0
        )
        output_text = shared_seed.to_share_string()
        return output_text

    def receiveSeed(self):
        try:
            print("".join(str(pc.paste()).splitlines()))
            shared_seed = SharedSeed.from_share_string(
                local_generator_version=LOCAL_UI_VERSION,
                share_string="".join(str(pc.paste()).splitlines())
            )
            # self.tourney_gen_toggle.setCheckState(Qt.Unchecked)
        except ShareStringException as exception:
            message = QMessageBox(text=exception.message)
            message.setWindowTitle("KH2 Seed Generator")
            message.exec()
            return

        # clear hash icons when loading a seed from clipboard
        self.clear_hash_icons()

        if shared_seed.tourney_gen:
            self.seedName.setDisabled(True)
            self.seedName.setHidden(True)
            self.spoiler_log.setDisabled(True)
            # self.tourney_gen_toggle.setDisabled(True)
            # self.rando_rando.setDisabled(True)
            for w in self.widgets:
                if not isinstance(w,CosmeticsMenu):
                    w.disable_widgets()
        self.seedName.setText(shared_seed.seed_name)
        self.spoiler_log.setCheckState(Qt.Checked if shared_seed.spoiler_log else Qt.Unchecked)
        self.recalculate = False
        self.settings.apply_settings_string(shared_seed.settings_string)
        for widget in self.widgets:
            widget.update_widgets()
        self.recalculate = True
        self.get_num_enabled_locations()

        post_shared_seed = SharedSeed.from_share_string(local_generator_version=LOCAL_UI_VERSION,share_string = self.createSharedString())

        if post_shared_seed.seed_name != shared_seed.seed_name or post_shared_seed.spoiler_log != shared_seed.spoiler_log or post_shared_seed.settings_string != shared_seed.settings_string:
            print(shared_seed.settings_string)
            print(post_shared_seed.settings_string)
            message = QMessageBox(text="There was an error getting the correct settings from the clipboard, try restarting the generator and trying again. If that fails, ask for the zip from the sharer.")
            message.setWindowTitle("KH2 Seed Generator")
            message.exec()
        else:
            message = QMessageBox(text="Received seed from clipboard")
            message.setWindowTitle("KH2 Seed Generator")
            message.exec()

    @staticmethod
    def openkh_folder_getter():
        save_file_widget = QFileDialog()
        selected_directory = save_file_widget.getExistingDirectory()

        if selected_directory is None or selected_directory == "":
            return

        selected_path = Path(selected_directory)
        if not (selected_path / 'OpenKh.Tools.ModsManager.exe').is_file():
            message = QMessageBox(text='Not a valid OpenKH folder')
            message.setWindowTitle('KH2 Seed Generator')
            message.exec()
        else:
            CosmeticsMod.write_openkh_path(selected_directory)

            message = QMessageBox(text="Restart the seed generator to apply changes.")
            message.setWindowTitle("KH2 Seed Generator")
            message.exec()

    @staticmethod
    def show_luabackend_configuration():
        dialog = LuaBackendSetupDialog()
        dialog.exec()

    def firstTimeSetup(self):
        print("First Time Setup")
        if self.setup is None:
            self.setup = FirstTimeSetup()
            self.setup.show()

    def showAbout(self):
        aboutText = '''
Kingdom Hearts II Final Mix Zip Seed Generator Version {0}<br>
Created by Equations19, Thundrio, Tommadness, and ZakTheRobot<br><br>

Thank you to all contributors, testers, and advocates.<br><br>

<a href="https://tommadness.github.io/KH2Randomizer" style="color: #4dd0e1">Website</a><br>
<a href="https://github.com/tommadness/KH2Randomizer" style="color: #4dd0e1">Github Link</a><br>
<a href="https://discord.gg/KH2FMRando" style="color: #4dd0e1">KH2 Randomizer Discord</a><br><br>

<a href="https://github.com/tommadness/KH2Randomizer/tree/local_ui#acknowledgements" style="color: #4dd0e1">Acknowledgements</a><br><br>

Uses the qt-material library for theming.<br>Copyright (c) 2020, GCPDS
<a href="https://github.com/UN-GCPDS/qt-material/blob/master/LICENSE" style="color: #4dd0e1">License</a>



'''.format(LOCAL_UI_VERSION)
        message = QMessageBox(text=aboutText)
        message.setTextFormat(Qt.RichText)
        message.setWindowTitle("About")
        message.setWindowIcon(QIcon(resource_path("Module/icon.png")))
        message.exec()


if __name__=="__main__":
    app = QApplication([])

    QtGui.QFontDatabase.addApplicationFont(resource_path('static/KHMenu.otf'))

    window = KH2RandomizerApp()

    apply_stylesheet(app, theme='dark_cyan.xml')
    stylesheet = app.styleSheet()
    with open(resource_path('UI/stylesheet.css')) as file:
        app.setStyleSheet(stylesheet + file.read().format(**os.environ))

    window.recalculate = True
    try:
        window.get_num_enabled_locations()
    except RandomizerExceptions as e:
        pass
    window.show()
    #commenting out first time setup for 2.999 version
    # configPath = Path("rando-config.yml")
    # if not configPath.is_file() or not os.environ.get("ALWAYS_SETUP") is None:
    #     window.firstTimeSetup()

    sys.exit(app.exec())
