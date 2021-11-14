from Class.itemClass import KH2Item
from List.configDict import itemType
import itertools


class Items:
    @staticmethod
    def getItemList():
        return [
            KH2Item(593, "Proof of Connection", itemType.PROOF_OF_CONNECTION),
            KH2Item(594, "Proof of Nonexistence", itemType.PROOF),
            KH2Item(595, "Proof of Peace", itemType.PROOF_OF_PEACE),

            KH2Item(21, "Fire Element", itemType.FIRE),
            KH2Item(21, "Fire Element", itemType.FIRE),
            KH2Item(21, "Fire Element", itemType.FIRE),

            KH2Item(22, "Blizzard Element", itemType.BLIZZARD),
            KH2Item(22, "Blizzard Element", itemType.BLIZZARD),
            KH2Item(22, "Blizzard Element", itemType.BLIZZARD),

            KH2Item(23, "Thunder Element", itemType.THUNDER),
            KH2Item(23, "Thunder Element", itemType.THUNDER),
            KH2Item(23, "Thunder Element", itemType.THUNDER),

            KH2Item(24, "Cure Element", itemType.CURE),
            KH2Item(24, "Cure Element", itemType.CURE),
            KH2Item(24, "Cure Element", itemType.CURE),

            KH2Item(87, "Magnet Element", itemType.MAGNET),
            KH2Item(87, "Magnet Element", itemType.MAGNET),
            KH2Item(87, "Magnet Element", itemType.MAGNET),

            KH2Item(88, "Reflect Element", itemType.REFLECT),
            KH2Item(88, "Reflect Element", itemType.REFLECT),
            KH2Item(88, "Reflect Element", itemType.REFLECT),

            KH2Item(94, "High Jump",itemType.GROWTH_ABILITY),
            KH2Item(95, "High Jump",itemType.GROWTH_ABILITY),
            KH2Item(96, "High Jump",itemType.GROWTH_ABILITY),
            KH2Item(97, "High Jump",itemType.GROWTH_ABILITY),

            KH2Item(98, "Quick Run",itemType.GROWTH_ABILITY),
            KH2Item(99, "Quick Run",itemType.GROWTH_ABILITY),
            KH2Item(100, "Quick Run",itemType.GROWTH_ABILITY),
            KH2Item(101, "Quick Run",itemType.GROWTH_ABILITY),

            KH2Item(102, "Aerial Dodge",itemType.GROWTH_ABILITY),
            KH2Item(103, "Aerial Dodge",itemType.GROWTH_ABILITY),
            KH2Item(104, "Aerial Dodge",itemType.GROWTH_ABILITY),
            KH2Item(105, "Aerial Dodge",itemType.GROWTH_ABILITY),

            KH2Item(106, "Glide",itemType.GROWTH_ABILITY),
            KH2Item(107, "Glide",itemType.GROWTH_ABILITY),
            KH2Item(108, "Glide",itemType.GROWTH_ABILITY),
            KH2Item(109, "Glide",itemType.GROWTH_ABILITY),

            KH2Item(564, "Dodge Roll",itemType.GROWTH_ABILITY),
            KH2Item(565, "Dodge Roll",itemType.GROWTH_ABILITY),
            KH2Item(566, "Dodge Roll",itemType.GROWTH_ABILITY),
            KH2Item(567, "Dodge Roll",itemType.GROWTH_ABILITY),

            KH2Item(26, "Valor Form", itemType.FORM),
            KH2Item(27, "Wisdom Form", itemType.FORM),
            KH2Item(29, "Final Form", itemType.FORM),
            KH2Item(31, "Master Form", itemType.FORM),
            KH2Item(563, "Limit Form", itemType.FORM),

            KH2Item(32, "Torn Pages",itemType.TORN_PAGE),
            KH2Item(32, "Torn Pages",itemType.TORN_PAGE),
            KH2Item(32, "Torn Pages",itemType.TORN_PAGE),
            KH2Item(32, "Torn Pages",itemType.TORN_PAGE),
            KH2Item(32, "Torn Pages",itemType.TORN_PAGE),

            KH2Item(159, "Lamp Charm (Genie)",itemType.SUMMON),
            KH2Item(160, "Feather Charm (Peter Pan)", itemType.SUMMON),
            KH2Item(25, "Ukulele Charm (Stitch)", itemType.SUMMON),
            KH2Item(383, "Baseball Charm (Chicken Little)", itemType.SUMMON),

            KH2Item(226, "Secret Ansem's Report 1", itemType.REPORT),
            KH2Item(227, "Secret Ansem's Report 2", itemType.REPORT),
            KH2Item(228, "Secret Ansem's Report 3", itemType.REPORT),
            KH2Item(229, "Secret Ansem's Report 4", itemType.REPORT),
            KH2Item(230, "Secret Ansem's Report 5", itemType.REPORT),
            KH2Item(231, "Secret Ansem's Report 6", itemType.REPORT),
            KH2Item(232, "Secret Ansem's Report 7", itemType.REPORT),
            KH2Item(233, "Secret Ansem's Report 8", itemType.REPORT),
            KH2Item(234, "Secret Ansem's Report 9", itemType.REPORT),
            KH2Item(235, "Secret Ansem's Report 10", itemType.REPORT),
            KH2Item(236, "Secret Ansem's Report 11", itemType.REPORT),
            KH2Item(237, "Secret Ansem's Report 12", itemType.REPORT),
            KH2Item(238, "Secret Ansem's Report 13", itemType.REPORT),

            KH2Item(42,"Oathkeeper", itemType.KEYBLADE),
            KH2Item(43,"Oblivion",itemType.KEYBLADE),
            KH2Item(480, "Star Seeker", itemType.KEYBLADE),
            KH2Item(481, "Hidden Dragon", itemType.KEYBLADE),
            KH2Item(484,"Hero's Crest",itemType.KEYBLADE),
            KH2Item(485,"Monochrome",itemType.KEYBLADE),
            KH2Item(486,"Follow the Wind",itemType.KEYBLADE),
            KH2Item(487,"Circle of Life",itemType.KEYBLADE),
            KH2Item(488,"Photon Debugger",itemType.KEYBLADE),
            KH2Item(489,"Gull Wing",itemType.KEYBLADE),
            KH2Item(490,"Rumbling Rose",itemType.KEYBLADE),
            KH2Item(491,"Guardian Soul",itemType.KEYBLADE),
            KH2Item(492,"Wishing Lamp",itemType.KEYBLADE),
            KH2Item(493,"Decisive Pumpkin",itemType.KEYBLADE),
            KH2Item(494,"Sleeping Lion",itemType.KEYBLADE),
            KH2Item(495,"Sweet Memories",itemType.KEYBLADE),
            KH2Item(496,"Mysterious Abyss",itemType.KEYBLADE),
            KH2Item(543,"Two Become One",itemType.KEYBLADE),
            KH2Item(497,"Fatal Crest",itemType.KEYBLADE),
            KH2Item(498,"Bond of Flame",itemType.KEYBLADE),
            KH2Item(499,"Fenrir",itemType.KEYBLADE),
            KH2Item(500,"Ultima Weapon",itemType.KEYBLADE),
            KH2Item(544,"Winner's Proof",itemType.KEYBLADE),

            KH2Item(546, "Centurion+", itemType.STAFF), #StatEntry = 151
            KH2Item(150, "Meteor Staff", itemType.STAFF), #StatEntry = 89
            KH2Item(155, "Nobody Lance", itemType.STAFF), #StatEntry = 94
            KH2Item(549, "Precious Mushroom", itemType.STAFF), #StatEntry = 154
            KH2Item(550, "Precious Mushroom+", itemType.STAFF), #StatEntry = 155
            KH2Item(551, "Premium Mushroom", itemType.STAFF), #StatEntry = 156
            KH2Item(154, "Rising Dragon", itemType.STAFF), #StatEntry = 93
            KH2Item(503, "Save The Queen+", itemType.STAFF), #StatEntry = 146
            KH2Item(156, "Shaman's Relic", itemType.STAFF), #StatEntry = 95

            KH2Item(146, "Akashic Record", itemType.SHIELD), #StatEntry = 107
            KH2Item(553, "Frozen Pride+", itemType.SHIELD), #StatEntry = 158
            KH2Item(145, "Genji Shield", itemType.SHIELD), #StatEntry = 106
            KH2Item(556, "Majestic Mushroom", itemType.SHIELD), #StatEntry = 161
            KH2Item(557, "Majestic Mushroom+", itemType.SHIELD), #StatEntry = 162
            KH2Item(147, "Nobody Guard", itemType.SHIELD), #StatEntry = 108
            KH2Item(141, "Ogre Shield", itemType.SHIELD), #StatEntry = 102
            KH2Item(504, "Save The King+", itemType.SHIELD), #StatEntry = 147
            KH2Item(558, "Ultimate Mushroom", itemType.SHIELD), #StatEntry = 163

            KH2Item(8, "Ability Ring", itemType.ACCESSORY),
            KH2Item(9, "Engineer's Ring", itemType.ACCESSORY),
            KH2Item(10, "Technician's Ring", itemType.ACCESSORY),
            KH2Item(38, "Skill Ring", itemType.ACCESSORY),
            KH2Item(39, "Skillful Ring", itemType.ACCESSORY),
            KH2Item(11, "Expert's Ring", itemType.ACCESSORY),
            KH2Item(34, "Master's Ring", itemType.ACCESSORY),
            KH2Item(52, "Cosmic Ring", itemType.ACCESSORY),
            KH2Item(599, "Executive's Ring", itemType.ACCESSORY),
            KH2Item(12, "Sardonyx Ring", itemType.ACCESSORY),
            KH2Item(13, "Tourmaline Ring", itemType.ACCESSORY),
            KH2Item(14, "Aquamarine Ring", itemType.ACCESSORY),
            KH2Item(15, "Garnet Ring", itemType.ACCESSORY),
            KH2Item(16, "Diamond Ring", itemType.ACCESSORY),
            KH2Item(17, "Silver Ring", itemType.ACCESSORY),
            KH2Item(18, "Gold Ring", itemType.ACCESSORY),
            KH2Item(19, "Platinum Ring", itemType.ACCESSORY),
            KH2Item(20, "Mythril Ring", itemType.ACCESSORY),
            KH2Item(28, "Orichalcum Ring", itemType.ACCESSORY),
            KH2Item(40, "Soldier Earring", itemType.ACCESSORY),
            KH2Item(46, "Fencer Earring", itemType.ACCESSORY),
            KH2Item(47, "Mage Earring", itemType.ACCESSORY),
            KH2Item(48, "Slayer Earring", itemType.ACCESSORY),
            KH2Item(53, "Medal", itemType.ACCESSORY),
            KH2Item(35, "Moon Amulet", itemType.ACCESSORY),
            KH2Item(36, "Star Charm", itemType.ACCESSORY),
            KH2Item(56, "Cosmic Arts", itemType.ACCESSORY),
            KH2Item(57, "Shadow Archive", itemType.ACCESSORY),
            KH2Item(58, "Shadow Archive+", itemType.ACCESSORY),
            KH2Item(64, "Full Bloom", itemType.ACCESSORY),
            KH2Item(66, "Full Bloom+", itemType.ACCESSORY),
            KH2Item(65, "Draw Ring", itemType.ACCESSORY),
            KH2Item(63, "Lucky Ring", itemType.ACCESSORY),

            KH2Item(67, "Elven Bandana", itemType.ARMOR),
            KH2Item(68, "Divine Bandana", itemType.ARMOR),
            KH2Item(78, "Protect Belt", itemType.ARMOR),
            KH2Item(79, "Gaia Belt", itemType.ARMOR),
            KH2Item(69, "Power Band", itemType.ARMOR),
            KH2Item(70, "Buster Band", itemType.ARMOR),
            KH2Item(111, "Cosmic Belt", itemType.ARMOR),
            KH2Item(173, "Fire Bangle", itemType.ARMOR),
            KH2Item(174, "Fira Bangle", itemType.ARMOR),
            KH2Item(197, "Firaga Bangle", itemType.ARMOR),
            KH2Item(284, "Firagun Bangle", itemType.ARMOR),
            KH2Item(286, "Blizzard Armlet", itemType.ARMOR),
            KH2Item(287, "Blizzara Armlet", itemType.ARMOR),
            KH2Item(288, "Blizzaga Armlet", itemType.ARMOR),
            KH2Item(289, "Blizzagun Armlet", itemType.ARMOR),
            KH2Item(291, "Thunder Trinket", itemType.ARMOR),
            KH2Item(292, "Thundara Trinket", itemType.ARMOR),
            KH2Item(293, "Thundaga Trinket", itemType.ARMOR),
            KH2Item(294, "Thundagun Trinket", itemType.ARMOR),
            KH2Item(132, "Shock Charm", itemType.ARMOR),
            KH2Item(133, "Shock Charm+", itemType.ARMOR),
            KH2Item(296, "Shadow Anklet", itemType.ARMOR),
            KH2Item(297, "Dark Anklet", itemType.ARMOR),
            KH2Item(298, "Midnight Anklet", itemType.ARMOR),
            KH2Item(299, "Chaos Anklet", itemType.ARMOR),
            KH2Item(305, "Champion Belt", itemType.ARMOR),
            KH2Item(301, "Abas Chain", itemType.ARMOR),
            KH2Item(302, "Aegis Chain", itemType.ARMOR),
            KH2Item(303, "Acrisius", itemType.ARMOR),
            KH2Item(307, "Acrisius+", itemType.ARMOR),
            KH2Item(308, "Cosmic Chain", itemType.ARMOR),
            KH2Item(306, "Petite Ribbon", itemType.ARMOR),
            KH2Item(304, "Ribbon", itemType.ARMOR),
            KH2Item(157, "Grand Ribbon", itemType.ARMOR),

            KH2Item(535,"Munny Pouch",itemType.MUNNY_POUCH),
            KH2Item(362, "Munny Pouch",itemType.MUNNY_POUCH),

            KH2Item(369, "Membership Card", itemType.MEMBERSHIPCARD),
            KH2Item(537, "Hades Cup Trophy", itemType.TROPHY),

            KH2Item(363, "Crystal Orb", itemType.KEYITEM),
            KH2Item(364, "Seifer's Trophy", itemType.KEYITEM),
            #KH2Item(365, "Tournament Poster", itemType.KEYITEM),
            #KH2Item(366, "Poster", itemType.KEYITEM),
            #KH2Item(367, "Letter", itemType.KEYITEM),
            KH2Item(368, "Namine's Sketches", itemType.KEYITEM),
            KH2Item(370, "Olympus Stone", itemType.KEYITEM),
            KH2Item(371, "Auron's Statue", itemType.KEYITEM),
            KH2Item(372, "Cursed Medallion", itemType.KEYITEM),
            KH2Item(373, "Presents", itemType.KEYITEM),
            KH2Item(374, "Decoy Presents", itemType.KEYITEM),
            KH2Item(375, "Ice Cream", itemType.KEYITEM),
            KH2Item(376, "Picture", itemType.KEYITEM),
            KH2Item(538, '"The Struggle" Trophy', itemType.KEYITEM),

            KH2Item(382, "Mega-Recipe", itemType.RECIPE),
            KH2Item(449, "Star Recipe", itemType.RECIPE),
            KH2Item(450, "Recovery Recipe", itemType.RECIPE),
            KH2Item(451, "Skill Recipe", itemType.RECIPE),
            KH2Item(452, "Guard Recipe", itemType.RECIPE),
            KH2Item(464, "Road to Discovery", itemType.RECIPE),
            KH2Item(465, "Strength Beyond Strength", itemType.RECIPE),
            KH2Item(466, "Book of Shadows", itemType.RECIPE),
            KH2Item(467, "Cloaked Thunder", itemType.RECIPE),
            KH2Item(468, "Eternal Blossom", itemType.RECIPE),
            KH2Item(469, "Rare Document", itemType.RECIPE),
            KH2Item(475, "Style Recipe", itemType.RECIPE),
            KH2Item(476, "Moon Recipe", itemType.RECIPE),
            KH2Item(477, "Queen Recipe", itemType.RECIPE),
            KH2Item(478, "King Recipe", itemType.RECIPE),
            KH2Item(479, "Ultimate Recipe", itemType.RECIPE),

            KH2Item(533, "Tower Map", itemType.MAP),
            KH2Item(255, "Twilight Town Map", itemType.MAP),
            KH2Item(531, "Sunset Hill Map", itemType.MAP),
            KH2Item(532, "Mansion Map", itemType.MAP),
            KH2Item(513, "Castle Perimeter Map", itemType.MAP),
            KH2Item(514, "The Great Maw Map", itemType.MAP),
            KH2Item(253, "Marketplace Map", itemType.MAP),
            KH2Item(586, "Dark Remembrance Map", itemType.MAP),
            KH2Item(590, "Depths of Remembrance Map", itemType.MAP),
            KH2Item(592, "Garden of Assemblage Map", itemType.MAP),
            KH2Item(90, "Castle Map", itemType.MAP),
            KH2Item(91, "Basement Map", itemType.MAP),
            KH2Item(92, "Castle Walls Map", itemType.MAP),
            KH2Item(135, "Underworld Map", itemType.MAP),
            KH2Item(136, "Caverns Map", itemType.MAP),
            KH2Item(134, "Coliseum Map", itemType.MAP),
            KH2Item(121, "Cave of Wonders Map", itemType.MAP),
            KH2Item(122, "Ruins Map", itemType.MAP),
            KH2Item(120, "Agrabah Map", itemType.MAP),
            KH2Item(130, "Palace Map", itemType.MAP),
            KH2Item(112, "Encampment Area Map", itemType.MAP),
            KH2Item(113, "Village Area Map", itemType.MAP),
            KH2Item(125, "100 Acre Wood Map", itemType.MAP),
            KH2Item(127, "Piglet's House Map", itemType.MAP),
            KH2Item(126, "Rabbit's House Map", itemType.MAP),
            KH2Item(128, "Kanga's House Map", itemType.MAP),
            KH2Item(129, "Spooky Cave Map", itemType.MAP),
            KH2Item(124, "Starry Hill Map", itemType.MAP),
            KH2Item(512, "Savannah Map", itemType.MAP),
            KH2Item(252, "Pride Rock Map", itemType.MAP),
            KH2Item(511, "Oasis Map", itemType.MAP),
            KH2Item(123, "Undersea Kingdom Map", itemType.MAP),
            KH2Item(119, "Disney Castle Map", itemType.MAP),
            KH2Item(114, "Cornerstone Hill Map", itemType.MAP),
            KH2Item(518, "Window of Time Map", itemType.MAP),
            KH2Item(115, "Window of Time Map?", itemType.MAP),
            KH2Item(116, "Lilliput Map", itemType.MAP),
            KH2Item(117, "Building Site Map", itemType.MAP),
            KH2Item(118, "Mickey's House Map", itemType.MAP),
            KH2Item(250, "Halloween Town Map", itemType.MAP),
            KH2Item(509, "Christmas Town Map", itemType.MAP),
            KH2Item(510, "Curly Hill Map", itemType.MAP),
            KH2Item(251, "Naval Map", itemType.MAP),
            KH2Item(507, "Isla de Muerta Map", itemType.MAP),
            KH2Item(508, "Ship Graveyard Map", itemType.MAP),
            KH2Item(505, "The Interceptor Map", itemType.MAP),
            KH2Item(506, "The Black Pearl Map", itemType.MAP),
            KH2Item(254, "Pit Cell Area Map", itemType.MAP),
            KH2Item(515, "I/O Tower Map", itemType.MAP),
            KH2Item(516, "Central Computer Core Map", itemType.MAP),
            KH2Item(517, "Solar Sailer Simulation Map", itemType.MAP),
            KH2Item(256, "Dark City Map", itemType.MAP),
            KH2Item(536, "Castle That Never Was Map", itemType.MAP),
        ] + list(itertools.repeat(KH2Item(279, "AP Boost", itemType.ITEM),50))

    @staticmethod
    def getStatItems():
        """Get different dummy items that represent stat bonuses (Dummy 23, 24, 25, 26, 27, 16)"""
        return list(itertools.repeat(KH2Item(470, "Max HP Up", itemType.STAT),20)) + \
            list(itertools.repeat(KH2Item(471, "Max MP Up", itemType.STAT),4)) + \
            list(itertools.repeat(KH2Item(472, "Drive Gauge Up", itemType.STAT),6)) + \
            list(itertools.repeat(KH2Item(473, "Armor Slot Up", itemType.STAT),3)) + \
            list(itertools.repeat(KH2Item(474, "Accessory Slot Up", itemType.STAT),3)) + \
            list(itertools.repeat(KH2Item(463, "Item Slot Up", itemType.STAT),5))

    @staticmethod
    def getPromiseCharm():
        return KH2Item(524, "PromiseCharm",itemType.PROMISE_CHARM)

    @staticmethod
    def getSupportAbilityList():
        return [
            KH2Item(138,"Scan",itemType.SUPPORT_ABILITY),
            KH2Item(138,"Scan",itemType.SUPPORT_ABILITY),
            KH2Item(158,"Aerial Recovery",itemType.SUPPORT_ABILITY),
            KH2Item(539,"Combo Master",itemType.SUPPORT_ABILITY),
            KH2Item(162,"Combo Plus",itemType.SUPPORT_ABILITY),
            KH2Item(162,"Combo Plus",itemType.SUPPORT_ABILITY),
            KH2Item(162,"Combo Plus",itemType.SUPPORT_ABILITY),
            KH2Item(163,"Air Combo Plus",itemType.SUPPORT_ABILITY),
            KH2Item(163,"Air Combo Plus",itemType.SUPPORT_ABILITY),
            KH2Item(163,"Air Combo Plus",itemType.SUPPORT_ABILITY),
            KH2Item(390,"Combo Boost",itemType.SUPPORT_ABILITY),
            KH2Item(390,"Combo Boost",itemType.SUPPORT_ABILITY),
            KH2Item(391,"Air Combo Boost",itemType.SUPPORT_ABILITY),
            KH2Item(391,"Air Combo Boost",itemType.SUPPORT_ABILITY),
            KH2Item(392,"Reaction Boost",itemType.SUPPORT_ABILITY),
            KH2Item(392,"Reaction Boost",itemType.SUPPORT_ABILITY),
            KH2Item(392,"Reaction Boost",itemType.SUPPORT_ABILITY),
            KH2Item(393,"Finishing Plus",itemType.SUPPORT_ABILITY),
            KH2Item(393,"Finishing Plus",itemType.SUPPORT_ABILITY),
            KH2Item(393,"Finishing Plus",itemType.SUPPORT_ABILITY),
            KH2Item(394,"Negative Combo",itemType.SUPPORT_ABILITY),
            KH2Item(394,"Negative Combo",itemType.SUPPORT_ABILITY),
            KH2Item(395,"Berserk Charge",itemType.SUPPORT_ABILITY),
            KH2Item(395,"Berserk Charge",itemType.SUPPORT_ABILITY),
            KH2Item(396,"Damage Drive",itemType.SUPPORT_ABILITY),
            KH2Item(397,"Drive Boost",itemType.SUPPORT_ABILITY),
            KH2Item(397,"Drive Boost",itemType.SUPPORT_ABILITY),
            KH2Item(398,"Form Boost",itemType.SUPPORT_ABILITY),
            KH2Item(398,"Form Boost",itemType.SUPPORT_ABILITY),
            KH2Item(398,"Form Boost",itemType.SUPPORT_ABILITY),
            KH2Item(399,"Summon Boost",itemType.SUPPORT_ABILITY),
            KH2Item(400,"Combination Boost",itemType.SUPPORT_ABILITY),
            KH2Item(401,"Experience Boost",itemType.SUPPORT_ABILITY),
            KH2Item(401,"Experience Boost",itemType.SUPPORT_ABILITY),
            KH2Item(402,"Leaf Bracer",itemType.SUPPORT_ABILITY),
            KH2Item(403,"Magic Lock-On",itemType.SUPPORT_ABILITY),
            KH2Item(405,"Draw",itemType.SUPPORT_ABILITY),
            KH2Item(405,"Draw",itemType.SUPPORT_ABILITY),
            KH2Item(405,"Draw",itemType.SUPPORT_ABILITY),
            KH2Item(405,"Draw",itemType.SUPPORT_ABILITY),
            KH2Item(406,"Jackpot",itemType.SUPPORT_ABILITY),
            KH2Item(406,"Jackpot",itemType.SUPPORT_ABILITY),
            KH2Item(407,"Lucky Lucky",itemType.SUPPORT_ABILITY),
            KH2Item(407,"Lucky Lucky",itemType.SUPPORT_ABILITY),
            KH2Item(407,"Lucky Lucky",itemType.SUPPORT_ABILITY),
            KH2Item(540,"Drive Converter",itemType.SUPPORT_ABILITY),
            KH2Item(540,"Drive Converter",itemType.SUPPORT_ABILITY),
            KH2Item(408,"Fire Boost",itemType.SUPPORT_ABILITY),
            KH2Item(408,"Fire Boost",itemType.SUPPORT_ABILITY),
            KH2Item(409,"Blizzard Boost",itemType.SUPPORT_ABILITY),
            KH2Item(409,"Blizzard Boost",itemType.SUPPORT_ABILITY),
            KH2Item(410,"Thunder Boost",itemType.SUPPORT_ABILITY),
            KH2Item(410,"Thunder Boost",itemType.SUPPORT_ABILITY),
            KH2Item(411,"Item Boost",itemType.SUPPORT_ABILITY),
            KH2Item(411,"Item Boost",itemType.SUPPORT_ABILITY),
            KH2Item(412,"MP Rage",itemType.SUPPORT_ABILITY),
            KH2Item(412,"MP Rage",itemType.SUPPORT_ABILITY),
            KH2Item(413,"MP Haste",itemType.SUPPORT_ABILITY),
            KH2Item(413,"MP Haste",itemType.SUPPORT_ABILITY),
            KH2Item(421,"MP Hastera",itemType.SUPPORT_ABILITY),
            KH2Item(421,"MP Hastera",itemType.SUPPORT_ABILITY),
            KH2Item(422,"MP Hastega",itemType.SUPPORT_ABILITY),
            KH2Item(414,"Defender",itemType.SUPPORT_ABILITY),
            KH2Item(414,"Defender",itemType.SUPPORT_ABILITY),
            KH2Item(542,"Damage Control",itemType.SUPPORT_ABILITY),
            KH2Item(542,"Damage Control",itemType.SUPPORT_ABILITY),
            KH2Item(415,"Second Chance",itemType.SUPPORT_ABILITY),
            KH2Item(416,"Once More",itemType.SUPPORT_ABILITY),
            KH2Item(404,"No Experience",itemType.SUPPORT_ABILITY),
            KH2Item(404,"No Experience",itemType.SUPPORT_ABILITY),
            KH2Item(541,"Light & Darkness",itemType.SUPPORT_ABILITY),
        ]

    @staticmethod
    def getActionAbilityList():
        return [
            KH2Item(82, "Guard", itemType.ACTION_ABILITY),
            KH2Item(137, "Upper Slash", itemType.ACTION_ABILITY),
            KH2Item(271, "Horizontal Slash", itemType.ACTION_ABILITY),
            KH2Item(267, "Finishing Leap", itemType.ACTION_ABILITY),
            KH2Item(273, "Relatliating Slash", itemType.ACTION_ABILITY),
            KH2Item(262, "Slapshot", itemType.ACTION_ABILITY),
            KH2Item(263, "Dodge Slash", itemType.ACTION_ABILITY),
            KH2Item(559, "Flash Step", itemType.ACTION_ABILITY),
            KH2Item(264, "Slide Dash", itemType.ACTION_ABILITY),
            KH2Item(562, "Vicinity Break", itemType.ACTION_ABILITY),
            KH2Item(265, "Guard Break", itemType.ACTION_ABILITY),
            KH2Item(266, "Explosion", itemType.ACTION_ABILITY),
            KH2Item(269, "Aerial Sweep", itemType.ACTION_ABILITY),
            KH2Item(560, "Aerial Dive", itemType.ACTION_ABILITY),
            KH2Item(270, "Aerial Spiral", itemType.ACTION_ABILITY),
            KH2Item(272, "Aerial Finish", itemType.ACTION_ABILITY),
            KH2Item(561, "Magnet Burst", itemType.ACTION_ABILITY),
            KH2Item(268, "Counterguard", itemType.ACTION_ABILITY),
            KH2Item(385, "Auto Valor", itemType.ACTION_ABILITY),
            KH2Item(386, "Auto Wisdom", itemType.ACTION_ABILITY),
            KH2Item(387, "Auto Master", itemType.ACTION_ABILITY),
            KH2Item(388, "Auto Final", itemType.ACTION_ABILITY),
            KH2Item(389, "Auto Summon", itemType.ACTION_ABILITY),
            KH2Item(568, "Auto Limit", itemType.ACTION_ABILITY),
            KH2Item(198, "Trinity Limit", itemType.ACTION_ABILITY),
        ]

    @staticmethod
    def getNullItem():
        return KH2Item(0,"", itemType.SYNTH)

    @staticmethod
    def getJunkList(betterJunk):
        if betterJunk:
            return [
                KH2Item(1, "Potion", itemType.ITEM),
                KH2Item(2, "Hi-Potion", itemType.ITEM),
                KH2Item(3, "Ether", itemType.ITEM),
                KH2Item(4, "Elixir", itemType.ITEM),
                KH2Item(5, "Mega-Potion", itemType.ITEM),
                KH2Item(6, "Mega-Ether", itemType.ITEM),
                KH2Item(7, "Mega-Elixir", itemType.ITEM),
                KH2Item(131, "Tent", itemType.ITEM),
                KH2Item(274, "Drive Recovery", itemType.ITEM),
                KH2Item(275, "High Drive Recovery", itemType.ITEM),
                KH2Item(276, "Power Boost", itemType.ITEM),
                KH2Item(277, "Magic Boost", itemType.ITEM),
                KH2Item(278, "Defense Boost", itemType.ITEM),
                KH2Item(279, "AP Boost", itemType.ITEM),
            ]
        return [
            KH2Item(317, "Blazing Shard", itemType.SYNTH),
            KH2Item(318, "Blazing Stone", itemType.SYNTH),
            KH2Item(319, "Blazing Gem", itemType.SYNTH),
            KH2Item(320, "Blazing Crystal", itemType.SYNTH),
            KH2Item(378, "Frost Shard", itemType.SYNTH),
            KH2Item(379, "Frost Stone", itemType.SYNTH),
            KH2Item(380, "Frost Gem", itemType.SYNTH),
            KH2Item(381, "Frost Crystal", itemType.SYNTH),
            KH2Item(325, "Lightning Shard", itemType.SYNTH),
            KH2Item(326, "Lightning Stone", itemType.SYNTH),
            KH2Item(327, "Lightning Gem", itemType.SYNTH),
            KH2Item(328, "Lightning Crystal", itemType.SYNTH),
            KH2Item(333, "Lucid Shard", itemType.SYNTH),
            KH2Item(334, "Lucid Stone", itemType.SYNTH),
            KH2Item(335, "Lucid Gem", itemType.SYNTH),
            KH2Item(336, "Lucid Crystal", itemType.SYNTH),
            KH2Item(329, "Power Shard", itemType.SYNTH),
            KH2Item(330, "Power Stone", itemType.SYNTH),
            KH2Item(331, "Power Gem", itemType.SYNTH),
            KH2Item(332, "Power Crystal", itemType.SYNTH),
            KH2Item(280, "Dark Shard", itemType.SYNTH),
            KH2Item(281, "Dark Stone", itemType.SYNTH),
            KH2Item(282, "Dark Gem", itemType.SYNTH),
            KH2Item(283, "Dark Crystal", itemType.SYNTH),
            KH2Item(337, "Dense Shard", itemType.SYNTH),
            KH2Item(338, "Dense Stone", itemType.SYNTH),
            KH2Item(339, "Dense Gem", itemType.SYNTH),
            KH2Item(340, "Dense Crystal", itemType.SYNTH),
            KH2Item(341, "Twilight Shard", itemType.SYNTH),
            KH2Item(342, "Twilight Stone", itemType.SYNTH),
            KH2Item(343, "Twilight Gem", itemType.SYNTH),
            KH2Item(344, "Twilight Crystal", itemType.SYNTH),
            KH2Item(345, "Mythril Shard", itemType.SYNTH),
            KH2Item(346, "Mythril Stone", itemType.SYNTH),
            KH2Item(347, "Mythril Gem", itemType.SYNTH),
            KH2Item(348, "Mythril Crystal", itemType.SYNTH),
            KH2Item(576, "Remembrance Shard", itemType.SYNTH),
            KH2Item(577, "Remembrance Stone", itemType.SYNTH),
            KH2Item(578, "Remembrance Gem", itemType.SYNTH),
            KH2Item(579, "Remembrance Crystal", itemType.SYNTH),
            KH2Item(580, "Tranquility Shard", itemType.SYNTH),
            KH2Item(581, "Tranquility Stone", itemType.SYNTH),
            KH2Item(582, "Tranquility Gem", itemType.SYNTH),
            KH2Item(583, "Tranquility Crystal", itemType.SYNTH),
            KH2Item(349, "Bright Shard", itemType.SYNTH),
            KH2Item(350, "Bright Stone", itemType.SYNTH),
            KH2Item(351, "Bright Gem", itemType.SYNTH),
            KH2Item(352, "Bright Crystal", itemType.SYNTH),
            KH2Item(353, "Energy Shard", itemType.SYNTH),
            KH2Item(354, "Energy Stone", itemType.SYNTH),
            KH2Item(355, "Energy Gem", itemType.SYNTH),
            KH2Item(356, "Energy Crystal", itemType.SYNTH),
            KH2Item(357, "Serenity Shard", itemType.SYNTH),
            KH2Item(358, "Serenity Stone", itemType.SYNTH),
            KH2Item(359, "Serenity Gem", itemType.SYNTH),
            KH2Item(360, "Serenity Crystal", itemType.SYNTH),
            KH2Item(584, "Lost Illusion", itemType.SYNTH),
            KH2Item(585, "Manifest Illusion", itemType.SYNTH),
            KH2Item(377, "Orichalcum", itemType.SYNTH),
            KH2Item(361, "Orichalcum+", itemType.SYNTH),
            KH2Item(1, "Potion", itemType.ITEM),
            KH2Item(2, "Hi-Potion", itemType.ITEM),
            KH2Item(3, "Ether", itemType.ITEM),
            KH2Item(4, "Elixir", itemType.ITEM),
            KH2Item(5, "Mega-Potion", itemType.ITEM),
            KH2Item(6, "Mega-Ether", itemType.ITEM),
            KH2Item(7, "Mega-Elixir", itemType.ITEM),
            KH2Item(131, "Tent", itemType.ITEM),
            KH2Item(274, "Drive Recovery", itemType.ITEM),
            KH2Item(275, "High Drive Recovery", itemType.ITEM),
            KH2Item(276, "Power Boost", itemType.ITEM),
            KH2Item(277, "Magic Boost", itemType.ITEM),
            KH2Item(278, "Defense Boost", itemType.ITEM),
            KH2Item(279, "AP Boost", itemType.ITEM),
        ]

    @staticmethod
    def getDonaldAbilityList():
        return [
            KH2Item(165, "Donald Fire", itemType.DONALD_ABILITY),
            KH2Item(166, "Donald Blizzard", itemType.DONALD_ABILITY),
            KH2Item(167, "Donald Thunder", itemType.DONALD_ABILITY),
            KH2Item(168, "Donald Cure", itemType.DONALD_ABILITY),
            KH2Item(199, "Fantasia", itemType.DONALD_ABILITY),
            KH2Item(200, "Flare Force", itemType.DONALD_ABILITY),
            KH2Item(412, "MP Rage", itemType.DONALD_ABILITY),
            KH2Item(406, "Jackpot", itemType.DONALD_ABILITY),
            KH2Item(407, "Lucky Lucky", itemType.DONALD_ABILITY),
            KH2Item(408, "Fire Boost", itemType.DONALD_ABILITY),
            KH2Item(409, "Blizzard Boost", itemType.DONALD_ABILITY),
            KH2Item(410, "Thunder Boost", itemType.DONALD_ABILITY),
            KH2Item(408, "Fire Boost", itemType.DONALD_ABILITY),
            KH2Item(409, "Blizzard Boost", itemType.DONALD_ABILITY),
            KH2Item(410, "Thunder Boost", itemType.DONALD_ABILITY),
            KH2Item(412, "MP Rage", itemType.DONALD_ABILITY),
            KH2Item(421, "MP Hastera", itemType.DONALD_ABILITY),
            KH2Item(417, "Auto Limit", itemType.DONALD_ABILITY),
            KH2Item(419, "Hyper Healing", itemType.DONALD_ABILITY),
            KH2Item(420, "Auto Healing", itemType.DONALD_ABILITY),
            KH2Item(422, "MP Hastega", itemType.DONALD_ABILITY),
            KH2Item(411, "Item Boost", itemType.DONALD_ABILITY),
            KH2Item(542, "Damage Control", itemType.DONALD_ABILITY),
            KH2Item(419, "Hyper Healing", itemType.DONALD_ABILITY),
            KH2Item(412, "MP Rage", itemType.DONALD_ABILITY),
            KH2Item(413, "MP Haste", itemType.DONALD_ABILITY),
            KH2Item(421, "MP Hastera", itemType.DONALD_ABILITY),
            KH2Item(422, "MP Hastega", itemType.DONALD_ABILITY),
            KH2Item(413, "MP Haste", itemType.DONALD_ABILITY),
            KH2Item(542, "Damage Control", itemType.DONALD_ABILITY),
            KH2Item(421, "MP Hastera", itemType.DONALD_ABILITY),
            KH2Item(405, "Draw", itemType.DONALD_ABILITY),
        ]

    def getGoofyAbilityList():
        return [
            KH2Item(423, "Goofy Tornado", itemType.GOOFY_ABILITY),
            KH2Item(425, "Goofy Turbo", itemType.GOOFY_ABILITY),
            KH2Item(429, "Goofy Bash", itemType.GOOFY_ABILITY),
            KH2Item(201, "Tornado Fusion", itemType.GOOFY_ABILITY),
            KH2Item(202, "Teamwork", itemType.GOOFY_ABILITY),
            KH2Item(405, "Draw", itemType.GOOFY_ABILITY),
            KH2Item(406, "Jackpot", itemType.GOOFY_ABILITY),
            KH2Item(407, "Lucky Lucky", itemType.GOOFY_ABILITY),
            KH2Item(411, "Item Boost", itemType.GOOFY_ABILITY),
            KH2Item(412, "MP Rage", itemType.GOOFY_ABILITY),
            KH2Item(414, "Defender", itemType.GOOFY_ABILITY),
            KH2Item(542, "Damage Control", itemType.GOOFY_ABILITY),
            KH2Item(417, "Auto Limit", itemType.GOOFY_ABILITY),
            KH2Item(415,"Second Chance",itemType.GOOFY_ABILITY),
            KH2Item(416,"Once More",itemType.GOOFY_ABILITY),
            KH2Item(418, "Auto Change", itemType.GOOFY_ABILITY),
            KH2Item(419, "Hyper Healing", itemType.GOOFY_ABILITY),
            KH2Item(420, "Auto Healing", itemType.GOOFY_ABILITY),
            KH2Item(414, "Defender", itemType.GOOFY_ABILITY),
            KH2Item(419, "Hyper Healing", itemType.GOOFY_ABILITY),
            KH2Item(413, "MP Haste", itemType.GOOFY_ABILITY),
            KH2Item(421, "MP Hastera", itemType.GOOFY_ABILITY),
            KH2Item(412, "MP Rage", itemType.GOOFY_ABILITY),
            KH2Item(422, "MP Hastega", itemType.GOOFY_ABILITY),
            KH2Item(411, "Item Boost", itemType.GOOFY_ABILITY),
            KH2Item(542, "Damage Control", itemType.GOOFY_ABILITY),
            KH2Item(596, "Protect", itemType.GOOFY_ABILITY),
            KH2Item(597, "Protera", itemType.GOOFY_ABILITY),
            KH2Item(598, "Protega", itemType.GOOFY_ABILITY),
            KH2Item(542, "Damage Control", itemType.GOOFY_ABILITY),
            KH2Item(596, "Protect", itemType.GOOFY_ABILITY),
            KH2Item(597, "Protera", itemType.GOOFY_ABILITY),
            KH2Item(598, "Protega", itemType.GOOFY_ABILITY),
        ]
