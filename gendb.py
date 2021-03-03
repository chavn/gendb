import npyscreen as nps
import sqlite3 as sql


####################################
# Database Integration
####################################

class DatabaseHandler(object):
    def __init__(self):
        self.db = None

    def close_db(self):
        self.db = None

    # Setup new database for setting
    def setup_database(self, title='', author='', genre='', overview=''):
        self.db = sql.connect(title + '.db')
        c = self.db.cursor()
        c.execute(
            'CREATE TABLE IF NOT EXISTS "setting" ( \
                "title" TEXT NOT NULL UNIQUE, \
                "author" TEXT, \
                "genre" TEXT, \
                "overview" TEXT \
            )'
        )
        c.execute(
            'CREATE TABLE IF NOT EXISTS "tropes" ( \
                "id" INTEGER NOT NULL UNIQUE, \
                "trope" TEXT NOT NULL, \
                "description" TEXT, \
                PRIMARY KEY("id" AUTOINCREMENT) \
            )'
        )
        c.execute(
            'CREATE TABLE IF NOT EXISTS "skills" ( \
                "id" INTEGER NOT NULL UNIQUE, \
                "skill" TEXT NOT NULL, \
                "category" TEXT, \
                "characteristic" TEXT, \
                "description" TEXT, \
                "should" TEXT, \
                "shouldnt" TEXT, \
                PRIMARY KEY("id" AUTOINCREMENT) \
            )'
        )
        c.execute(
            'CREATE TABLE IF NOT EXISTS "talents" ( \
                "id" INTEGER NOT NULL UNIQUE, \
                "talent" TEXT NOT NULL, \
                "tier" TEXT, \
                "activation" TEXT, \
                "ranked" TEXT, \
                "description" TEXT, \
                PRIMARY KEY("id" AUTOINCREMENT) \
            )'
        )
        c.execute(
            'CREATE TABLE IF NOT EXISTS "qualities" ( \
                "id" INTEGER NOT NULL UNIQUE, \
                "quality" TEXT NOT NULL, \
                "description" TEXT, \
                PRIMARY KEY("id" AUTOINCREMENT) \
            )'
        )
        c.execute(
            'CREATE TABLE IF NOT EXISTS "weapons" ( \
                "id" INTEGER NOT NULL UNIQUE, \
                "weapon" TEXT NOT NULL, \
                "category" TEXT, \
                "skill" TEXT, \
                "damage" TEXT, \
                "critical" TEXT, \
                "range" TEXT, \
                "encumbrance" TEXT, \
                "price" TEXT, \
                "rarity" TEXT, \
                "special" TEXT, \
                "description" TEXT, \
                PRIMARY KEY("id" AUTOINCREMENT) \
            )'
        )
        c.execute(
            'CREATE TABLE IF NOT EXISTS "attachments" ( \
                "id" INTEGER NOT NULL UNIQUE, \
                "attachment" TEXT NOT NULL, \
                "armor" BOOLEAN, \
                "hardpoints" TEXT, \
                "price" TEXT, \
                "rarity" TEXT, \
                "description" TEXT, \
                PRIMARY KEY("id" AUTOINCREMENT) \
            )'
        )
        c.execute(
            'CREATE TABLE IF NOT EXISTS "armor" ( \
                "id" INTEGER NOT NULL UNIQUE, \
                "armor" TEXT NOT NULL, \
                "category" TEXT, \
                "defense" TEXT, \
                "soak" TEXT, \
                "encumbrance" TEXT, \
                "price" TEXT, \
                "rarity" TEXT, \
                "description" TEXT, \
                PRIMARY KEY("id" AUTOINCREMENT) \
            )'
        )
        c.execute(
            'CREATE TABLE IF NOT EXISTS "gear" ( \
                "id" INTEGER NOT NULL UNIQUE, \
                "gear" TEXT NOT NULL, \
                "category" TEXT, \
                "encumbrance" TEXT, \
                "price" TEXT, \
                "rarity" TEXT, \
                "description" TEXT, \
                PRIMARY KEY("id" AUTOINCREMENT) \
            )'
        )
        c.execute(
            'INSERT INTO setting(title, author, genre, overview) \
            VALUES(?,?,?,?)', (title, author, genre, overview)
        )
        self.db.commit()
        c.close()

####################################
# Custom Widgets
####################################

class InputBox(nps.BoxTitle):
    _contained_widget = nps.MultiLineEdit


