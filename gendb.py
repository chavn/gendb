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

	def open_db(self, path):
		try:
		    self.db = sql.connect(path)
		except sql.Error:
			return 1
		else:
			return 0

	# Setup new database for setting
	def setup_database(self, path, name, author, genre, overview):
		try:
			self.db = sql.connect(path + name + '.db')
			c = self.db.cursor()
			c.execute(
				'CREATE TABLE IF NOT EXISTS "setting" ( \
					"name" TEXT NOT NULL UNIQUE, \
					"author" TEXT, \
					"genre" TEXT, \
					"overview" TEXT \
				)'
			)
			c.execute(
				'CREATE TABLE IF NOT EXISTS "tropes" ( \
					"id" INTEGER NOT NULL UNIQUE, \
					"name" TEXT NOT NULL, \
					"description" TEXT, \
					PRIMARY KEY("id" AUTOINCREMENT) \
				)'
			)
			c.execute(
				'CREATE TABLE IF NOT EXISTS "tones" ( \
		        	"id" INTEGER NOT NULL UNIQUE, \
		        	"name" TEXT NOT NULL, \
		        	"description" TEXT, \
		        	PRIMARY KEY("id" AUTOINCREMENT) \
				)'
			)
			c.execute(
				'CREATE TABLE IF NOT EXISTS "skills" ( \
					"id" INTEGER NOT NULL UNIQUE, \
					"name" TEXT NOT NULL, \
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
					"name" TEXT NOT NULL, \
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
					"name" TEXT NOT NULL, \
					"description" TEXT, \
					PRIMARY KEY("id" AUTOINCREMENT) \
				)'
			)
			c.execute(
				'CREATE TABLE IF NOT EXISTS "weapons" ( \
					"id" INTEGER NOT NULL UNIQUE, \
					"name" TEXT NOT NULL, \
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
					"name" TEXT NOT NULL, \
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
					"name" TEXT NOT NULL, \
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
					"name" TEXT NOT NULL, \
					"category" TEXT, \
					"encumbrance" TEXT, \
					"price" TEXT, \
					"rarity" TEXT, \
					"description" TEXT, \
					PRIMARY KEY("id" AUTOINCREMENT) \
				)'
			)
			c.execute(
				'INSERT INTO setting(name, author, genre, overview) \
				VALUES(?,?,?,?)', (name, author, genre, overview)
			)
			self.db.commit()
			c.close()
		except sql.Error:
			return 1
		else:
			return 0

	def add_trope(self, data):
		c = self.db.cursor()
		c.execute(
			'INSERT INTO tropes(name, description) \
			VALUES(?,?)', (data['name'], data['description'])
		)
		self.db.commit()
		c.close()

	def update_trope(self, data):
		pass
		
	def add_tone(self, data):
		c = self.db.cursor()
		c.execute(
			'INSERT INTO tones(name, description) \
			VALUES(?,?)', (data['name'], data['description'])
		)
		self.db.commit()
		c.close()

	def add_attachment(self, data):
		c = self.db.cursor()
		c.execute(
			'INSERT INTO attachments(name, armor, hardpoints, \
			price, rarity, description) VALUES(?,?,?,?,?,?)', \
			(data['name'], data['armor'], data['hardpoints'], data['price'],
			data['rarity'], data['description'])
		)
		self.db.commit()
		c.close()

	def update_attachment(self, data):
		pass

	def add_quality(self, data):
		c = self.db.cursor()
		c.execute(
			'INSERT INTO qualities(name, description) \
			VALUES(?,?)', (data['name'], data['description'])
		)
		self.db.commit()
		c.close()

	def update_quality(self, data):
		pass

	def add_skill(self, data):
		c = self.db.cursor()
		c.execute(
			'INSERT INTO skills(name, category, characteristic, description, \
			should, shouldnt) VALUES(?,?,?,?,?,?)',
			(data['name'], data['category'], data['characteristic'],
			data['description'], data['should'], data['shouldnt'])
		)
		self.db.commit()
		c.close()

	def update_skill(self, data):
		pass

	def add_trope(self, data):
		c = self.db.cursor()
		c.execute(
			'INSERT INTO tropes(name, description) VALUES(?,?)',
			(data['name'], data['description'])
		)
		self.db.commit()
		c.close()

	def update_trope(self, data):
		pass

	def add_weapon(self, data):
		c = self.db.cursor()
		c.execute(
			'INSERT INTO weapons(name, category, skill, damage, critical, \
			range, encumbrance, price, rarity, special, description) \
			VALUES(?,?,?,?,?,?,?,?,?,?,?)',
			(data['name'], data['category'], data['skill'], data['damage'],
			data['critical'], data['range'], data['encumbrance'], data['price'],
			data['rarity'], data['special'], data['description'])
		)
		self.db.commit()
		c.close()

	def update_weapon(self, data):
		pass

	def add_armor(self, data):
		c = self.db.cursor()
		c.execute(
			'INSERT INTO armor(name, category,  defense, soak, encumbrance, \
			price, rarity, description) VALUES(?,?,?,?,?,?,?,?)',
			(data['name'], data['category'], data['defense'], data['soak'],
			data['encumbrance'], data['price'], data['rarity'],
			data['description'])
		)
		self.db.commit()
		c.close()

	def update_armor(self, data):
		pass

	def add_gear(self, data):
		c = self.db.cursor()
		c.execute(
			'INSERT INTO gear(name, category, encumbrance, price, rarity, \
			description) VALUES(?,?,?,?,?,?)', (data['name'], data['category'],
			data['encumbrance'], data['price'], data['rarity'],
			data['description'])
		)
		self.db.commit()
		c.close()

	def update_gear(self, data):
		pass

	def remove_entry(self, table, id):
		pass

