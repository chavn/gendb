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

	### TROPE RECORDS
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
		
	def delete_trope(self, id):
		pass
		
	def get_all_tropes(self):
		pass
		
	### TONE RECORDS
	def add_tone(self, data):
		c = self.db.cursor()
		c.execute(
			'INSERT INTO tones(name, description) \
			VALUES(?,?)', (data['name'], data['description'])
		)
		self.db.commit()
		c.close()
		
	def update_tone(self, id, data):
		pass
		
	def delete_tone(self, id):
		pass
		
	def get_all_tones(self):
		pass

	### ATTACHMENT RECORDS
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

	def update_attachment(self, id, data):
		pass
		
	def get_all_attachments(self):
		pass
		
	def delete_attachment(self, id):
		pass

	### QUALITY RECORDS
	def add_quality(self, data):
		c = self.db.cursor()
		c.execute(
			'INSERT INTO qualities(name, description) \
			VALUES(?,?)', (data['name'], data['description'])
		)
		self.db.commit()
		c.close()

	def update_quality(self, id, data):
		pass
		
	def delete_quality(self, id):
		pass
		
	def get_all_qualities(self):
		pass

	### SKILL RECORDS
	def add_skill(self, data):
		c = self.db.cursor()
		c.execute(
			'INSERT INTO skills(name, category, characteristic, description, \
			should, shouldnt) VALUES(?,?,?,?,?,?)',
			(data['name'], data['category'], data['characteristic'],
			data['description'], data['should use if...'],
			data['should not use if...'])
		)
		self.db.commit()
		c.close()

	def update_skill(self, id, data):
		pass
		
	def get_all_skills(self):
		c = self.db.cursor()
		c.execute('SELECT * FROM skills')
		skills = c.fetchall()
		c.close()
		return skills
		
	def delete_skill(self, id):
		c = self.db.cursor()
		c.execute('DELETE FROM skills WHERE id=?', (id,))
		self.db.commit()
		c.close()

	### TALENT RECORDS
	def add_talent(self, data):
		c = self.db.cursor()
		c.execute(
			'INSERT INTO talents(name, description) VALUES(?,?)',
			(data['name'], data['description'])
		)
		self.db.commit()
		c.close()

	def update_talent(self, id, data):
		pass
		
	def delete_talent(self, id):
		c = self.db.cursor()
		c.execute('DELETE FROM talents WHERE id=?', (id,))
		self.db.commit()
		c.close()
		
	def get_all_talents(self):
		c = self.db.cursor()
		c.execute('SELECT * FROM talents')
		talents = c.fetchall()
		c.close()
		return talents

	### WEAPON RECORDS
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
		
	def get_all_weapons(self):
		c = self.db.cursor()
		c.execute('SELECT * FROM weapons')
		weapons = c.fetchall()
		c.close()
		return weapons
		
	def delete_weapon(self, id):
		c = self.db.cursor()
		c.execute('DELETE FROM weapons WHERE id=?', (id,))
		self.db.commit()
		c.close()

	### ARMOR RECORDS
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

	def update_armor(self, id, data):
		pass
		
	def get_all_armor(self):
		c = self.db.cursor()
		c.execute('SELECT * FROM armor')
		armor = c.fetchall()
		c.close()
		return armor
		
	def delete_armor(self, id):
		c = self.db.cursor()
		c.execute('DELETE FROM armor WHERE id=?', (id,))
		self.db.commit()
		c.close()

	### GEAR RECORDS
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
		
	def get_all_gear(self):
		c = self.db.cursor()
		c.execute('SELECT * FROM gear')
		gear = c.fetchall()
		c.close()
		return gear
		
	def delete_gear(self, id):
		c = self.db.cursor()
		c.execute('DELETE FROM gear WHERE id=?', (id,))
		self.db.commit()
		c.close()


####################################
# Custom Widgets
####################################

# Titled MultiLineEdit
class InputBox(nps.BoxTitle):
	_contained_widget = nps.MultiLineEdit