class MenuSelect(nps.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(MenuSelect, self).__init__(*args, **keywords)
        self.menu_actions = {}

    def actionHighlighted(self, act_on_this, key_press):
        if act_on_this in self.menu_actions:
            self.parent.parentApp.switchForm(self.menu_actions[act_on_this])
        elif act_on_this == 'BACK':
            self.parent.parentApp.switchFormPrevious()
        elif act_on_this == 'EXIT':
            self.parent.parentApp.switchForm(None)
        elif act_on_this == 'CLOSE':
            self.parent.parentApp.db_handler.close_db()
            self.parent.parentApp.switchForm('MAIN')

####################################
# New Setting Form
####################################

class NewSetting(nps.FormBaseNewWithMenus):
    def create(self):
        self.name = 'GENESYS DATABASE - NEW SETTING'

        self.menu = self.new_menu()
        self.menu.addItem(text='CREATE', onSelect=self.create_setting)
        self.menu.addItem(text='CANCEL', onSelect=self.cancel)

        self.setting = self.add(nps.TitleText, name='TITLE')
        self.author = self.add(nps.TitleText, name='AUTHOR')
        self.genre = self.add(nps.TitleText, name='MAIN GENRE')
        self.overview = self.add(InputBox, name='OVERVIEW')

    def create_setting(self):
        self.parentApp.dbhandler.setup_database(
            title = self.setting.value,
            author = self.author.value,
            genre = self.genre.value,
            overview = self.overview.value
        )
        self.parentApp.switchForm('SETTINGMENU')

    def cancel(self):
        self.parentApp.switchFormPrevious()

####################################
# Create Talent Form
####################################

class CreateTalent(nps.FormBaseNewWithMenus):
    def create(self):
        self.name = 'GENESYS DATABASE - CREATE - TALENT'

        self.menu = self.new_menu()
        self.menu.addItem(text='SAVE', shortcut='^S')
    
        self.tal = self.add(nps.TitleText, name='TALENT')
        self.tier = self.add(nps.TitleText, name='TIER')
        self.act = self.add(nps.TitleText, name='ACTIVATION')
        self.rank = self.add(nps.Checkbox, name='RANKED')
        self.desc = self.add(InputBox, name='DESCRIPTION')

####################################
# Create Skill Form
####################################

class CreateSkill(nps.FormBaseNewWithMenus):
    def create(self):
        self.name = 'GENESYS DATABASE - CREATE - SKILL'

        self.skill = self.add(nps.TitleText, name='SKILL', begin_entry_at=17)
        self.cat = self.add(nps.TitleText, name='CATEGORY', begin_entry_at=17)
        self.char = self.add(nps.TitleText, name='CHARACTERISTIC',
            begin_entry_at=17)
        self.desc = self.add(InputBox, name='DESCRIPTION', max_height=7)
        self.dos = self.add(InputBox, name='SHOULD USE IF...', max_height=6)
        self.dont = self.add(InputBox, name='SHOULD NOT USE IF...', 
            max_height=6)

####################################
# Create Gear/Item Form
####################################

class CreateGear(nps.FormBaseNewWithMenus):
    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
        self.name = 'GENESYS DATABASE - CREATE - GEAR'

        self.type = self.add(nps.TitleText, name='TYPE')
        self.cat = self.add(nps.TitleText, name='CATEGORY')
        self.encum = self.add(nps.TitleText, name='ENCUMBRANCE')
        self.price = self.add(nps.TitleText, name='PRICE')
        self.rarity = self.add(nps.TitleText, name='RARITY')
        self.desc = self.add(InputBox, name='DESCRIPTION')

####################################
# Create Armor Form
####################################

class CreateArmor(nps.FormBaseNewWithMenus):
    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
        self.name = 'GENESYS DATABASE - CREATE - ARMOR'

        self.type = self.add(nps.TitleText, name='TYPE')
        self.cat = self.add(nps.TitleText, name='CATEGORY')
        self.defen = self.add(nps.TitleText, name='DEFENSE')
        self.soak = self.add(nps.TitleText, name='SOAK')
        self.encum = self.add(nps.TitleText, name='ENCUMBRANCE')
        self.price = self.add(nps.TitleText, name='PRICE')
        self.rarity = self.add(nps.TitleText, name='RARITY')
        self.desc = self.add(InputBox, name='DESCRIPTION')

####################################
# Create Weapon Form
####################################

class CreateWeapon(nps.FormBaseNewWithMenus):
    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
        self.name = 'GENESYS DATABASE - CREATE - WEAPON'

        self.type = self.add(nps.TitleText, name='NAME')
        self.cat = self.add(nps.TitleText, name='CATEGORY')
        self.skill = self.add(nps.TitleText, name='SKILL')
        self.dam = self.add(nps.TitleText, name='DAMAGE')
        self.crit = self.add(nps.TitleText, name='CRITICAL')
        self.range = self.add(nps.TitleText, name='RANGE')
        self.encum = self.add(nps.TitleText, name='ENCUMBRANCE')
        self.price = self.add(nps.TitleText, name='PRICE')
        self.rarity = self.add(nps.TitleText, name='RARITY')
        self.special = self.add(nps.TitleText, name='SPECIAL')
        self.desc = self.add(InputBox, name='DESCRIPTION')

####################################
# Create Armor Attachment Form
####################################

class CreateArmorAttachment(nps.FormBaseNewWithMenus):
    def create(self):
        self.name = 'GENESYS DATABASE - CREATE - ARMOR ATTACHMENT'
            
        self.attach = self.add(nps.TitleText, name='ATTACHMENT')
        self.hp = self.add(nps.TitleText, name='HARDPOINTS')
        self.price = self.add(nps.TitleText, name='PRICE')
        self.rarity = self.add(nps.TitleText, name='RARITY')
        self.desc = self.add(InputBox, name='DESCRIPTION')

####################################
# Create Weapon Attachment Form
####################################

class CreateWeaponAttachment(nps.FormBaseNewWithMenus):
    def create(self):
        self.name = 'GENESYS DATABASE - CREATE - WEAPON ATTACHMENT'

        self.attach = self.add(nps.TitleText, name='ATTACHMENT')
        self.hp = self.add(nps.TitleText, name='HARDPOINTS')
        self.price = self.add(nps.TitleText, name='PRICE')
        self.rarity = self.add(nps.TitleText, name='RARITY')
        self.desc = self.add(InputBox, name='DESCRIPTION')

####################################
# Main Menu Form
####################################

class MainMenu(nps.FormBaseNew):
    def create(self):
        self.name = 'GENESYS DATABASE'

        self.selector = self.add(MenuSelect)
        self.selector.values = ('NEW SETTING', 'OPEN SETTING', 'EXIT')
        self.selector.menu_actions = {
            'NEW SETTING': 'NEWSETTING',
            #'OPEN SETTING': 'OPENSETTING'
        }


####################################
# Setting Menu Form
####################################

class SettingMenu(nps.FormBaseNew):
    def create(self):
        self.name = 'GENESYS DATABASE - SETTING MENU'

        self.selector = self.add(MenuSelect)
        self.selector.values = ('CREATE', 'BROWSE', 'CLOSE')
        self.selector.menu_actions = {
            'CREATE': 'CREATE',
            'BROWSE': 'SEARCH'
        }


####################################
# Create Entry Menu Form
####################################

class CreateMenu(nps.FormBaseNew):
    def create(self):
        self.name = 'GENESYS DATABASE - CREATE'
        
        self.menu = self.add(MenuSelect)
        self.menu.values = (
            'TROPE', 'TONE', 'ARCHETYPE/SPECIES', 'CAREER',
            'FACTION/ORGANIZATION',
            'HEROIC ABILITY', 'SKILL', 'TALENT', 'WEAPON', 
            'WEAPON ATTACHMENT', 'ARMOR', 'ARMOR ATTACHMENT', 
            'GEAR', 'BACK' 
        )

        self.menu.menu_actions = {
            'SKILL': 'CREATE_SKILL',
            'TALENT': 'CREATE_TALENT',
            'WEAPON': 'CREATE_WEAPON',
            'WEAPON ATTACHMENT': 'CREATE_WEAPATT',
            'ARMOR': 'CREATE_ARMOR',
            'ARMOR ATTACHMENT': 'CREATE_ARMATT',
            'GEAR': 'CREATE_GEAR'
        }

####################################
# Search Entry Menu Form - To Edit
####################################

class SearchMenu(nps.FormBaseNew):
    def create(self):
        self.name = 'GENESYS DATABASE - SEARCH'

####################################
# App
####################################

class GenDB(nps.NPSAppManaged):
    def onStart(self):
        self.dbhandler = DatabaseHandler()
        self.addForm('MAIN', MainMenu)
        self.addForm('NEWSETTING', NewSetting)
        self.addForm('SETTINGMENU', SettingMenu)
        self.addForm('CREATE', CreateMenu)
        #self.addForm('SEARCH', SearchMenu)
        self.addForm('CREATE_SKILL', CreateSkill)
        self.addForm('CREATE_TALENT', CreateTalent)
        self.addForm('CREATE_WEAPON', CreateWeapon)
        self.addForm('CREATE_WEAPATT', CreateWeaponAttachment)
        self.addForm('CREATE_ARMOR', CreateArmor)
        self.addForm('CREATE_ARMATT', CreateArmorAttachment)
        self.addForm('CREATE_GEAR', CreateGear)

####################################
# Main Function
####################################

if __name__ == '__main__':
    App = GenDB().run()        