####################################
# Custom Widgets
####################################

# Titled MultiLineEdit
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
			self.parent.parentApp.dbhandler.close_db()
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

		self.path = self.add(nps.TitleFilename, name='PATH')
		self.setting = self.add(nps.TitleText, name='TITLE')
		self.author = self.add(nps.TitleText, name='AUTHOR')
		self.genre = self.add(nps.TitleText, name='MAIN GENRE')
		self.overview = self.add(InputBox, name='OVERVIEW')

	def create_setting(self):
		res = self.parentApp.dbhandler.setup_database(
			self.path.value,
			self.setting.value,
			self.author.value,
			self.genre.value,
			self.overview.value
		)
		if res < 1:
			self.parentApp.switchForm('SETTINGMENU')

	def cancel(self):
		self.setting.value = ''
		self.author.value = ''
		self.genre.value = ''
		self.overview.value = ''
		self.parentApp.switchFormPrevious()

####################################
# Create Talent Form
####################################

class CreateTalent(nps.FormBaseNewWithMenus):
	def create(self):
		self.name = 'GENESYS DATABASE - CREATE - TALENT'

		self.menu = self.new_menu()
		self.menu.addItem(text='CREATE', onSelect=self.create_talent)
		self.menu.addItem(text='CANCEL', onSelect=self.cancel)
	
		self.tal = self.add(nps.TitleText, name='TALENT')
		self.tier = self.add(nps.TitleText, name='TIER')
		self.act = self.add(nps.TitleText, name='ACTIVATION')
		self.rank = self.add(nps.Checkbox, name='RANKED')
		self.desc = self.add(InputBox, name='DESCRIPTION')
	
	def create_talent(self):
		data = {
			'name': self.tal.value,
			'tier': self.tier.value,
			'activation': self.tier.value,
			'ranked': self.rank.value,
			'description': self.desc.value
		}
		self.parentApp.dbhandler.add_talent(data)
		self.cancel()
	
	def cancel(self):
		self.tal.value = ''
		self.tier.value = ''
		self.act.value = ''
		self.rank.value = False
		self.desc.value = ''
		self.parentApp.switchFormPrevious()

####################################
# Create Skill Form
####################################

class CreateSkill(nps.FormBaseNewWithMenus):
	def create(self):
		self.name = 'GENESYS DATABASE - CREATE - SKILL'

		self.menu = self.new_menu()
		self.menu.addItem(text='CREATE', onSelect=self.create_skill)
		self.menu.addItem(text='CANCEL', onSelect=self.cancel)

		self.skill = self.add(nps.TitleText, name='SKILL', begin_entry_at=17)
		self.cat = self.add(nps.TitleText, name='CATEGORY', begin_entry_at=17)
		self.char = self.add(nps.TitleText, name='CHARACTERISTIC',
			begin_entry_at=17)
		self.desc = self.add(InputBox, name='DESCRIPTION', max_height=7)
		self.dos = self.add(InputBox, name='SHOULD USE IF...', max_height=6)
		self.dont = self.add(InputBox, name='SHOULD NOT USE IF...',
			max_height=6)
			
	def create_skill(self):
		data = {
			'name': self.skill.value,
			'category': self.cat.value,
			'characteristic': self.char.value,
			'description': self.desc.value,
			'should': self.dos.value,
			'shouldnt': self.dont.value
		}
		self.parentApp.dbhandler.add_skill(data)
		self.cancel()

	def cancel(self):
		self.skill.value = ''
		self.cat.value = ''
		self.char.value = ''
		self.desc.value = ''
		self.dos.value = ''
		self.dont.value = ''
		self.parentApp.switchFormPrevious()