# Record list for browsing
class RecordList(nps.MultiLineAction):
	def __init__(self, *args, **keywords):
		super(RecordList, self).__init__(*args, **keywords)
		self.category = False
		
	def display_value(self, vl):
		if self.category:
			category_text = 'ID: %s \t NAME: %s \t CATEG.: %s'
			return category_text % (vl[0], vl[1], vl[2])
		else:
			text = 'ID: %s \t NAME: %s'
			return text % (vl[0], vl[1])
		
	def get_id(self):
		return int(self.values[self.cursor_line][0])
	
	
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
		elif act_on_this == 'CLOSE SETTING':
			self.parent.parentApp.dbhandler.close_db()
			self.parent.parentApp.switchForm('MAIN')

####################################
# New Setting Form
####################################

class NewSetting(nps.ActionFormV2):
	def create(self):
		self.name = 'GENESYS DATABASE - NEW SETTING'

		self.path = self.add(nps.TitleFilename, name='PATH')
		self.setting = self.add(nps.TitleText, name='TITLE')
		self.author = self.add(nps.TitleText, name='AUTHOR')
		self.genre = self.add(nps.TitleText, name='MAIN GENRE(S)')
		self.overview = self.add(InputBox, name='OVERVIEW')

	def on_ok(self):
		if self.setting.value == '':
			self.empty_title()
		else:
			res = self.parentApp.dbhandler.setup_database(
				self.path.value,
				self.setting.value,
				self.author.value,
				self.genre.value,
				self.overview.value
			)
			if res < 1:
				self.clear_items()
				self.parentApp.switchForm('SETTINGMENU')

	def on_cancel(self):
		self.clear_items()
		self.parentApp.switchFormPrevious()
		
	def clear_items(self):
		self.setting.value = ''
		self.path.value = ''
		self.author.value = ''
		self.genre.value = ''
		self.overview.value = ''
	
	def empty_title(self):
		message = 'The "TITLE" field requires input.'
		nps.notify_confirm(message, title='Title Required', editw=1)

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
		self.name = 'GENESYS DATABASE - SETTING BROWSER'
		
		self.menu = self.add(MenuSelect)
		self.menu.values = (
			'TROPES', 'TONES', '!ARCHETYPES/SPECIES', '!CAREERS',
			'!FACTIONS/ORGANIZATIONS',
			'!HEROIC ABILITIES', 'SKILLS', 'TALENTS', 'WEAPONS',
			'WEAPON ATTACHMENTS', 'ARMOR', 'ARMOR ATTACHMENTS',
			'GEAR', 'CLOSE SETTING'
		)

		self.menu.menu_actions = {
			'TROPES': 'BROWSE_TROPES',
			'TONES': 'BROWSE_TONES',
			'SKILLS': 'BROWSE_SKILLS',
			'TALENTS': 'BROWSE_TALENTS',
			'WEAPONS': 'BROWSE_WEAPONS',
			'WEAPON ATTACHMENTS': 'BROWSE_WEAPATTS',
			'ARMOR': 'BROWSE_ARMOR',
			'ARMOR ATTACHMENTS': 'BROWSE_ARMATTS',
			'GEAR': 'BROWSE_GEAR'
		}
		
####################################
# Browse Talents Form
####################################

class BrowseTalents(nps.FormBaseNewWithMenus):
	def beforeEditing(self):
		self.talents.values = self.parentApp.dbhandler.get_all_skills()

	def create(self):
		self.name = 'GENESYS DATABASE - BROWSE - TALENTS'
		
		self.menu = self.new_menu(name='TALENT MENU')
		self.menu.addItem(text='CREATE', onSelect=self.create_talent)
		self.menu.addItem(text='EDIT', onSelect=self.edit_talent)
		self.menu.addItem(text='DELETE', onSelect=self.delete_talent)
		self.menu.addItem(text='BACK', onSelect=self.back)
		
		self.talents = self.add(RecordList)
		self.talents.category = False
		
	def create_talent(self):
		self.talents.values = ()
		self.parentApp.switchForm('CREATE_TALENT')
	
	def delete_talent(self):
		self.parentApp.dbhandler.delete_talent(self.talents.get_id())
		self.talents.values = self.parentApp.dbhandler.get_all_skills()
		
	def edit_talent(self):
		data = self.talents.values[self.talents.cursor_line]
		form = self.parentApp.getForm('CREATE_TALENT')
		formFields = form.fields
		form.id = data[0]
		form.name = 'GENESYS DATABASE - EDIT - TALENT - ' + data[1]
		for i, field in enumerate(formFields):
			field.value = data[i + 1]
		
		self.parentApp.switchForm('CREATE_TALENT')
		
	def back(self):
		self.talents.values = ()
		self.parentApp.switchFormPrevious()

####################################
# Create Talent Form
####################################

class CreateTalent(nps.ActionFormV2):
	def create(self):
		self.standard_name = 'GENESYS DATABASE - CREATE - TALENT'
		self.name = self.standard_name
	
		self.id = ''
		self.fields = (
			self.add(nps.TitleText, name='TALENT'),
			self.add(nps.TitleText, name='TIER'),
			self.add(nps.TitleText, name='ACTIVATION'),
			self.add(nps.Checkbox, name='RANKED'),
			self.add(InputBox, name='DESCRIPTION')
		)
	
	def on_ok(self):
		if self.fields[0].value == '':
			self.empty_name()
		else:
			data = {}
			for field in self.fields:
				data[field.name.lower()] = field.value
			if self.id == '':
				self.parentApp.dbhandler.add_talent(data)
			else:
				self.parentApp.dbhandler.update_talent(self.id, data)
			self.clear_items()
			self.parentApp.switchFormPrevious()
	
	def on_cancel(self):
		self.clear_items()
		self.parentApp.switchFormPrevious()
		
	def clear_items(self):
		self.name = self.standard_name
		self.id = ''
		for field in self.fields:
			field.value = ''
		
	def empty_name(self):
		message = 'The "NAME" field requires input.'
		nps.notify_confirm(message, title='Title Required', editw=1)

####################################
# Browse Skills Form
####################################

class BrowseSkills(nps.FormBaseNewWithMenus):
	def beforeEditing(self):
		self.skill.values = self.parentApp.dbhandler.get_all_skills()

	def create(self):
		self.name = 'GENESYS DATABASE - BROWSE - SKILLS'
		
		self.menu = self.new_menu(name='SKILLS MENU')
		self.menu.addItem(text='CREATE', onSelect=self.create_skill)
		self.menu.addItem(text='EDIT', onSelect=self.edit_skill)
		self.menu.addItem(text='DELETE', onSelect=self.delete_skill)
		self.menu.addItem(text='BACK', onSelect=self.back)
		
		self.skill = self.add(RecordList)
		self.skill.category = True
		
	def create_skill(self):
		self.skill.values = ()
		self.parentApp.switchForm('CREATE_SKILL')
	
	def delete_skill(self):
		self.parentApp.dbhandler.delete_skill(self.skill.get_id())
		self.skill.values = self.parentApp.dbhandler.get_all_skills()
		
	def edit_skill(self):
		data = self.skill.values[self.skill.cursor_line]
		form = self.parentApp.getForm('CREATE_SKILL')
		formFields = form.fields
		form.id = data[0]
		form.name = 'GENESYS DATABASE - EDIT - SKILL - ' + data[1]
		for i, field in enumerate(formFields):
			field.value = data[i + 1]
		
		self.parentApp.switchForm('CREATE_SKILL')
		
	def back(self):
		self.skill.values = ()
		self.parentApp.switchFormPrevious()

####################################
# Create Skill Form
####################################