####################################
# Create Gear/Item Form
####################################

class CreateGear(nps.FormBaseNewWithMenus):
	def create(self):
		self.name = 'GENESYS DATABASE - CREATE - GEAR'

		self.menu = self.new_menu()
		self.menu.addItem(text='CREATE', onSelect=self.create_gear)
		self.menu.addItem(text='CANCEL', onSelect=self.cancel)

		self.type = self.add(nps.TitleText, name='TYPE')
		self.cat = self.add(nps.TitleText, name='CATEGORY')
		self.encum = self.add(nps.TitleText, name='ENCUMBRANCE')
		self.price = self.add(nps.TitleText, name='PRICE')
		self.rarity = self.add(nps.TitleText, name='RARITY')
		self.desc = self.add(InputBox, name='DESCRIPTION')
		
	def create_gear(self):
		data = {
			'name': self.type.value,
			'category': self.cat.value,
			'encumbrance': self.encum.value,
			'price': self.price.value,
			'rarity': self.rarity.value,
			'description': self.desc.value
		}
		self.parentApp.dbhandler.add_gear(data)
		self.cancel()

	def cancel(self):
		self.type.value = ''
		self.cat.value = ''
		self.encum.value = ''
		self.price.value = ''
		self.rarity.value = ''
		self.desc.value = ''
		self.parentApp.switchFormPrevious()

####################################
# Create Armor Form
####################################

class CreateArmor(nps.FormBaseNewWithMenus):
	def create(self):
		self.name = 'GENESYS DATABASE - CREATE - ARMOR'

		self.menu = self.new_menu()
		self.menu.addItem(text='CREATE', onSelect=self.create_armor)
		self.menu.addItem(text='CANCEL', onSelect=self.cancel)

		self.type = self.add(nps.TitleText, name='TYPE')
		self.cat = self.add(nps.TitleText, name='CATEGORY')
		self.defen = self.add(nps.TitleText, name='DEFENSE')
		self.soak = self.add(nps.TitleText, name='SOAK')
		self.encum = self.add(nps.TitleText, name='ENCUMBRANCE')
		self.price = self.add(nps.TitleText, name='PRICE')
		self.rarity = self.add(nps.TitleText, name='RARITY')
		self.desc = self.add(InputBox, name='DESCRIPTION')
		
	def create_armor(self):
		data = {
			'name': self.type.value,
			'category': self.cat.value,
			'defense': self.defen.value,
			'soak': self.soak.value,
			'encumbrance': self.encum.value,
			'price': self.price.value,
			'rarity': self.rarity.value,
			'description': self.desc.value
		}
		self.parentApp.dbhandler.add_armor(data)
		self.cancel()

	def cancel(self):
		self.type.value = ''
		self.cat.value = ''
		self.defen.value = ''
		self.soak.value = ''
		self.encum.value = ''
		self.price.value = ''
		self.rarity.value = ''
		self.desc.value = ''
		self.parentApp.switchFormPrevious()

####################################
# Create Weapon Form
####################################

class CreateWeapon(nps.FormBaseNewWithMenus):
	def create(self):
		self.name = 'GENESYS DATABASE - CREATE - WEAPON'

		self.menu = self.new_menu()
		self.menu.addItem(text='CREATE', onSelect=self.create_weapon)
		self.menu.addItem(text='CANCEL', onSelect=self.cancel)

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
		
	def create_weapon(self):
		data = {
			'name': self.type.value,
			'category': self.cat.value,
			'skill': self.skill.value,
			'damage': self.dam.value,
			'critical': self.crit.value,
			'range': self.range.value,
			'encumbrance': self.encum.value,
			'price': self.price.value,
			'rarity': self.rarity.value,
			'special': self.special.value,
			'description': self.desc.value
		}
		self.parentApp.dbhandler.add_weapon(data)
		self.cancel()

	def cancel(self):
		self.type.value = ''
		self.cat.value = ''
		self.skill.value = ''
		self.dam.value = ''
		self.crit.value = ''
		self.range.value = ''
		self.encum.value = ''
		self.price.value = ''
		self.rarity.value = ''
		self.special.value = ''
		self.desc.value = ''
		self.parentApp.switchFormPrevious()

####################################
# Create Armor Attachment Form
####################################