class CreateSkill(nps.ActionFormV2):
	def create(self):
		self.standard_name = 'GENESYS DATABASE - CREATE - SKILL'
		self.name = self.standard_name

		self.id = ''
		self.fields = (
			self.add(nps.TitleText, name='NAME', begin_entry_at=17),
			self.add(nps.TitleText, name='CATEGORY', begin_entry_at=17),
			self.add(nps.TitleText, name='CHARACTERISTIC', begin_entry_at=17),
			self.add(InputBox, name='DESCRIPTION', max_height=6),
			self.add(InputBox, name='SHOULD USE IF...', max_height=6),
			self.add(InputBox, name='SHOULD NOT USE IF...', max_height=6)
		)
			
	def on_ok(self):
		if self.fields[0].value == '':
			self.empty_name()
		else:
			data = {}
			for field in self.fields:
				data[field.name.lower()] = field.value
			if self.id == '':
				self.parentApp.dbhandler.add_skill(data)
			else:
				self.parentApp.dbhandler.update_skill(self.id, data)
			self.parentApp.switchFormPrevious()
			self.clear_items()

	def on_cancel(self):
		self.clear_items()
		self.parentApp.switchFormPrevious()
		
	def clear_items(self):
		self.name = self.standard_name
		self.id = ''
		for field in self.fields:
			field.value = ''
		
	def empty_name(self):
		message = 'The "NAME" field requires input.'
		nps.notify_confirm(message, title='Name Required', editw=1)

####################################
# Browse Gear/Items Form
####################################

class BrowseGear(nps.FormBaseNewWithMenus):
	def beforeEditing(self):
		self.gear.values = self.parentApp.dbhandler.get_all_gear()

	def create(self):
		self.name = 'GENESYS DATABASE - BROWSE - GEAR'
		
		self.menu = self.new_menu(name='GEAR MENU')
		self.menu.addItem(text='CREATE', onSelect=self.create_gear)
		self.menu.addItem(text='EDIT', onSelect=self.edit_gear)
		self.menu.addItem(text='DELETE', onSelect=self.delete_gear)
		self.menu.addItem(text='BACK', onSelect=self.back)
		
		self.gear = self.add(RecordList)
		self.gear.category = True
		
	def create_gear(self):
		self.gear.values = ()
		self.parentApp.switchForm('CREATE_GEAR')
	
	def delete_gear(self):
		self.parentApp.dbhandler.delete_gear(self.gear.get_id())
		self.gear.values = self.parentApp.dbhandler.get_all_gear()
		
	def edit_gear(self):
		data = self.gear.values[self.gear.cursor_line]
		form = self.parentApp.getForm('CREATE_GEAR')
		formFields = form.fields
		form.id = data[0]
		form.name = 'GENESYS DATABASE - EDIT - GEAR - ' + data[1]
		for i, field in enumerate(formFields):
			field.value = data[i + 1]
		
		self.parentApp.switchForm('CREATE_GEAR')
		
	def back(self):
		self.gear.values = ()
		self.parentApp.switchFormPrevious()

####################################
# Create Gear/Item Form
####################################

class CreateGear(nps.ActionFormV2):
	def create(self):
		self.standard_name = 'GENESYS DATABASE - CREATE - GEAR'
		self.name = self.standard_name

		self.id = ''
		self.fields = (
			self.add(nps.TitleText, name='NAME'),
			self.add(nps.TitleText, name='CATEGORY'),
			self.add(nps.TitleText, name='ENCUMBRANCE'),
			self.add(nps.TitleText, name='PRICE'),
			self.add(nps.TitleText, name='RARITY'),
			self.add(InputBox, name='DESCRIPTION')
		)
		
	def on_ok(self):
		if self.fields[0].value == '':
			self.empty_name()
		else:
			data = {}
			for field in self.fields:
				data[field.name.lower()] = field.value
			if self.id == '':
				self.parentApp.dbhandler.add_gear(data)
			else:
				self.parentApp.dbhandler.update_gear(self.id, data)
			self.clear_items()
			self.parentApp.switchFormPrevious()

	def on_cancel(self):
		self.clear_items()
		self.parentApp.switchFormPrevious()
		
	def clear_items(self):
		self.name = self.standard_name
		self.id = ''
		for field in self.fields:
			field.value = ''
		
	def empty_name(self):
		message = 'The "NAME" field requires input.'
		nps.notify_confirm(message, title='Name Required', editw=1)

####################################
# Browse Armor Form
####################################

class BrowseArmor(nps.FormBaseNewWithMenus):
	def beforeEditing(self):
		self.arm.values = self.parentApp.dbhandler.get_all_armor()

	def create(self):
		self.name = 'GENESYS DATABASE - BROWSE - ARMOR'
		
		self.menu = self.new_menu(name='ARMOR MENU')
		self.menu.addItem(text='CREATE', onSelect=self.create_armor)
		self.menu.addItem(text='EDIT', onSelect=self.edit_armor)
		self.menu.addItem(text='DELETE', onSelect=self.delete_armor)
		self.menu.addItem(text='BACK', onSelect=self.back)
		
		self.arm = self.add(RecordList)
		self.arm.category = True
		
	def create_armor(self):
		self.arm.values = ()
		self.parentApp.switchForm('CREATE_ARMOR')
	
	def delete_armor(self):
		self.parentApp.dbhandler.delete_armor(self.arm.get_id())
		self.arm.values = self.parentApp.dbhandler.get_all_armor()
		
	def edit_armor(self):
		data = self.arm.values[self.arm.cursor_line]
		form = self.parentApp.getForm('CREATE_ARMOR')
		formFields = form.fields
		form.id = data[0]
		form.name = 'GENESYS DATABASE - EDIT - ARMOR - ' + data[1]
		for i, field in enumerate(formFields):
			field.value = data[i + 1]
		self.parentApp.switchForm('CREATE_ARMOR')
		
	def back(self):
		self.arm.values = ()
		self.parentApp.switchFormPrevious()

####################################
# Create/Edit Armor Form
####################################

class CreateArmor(nps.ActionFormV2):
	def create(self):
		self.standard_name = 'GENESYS DATABASE - CREATE - ARMOR'
		self.name = self.standard_name
		
		self.id = ''
		self.fields = (
			self.add(nps.TitleText, name='NAME'),
			self.add(nps.TitleText, name='CATEGORY'),
			self.add(nps.TitleText, name='DEFENSE'),
			self.add(nps.TitleText, name='SOAK'),
			self.add(nps.TitleText, name='ENCUMBRANCE'),
			self.add(nps.TitleText, name='PRICE'),
			self.add(nps.TitleText, name='RARITY'),
			self.add(InputBox, name='DESCRIPTION'),
		)
		
	def on_ok(self):
		if self.fields[0].value == '':
			self.empty_name()
		else:
			data = {}
			for field in self.fields:
				data[field.name.lower()] = field.value
			if self.id == '':
				self.parentApp.dbhandler.add_armor(data)
			else:
				self.parentApp.dbhandler.update_armor(self.id, data)
			clear_items()
			self.parentApp.switchFormPrevious()

	def on_cancel(self):
		self.clear_items()
		self.parentApp.switchFormPrevious()
		
	def clear_items():
		self.name = self.standard_name
		self.id = ''
		for field in self.fields:
			field.value = ''
		
	def empty_name(self):
		message = 'The "NAME" field requires input.'
		nps.notify_confirm(message, title='Name Required', editw=1)

####################################
# Browse Weapons Form
####################################

class BrowseWeapons(nps.FormBaseNewWithMenus):
	def beforeEditing(self):
		self.weap.values = self.parentApp.dbhandler.get_all_weapons()

	def create(self):
		self.name = 'GENESYS DATABASE - BROWSE - WEAPONS'
		
		self.menu = self.new_menu(name='WEAPONS MENU')
		self.menu.addItem(text='CREATE', onSelect=self.create_weapon)
		self.menu.addItem(text='EDIT', onSelect=self.edit_weapon)
		self.menu.addItem(text='DELETE', onSelect=self.delete_weapon)
		self.menu.addItem(text='BACK', onSelect=self.back)
		
		self.weap = self.add(RecordList)
		self.weap.category = True
		
	def create_weapon(self):
		self.weap.values = ()
		self.parentApp.switchForm('CREATE_WEAPON')
	
	def delete_weapon(self):
		self.parentApp.dbhandler.delete_weapon(self.weap.get_id())
		self.weap.values = self.parentApp.dbhandler.get_all_weapons()
		
	def edit_weapon(self):
		data = self.weap.values[self.weap.cursor_line]
		form = self.parentApp.getForm('CREATE_WEAPON')
		formFields = form.fields
		form.id = data[0]
		form.name = 'GENESYS DATABASE - EDIT - WEAPON - ' + data[1]
		for i, field in enumerate(formFields):
			field.value = data[i + 1]
		self.parentApp.switchForm('CREATE_WEAPON')
		
	def back(self):
		self.weap.values = ()
		self.parentApp.switchFormPrevious()
		