class CreateArmorAttachment(nps.FormBaseNewWithMenus):
	def create(self):
		self.name = 'GENESYS DATABASE - CREATE - ARMOR ATTACHMENT'

		self.menu = self.new_menu()
		self.menu.addItem(text='CREATE', onSelect=self.create_attachment)
		self.menu.addItem(text='CANCEL', onSelect=self.cancel)
			
		self.attach = self.add(nps.TitleText, name='ATTACHMENT')
		self.hp = self.add(nps.TitleText, name='HARDPOINTS')
		self.price = self.add(nps.TitleText, name='PRICE')
		self.rarity = self.add(nps.TitleText, name='RARITY')
		self.desc = self.add(InputBox, name='DESCRIPTION')
		
	def create_attachment(self):
		data = {
			'name': self.attach.value,
			'hardpoints': self.hp.value,
			'price': self.price.value,
			'rarity': self.rarity.value,
			'description': self.desc.value,
			'armor': True
		}
		self.parentApp.dbhandler.add_attachment(data)
		self.cancel()

	def cancel(self):
		self.attach.value = ''
		self.hp.value = ''
		self.price.value = ''
		self.rarity.value = ''
		self.desc.value = ''
		self.parentApp.switchFormPrevious()

####################################
# Create Weapon Attachment Form
####################################

class CreateWeaponAttachment(nps.FormBaseNewWithMenus):
	def create(self):
		self.name = 'GENESYS DATABASE - CREATE - WEAPON ATTACHMENT'

		self.menu = self.new_menu()
		self.menu.addItem(text='CREATE', onSelect=self.create_weapon_attachment)
		self.menu.addItem(text='CANCEL', onSelect=self.cancel)

		self.attach = self.add(nps.TitleText, name='ATTACHMENT')
		self.hp = self.add(nps.TitleText, name='HARDPOINTS')
		self.price = self.add(nps.TitleText, name='PRICE')
		self.rarity = self.add(nps.TitleText, name='RARITY')
		self.desc = self.add(InputBox, name='DESCRIPTION')

	def create_weapon_attachment(self):
		data = {
			'name': self.attach.value,
			'hardpoints': self.hp.value,
			'price': self.price.value,
			'rarity': self.rarity.value,
			'description': self.desc.value,
			'armor': False
		}
		self.parentApp.dbhandler.add_attachment(data)
		self.cancel()

	def cancel(self):
		self.attach.value = ''
		self.hp.value = ''
		self.price.value = ''
		self.rarity.value = ''
		self.desc.value = ''
		self.parentApp.switchFormPrevious()
		
####################################
# Create Trope Form
####################################
class CreateTrope(nps.FormBaseNewWithMenus):
	def create(self):
		self.name = 'GENESYS DATABASE - CREATE - TROPE'
		
		self.trope = self.add(nps.TitleText, name='TROPE')
		self.desc = self.add(InputBox, name='DESCRIPTION')
		
	def create_trope(self):
		data = {
			'name': self.trope.value,
			'description': self.desc.value
		}
		self.parentApp.dbhandler.add_trope(data)
		self.cancel()
		
	def cancel(self):
		self.trope.value = ''
		self.desc.value = ''
		self.parentApp.switchFormPrevious()

####################################
# Create Tone Form
####################################
class CreateTone(nps.FormBaseNewWithMenus):
	def create(self):
		self.name = 'GENESYS DATABASE - CREATE - TONE'
		
		self.tone = self.add(nps.TitleText, name='TONE')
		self.desc = self.add(InputBox, name='DESCRIPTION')
		
	def create_trope(self):
		data = {
			'name': self.tone.value,
			'description': self.desc.value
		}
		self.parentApp.dbhandler.add_tone(data)
		self.cancel()
		
	def cancel(self):
		self.tone.value = ''
		self.desc.value = ''
		self.parentApp.switchFormPrevious()

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
			'OPEN SETTING': 'OPENSETTING'
		}


####################################
# Open Setting Form
####################################

class OpenSetting(nps.ActionFormV2):
	def create(self):
		self.name = 'GENESYS DATABASE - OPEN SETTING'

		self.path = self.add(nps.TitleFilename, name='Path (*.db)')

	def on_ok(self):
		self.parentApp.dbhandler.open_db(self.path.value)
		self.parentApp.switchForm('SETTINGMENU')

	def on_cancel(self):
		self.path.value = ''
		self.parentApp.switchFormPrevious()

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
# Compile Menu Form
####################################

class CompileMenu(nps.FormBaseNewWithMenus):
	def create(self):
		self.name = 'GENESYS DATABASE - COMPILE'

####################################
# App
####################################

class GenDB(nps.NPSAppManaged):
	def onStart(self):
		self.dbhandler = DatabaseHandler()
		self.addForm('MAIN', MainMenu)
		self.addForm('NEWSETTING', NewSetting)
		self.addForm('OPENSETTING', OpenSetting)
		self.addForm('SETTINGMENU', SettingMenu)
		self.addForm('CREATE', CreateMenu)
		#self.addForm('SEARCH', SearchMenu)
		#self.addForm('COMPILE', CompileMenu)
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