####################################
# Create/Edit Weapon Form
####################################

class CreateWeapon(nps.ActionFormV2):
	
	def create(self):
		self.standard_name = 'GENESYS DATABASE - CREATE - WEAPON'
		self.name = self.standard_name
		
		self.id = ''
		self.fields = (
			self.add(nps.TitleText, name='NAME'),
			self.add(nps.TitleText, name='CATEGORY'),
			self.add(nps.TitleText, name='SKILL'),
			self.add(nps.TitleText, name='DAMAGE'),
			self.add(nps.TitleText, name='CRITICAL'),
			self.add(nps.TitleText, name='RANGE'),
			self.add(nps.TitleText, name='ENCUMBRANCE'),
			self.add(nps.TitleText, name='PRICE'),
			self.add(nps.TitleText, name='RARITY'),
			self.add(nps.TitleText, name='SPECIAL'),
			self.add(InputBox, name='DESCRIPTION')
		)
		
	def on_ok(self):
		if self.fields[0].value == '':
			self.empty_name()
		else:
			data = {}
			for field in fields:
				data[field.name.lower()] = field.value
			self.name = self.standard_name
			if self.id == '':
				self.parentApp.dbhandler.add_weapon(data)
			else:
				self.parentapp.dbhandler.update_weapon(self.id, data)
			self.clear_items()
			self.parentApp.switchFormPrevious()

	def on_cancel(self):
		self.clear_items()
		self.parentApp.switchFormPrevious()
		
	def clear_items(self):
		self.name = self.standard_name
		self.id = ''
		for field in self.fields:
			field.value = ''
		
	def empty_name(self):
		message = 'The "NAME" field requires input.'
		nps.notify_confirm(message, title='Name Required', editw=1)

####################################
# Create Armor Attachment Form
####################################

class CreateArmorAttachment(nps.ActionFormV2):
	def create(self):
		self.standard_name = 'GENESYS DATABASE - CREATE - ARMOR ATTACHMENT'
		self.name = self.standard_name
			
		self.fields = (
			self.add(nps.TitleText, name='NAME'),
			self.add(nps.TitleText, name='HARDPOINTS'),
			self.add(nps.TitleText, name='PRICE'),
			self.add(nps.TitleText, name='RARITY'),
			self.add(InputBox, name='DESCRIPTION')
		)
		
	def on_ok(self):
		if self.fields[0].value == '':
			self.empty_name()
		else:
			data = {}
			for field in self.fields:
				data[field.name.lower()] = field.value
			data['armor'] = True
			self.parentApp.dbhandler.add_attachment(data)
			self.clear_items()
			self.parentApp.switchFormPrevious()

	def on_cancel(self):
		self.clear_items()
		self.parentApp.switchFormPrevious()

	def clear_items(self):
		self.name = self.standard_name
		self.attach.value = ''
		self.hp.value = ''
		self.price.value = ''
		self.rarity.value = ''
		self.desc.value = ''

	def empty_name(self):
		message = 'The "NAME" field requires input.'
		nps.notify_confirm(message, title='Name Required', editw=1)

####################################
# Create Weapon Attachment Form
####################################

class CreateWeaponAttachment(nps.ActionFormV2):
	def create(self):
		self.standard_name = 'GENESYS DATABASE - CREATE - WEAPON ATTACHMENT'
		self.name = self.standard_name
		
		self.id = ''
		self.fields = (
			self.add(nps.TitleText, name='NAME'),
			self.add(nps.TitleText, name='HARDPOINTS'),
			self.add(nps.TitleText, name='PRICE'),
			self.add(nps.TitleText, name='RARITY'),
			self.add(InputBox, name='DESCRIPTION')
		)

	def on_ok(self):
		if self.fields[0].value == '':
			self.empty_name()
		else:
			data = {}
			for field in self.fields:
				data[field.name.lower()] = field.value
			data['armor'] = False
			self.parentApp.dbhandler.add_attachment(data)
			self.clear_items()
			self.parentApp.switchFormPrevious()

	def on_cancel(self):
		self.clear_items()
		self.parentApp.switchFormPrevious()
		
	def clear_items(self):
		self.name = self.standard_name
		self.id = ''
		for field in self.fields:
			field.value = ''
		
	def empty_name(self):
		message = 'The "NAME" field requires input.'
		nps.notify_confirm(message, title='Name Required', editw=1)
		
####################################
# Create Trope Form
####################################
class CreateTrope(nps.ActionFormV2):
	def create(self):
		self.standard_name = 'GENESYS DATABASE - CREATE - TROPE'
		self.name = self.standard_name
		
		self.id = ''
		self.fields = (
			self.add(nps.TitleText, name='NAME'),
			self.add(InputBox, name='DESCRIPTION')
		)
		
	def on_ok(self):
		if self.fields[0].value == '':
			self.empty_name()
		else:
			data = {}
			for field in self.fields:
				data[field.name.lower()] = field.value
			self.parentApp.dbhandler.add_trope(data)
			self.clear_items()
			self.parentApp.switchFormPrevious()
		
	def on_cancel(self):
		self.clear_items()
		self.parentApp.switchFormPrevious()
		
	def clear_items(self):
		self.name = self.standard_name
		self.id = ''
		for field in self.fields:
			field.value = ''
		
	def empty_name(self):
		message = 'The "NAME" field requires input.'
		nps.notify_confirm(message, title='Name Required', editw=1)

####################################
# Create Tone Form
####################################
class CreateTone(nps.ActionFormV2):
	def create(self):
		self.standard_name = 'GENESYS DATABASE - CREATE - TONE'
		self.name = self.standard_name
		
		self.id = ''
		self.fields = (
			self.add(nps.TitleText, name='NAME'),
			self.add(InputBox, name='DESCRIPTION')
		)
		
	def on_ok(self):
		if self.tone.value == '':
			self.empty_name()
		else:
			data = {}
			for field in self.fields:
				data[field.name.lower()] = field.value
			self.parentApp.dbhandler.add_tone(data)
			self.clear_items()
			self.parentApp.switchFormPrevious()
		
	def on_cancel(self):
		self.clear_items()
		self.parentApp.switchFormPrevious()
		
	def clear_items(self):
		self.name = self.standard_name
		self.id = ''
		for field in self.fields:
			field.value = ''
	
	def empty_name(self):
		message = 'The "NAME" field requires input.'
		nps.notify_confirm(message, title='Name Required', editw=1)

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
		# SETTING MENUS
		self.addForm('MAIN', MainMenu)
		self.addForm('NEWSETTING', NewSetting)
		self.addForm('OPENSETTING', OpenSetting)
		self.addForm('SETTINGMENU', SettingMenu)
		#self.addForm('COMPILE', CompileMenu)
		# BROWSE MENUS
		self.addForm('BROWSE_WEAPONS', BrowseWeapons)
		self.addForm('BROWSE_ARMOR', BrowseArmor)
		self.addForm('BROWSE_GEAR', BrowseGear)
		self.addForm('BROWSE_SKILLS', BrowseSkills)
		# CREATE MENUS
		self.addForm('CREATE_SKILL', CreateSkill)
		self.addForm('CREATE_TALENT', CreateTalent)
		self.addForm('CREATE_WEAPON', CreateWeapon)
		self.addForm('CREATE_WEAPATT', CreateWeaponAttachment)
		self.addForm('CREATE_ARMOR', CreateArmor)
		self.addForm('CREATE_ARMATT', CreateArmorAttachment)
		self.addForm('CREATE_GEAR', CreateGear)
		self.addForm('CREATE_TROPE', CreateTrope)
		self.addForm('CREATE_TONE', CreateTone)

####################################
# Main Function
####################################

if __name__ == '__main__':
	App = GenDB().run()
