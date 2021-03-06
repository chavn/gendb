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
					"hardpoints" TEXT, \
					"price" TEXT, \
					"rarity" TEXT, \
					"description" TEXT, \
					"armor" BOOLEAN, \
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

	### SETTING RECORDS
	def update_setting(self, data):
		c = self.db.cursor()
		c.execute(
			'UPDATE setting SET name=?, author=?, genre=?, overview=?',
			(data['title'], data['author'], data['main genre(s)'],
			data['overview'])
		)
		self.db.commit()
		c.close
		
	def get_setting(self):
		c = self.db.cursor()
		c.execute('SELECT * FROM setting')
		setting = c.fetchone()
		c.close()
		return setting

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
		c = self.db.cursor()
		c.execute(
			'UPDATE attachments SET name=?, armor=?, hardpoints=?, price=?, \
			rarity=?, description=? WHERE id=?', (data['name'], data['armor'],
			data['hardpoints'], data['price'], data['rarity'],
			data['description'], id)
		)
		self.db.commit()
		c.close()
		
	def get_all_weaponatts(self):
		c = self.db.cursor()
		c.execute('SELECT * FROM attachments WHERE armor = FALSE')
		weaponatts = c.fetchall()
		c.close()
		return weaponatts
		
	def get_all_armoratts(self):
		c = self.db.cursor()
		c.execute('SELECT * FROM attachments WHERE armor = TRUE')
		armoratts = c.fetchall()
		c.close()
		return armoratts
		
	def delete_attachment(self, id):
		c = self.db.cursor()
		c.execute('DELETE FROM attachments WHERE id=?', (id,))
		self.db.commit()
		c.close()

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
			'INSERT INTO talents(name, tier, activation, ranked, description) \
			VALUES(?,?,?,?,?)', (data['name'], data['tier'], data['activation'],
			data['ranked'], data['description'])
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
		c = self.db.cursor()
		c.execute(
			'UPDATE weapons SET name=?, category=?, skill=?, damage=?, \
			critical=?, range=?, encumbrance=?, price=?, rarity=?, special=?, \
			description=? WHERE id=?', (data['name'], data['category'],
			data['skill'], data['damage'], data['critical'], data['range'],
			data['encumbrance'], data['price'], data['rarity'], data['special'],
			data['description'], id)
		)
		self.db.commit()
		c.close()
		
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
		c = self.db.cursor()
		c.execute(
			'UPDATE armor SET name=?, category=?, defense=?, soak=?, \
			encumbrance=?, price=?, rarity=?, description=? WHERE id=?', (
			data['name'], data['category'], data['defense'], data['soak'],
			data['encumbrance'], data['price'], data['rarity'],
			data['description'], id)
		)
		self.db.commit()
		c.close()
		
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

	def update_gear(self, id, data):
		c = self.db.cursor()
		c.execute(
			'UPDATE gear SET name=?, category=?, encumbrance=?, price=?, \
			rarity=?, description=? WHERE id=?', (data['name'],
			data['category'], data['encumbrance'], data['price'],
			data['rarity'], data['description'], id)
		)
		self.db.commit()
		c.close()
		
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
			category_text = 'NAME: %s \t CATEG.: %s'
			return category_text % (vl[1], vl[2])
		else:
			text = 'NAME: %s'
			return text % (vl[1])
		
	def get_id(self):
		return int(self.values[self.cursor_line][0])
	
# Menu selection for main and setting menu
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
# Custom Forms
####################################

# Record Create and Edit Form
class RecordForm(nps.ActionFormV2):
	def __init__(self, *args, **keywords):
		self.standard_name = keywords['std_name']
		self.add_function = keywords['add_function']
		self.update_function = keywords['update_function']
		self.extra_data = {}
		self.id = ''
		self.fields = []
		super(RecordForm, self).__init__(*args, **keywords)
		
	def create(self):
		self.name = self.standard_name
		
	def on_ok(self):
		if self.fields[0].value == '':
			self.empty_name()
		else:
			data = {}
			for field in self.fields:
				data[field.name.lower()] = field.value
			for key in self.extra_data.keys():
				data[key] = self.extra_data[key]
			if self.id == '':
				self.add_function(data)
			else:
				self.update_function(self.id, data)
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
		
# Record Browse Form
class RecordBrowse(nps.FormBaseNewWithMenus):
	def __init__(self, *args, **keywords):
		self.menu_title = keywords['menu_title']
		self.show_category = keywords['show_category']
		self.get_all_function = keywords['get_all']
		self.create_form = keywords['create_form']
		self.delete = keywords['delete_function']
		self.create_type = keywords['create_type']
		self.display_name = keywords['display_name']
		super(RecordBrowse, self).__init__(*args, **keywords)
		self.add_handlers({
			'c': self.create_function,
			'e': self.edit_function,
			'd': self.delete_function,
			'b': self.back_function
		})

	def beforeEditing(self):
		self.records.values = self.get_all_function()
		
	def create(self):
		self.name = 'GENESYS DATABASE - BROWSE - ' + self.display_name
		
		self.menu = self.new_menu(name=self.menu_title)
		self.menu.addItem(text='CREATE', onSelect=self.create_function, shortcut='c')
		self.menu.addItem(text='EDIT', onSelect=self.edit_function, shortcut='e')
		self.menu.addItem(text='DELETE', onSelect=self.delete_function, shortcut='d')
		self.menu.addItem(text='BACK', onSelect=self.back_function, shortcut='b')
		
		self.records = self.add(RecordList)
		self.records.category = self.show_category
		
	def create_function(self, *args):
		self.records.values = ()
		self.parentApp.switchForm(self.create_form)
	
	def delete_function(self, *args):
		self.delete(self.records.get_id())
		self.records.values = self.get_all_function()
		
	def edit_function(self, *args):
		data = self.records.values[self.records.cursor_line]
		form = self.parentApp.getForm(self.create_form)
		form.id = data[0]
		form.name = 'GENESYS DATABASE - EDIT - ' + self.create_type + ' - ' + data[1]
		for i, field in enumerate(form.fields):
			field.value = data[i + 1]
		self.parentApp.switchForm(self.create_form)
		
	def back_function(self, *args):
		self.records.values = ()
		self.parentApp.switchForm('SETTINGMENU')

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
# Edit Setting Form
####################################

class EditSetting(nps.ActionFormV2):
	def beforeEditing(self):
		data = self.parentApp.dbhandler.get_setting()
		for i, field in enumerate(self.fields):
			field.value = data[i]
		
	def create(self):
		self.name = 'GENESYS DATABASE - EDIT SETTING'

		self.fields = [
			self.add(nps.TitleText, name='TITLE'),
			self.add(nps.TitleText, name='AUTHOR'),
			self.add(nps.TitleText, name='MAIN GENRE(S)'),
			self.add(InputBox, name='OVERVIEW')
		]

	def on_ok(self):
		if self.fields[0].value == '':
			self.empty_title()
		else:
			data={}
			for field in self.fields:
				data[field.name.lower()] = field.value
			self.parentApp.dbhandler.update_setting(data)
			self.clear_items()
			self.parentApp.switchForm('SETTINGMENU')

	def on_cancel(self):
		self.clear_items()
		self.parentApp.switchFormPrevious()
		
	def clear_items(self):
		for field in self.fields:
			field.value = ''
	
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
			'SETTING', 'TROPES', '!ARCHETYPES/SPECIES', '!CAREERS',
			'!FACTIONS/ORGANIZATIONS', '!HEROIC ABILITIES', 'SKILLS',
			'TALENTS', 'WEAPONS', 'WEAPON ATTACHMENTS', 'ARMOR',
			'ARMOR ATTACHMENTS', 'GEAR', 'CLOSE SETTING'
		)

		self.menu.menu_actions = {
			'SETTING': 'EDIT_SETTING',
			'TROPES': 'BROWSE_TROPES',
			'SKILLS': 'BROWSE_SKILLS',
			'TALENTS': 'BROWSE_TALENTS',
			'WEAPONS': 'BROWSE_WEAPONS',
			'WEAPON ATTACHMENTS': 'BROWSE_WEAPATTS',
			'ARMOR': 'BROWSE_ARMOR',
			'ARMOR ATTACHMENTS': 'BROWSE_ARMATTS',
			'GEAR': 'BROWSE_GEAR'
		}


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
		
		self.browse_weapons = self.addForm('BROWSE_WEAPONS', RecordBrowse,
			menu_title='WEAPONS MENU',
			show_category=True,
			get_all=self.dbhandler.get_all_weapons,
			create_form='CREATE_WEAPON',
			delete_function=self.dbhandler.delete_weapon,
			create_type='WEAPON',
			display_name='WEAPONS'
		)
		
		self.browse_armor = self.addForm('BROWSE_ARMOR', RecordBrowse,
			menu_title='ARMOR MENU',
			show_category=True,
			get_all=self.dbhandler.get_all_armor,
			create_form='CREATE_ARMOR',
			delete_function=self.dbhandler.delete_armor,
			create_type='ARMOR',
			display_name='ARMOR'
		)
				
		self.browse_gear = self.addForm('BROWSE_GEAR', RecordBrowse,
			menu_title='GEAR MENU',
			show_category=True,
			get_all=self.dbhandler.get_all_gear,
			create_form='CREATE_GEAR',
			delete_function=self.dbhandler.delete_gear,
			create_type='GEAR',
			display_name='GEAR'
		)
		
		self.browse_skills = self.addForm('BROWSE_SKILLS', RecordBrowse,
			menu_title='SKILLS MENU',
			show_category=True,
			get_all=self.dbhandler.get_all_skills,
			create_form='CREATE_SKILL',
			delete_function=self.dbhandler.delete_skill,
			create_type='SKILL',
			display_name='SKILLS'
		)
		
		self.browse_talents = self.addForm('BROWSE_TALENTS', RecordBrowse,
			menu_title='TALENTS MENU',
			show_category=False,
			get_all=self.dbhandler.get_all_talents,
			create_form='CREATE_TALENT',
			delete_function=self.dbhandler.delete_talent,
			create_type='TALENT',
			display_name='TALENTS'
		)
		
		self.browse_tropes = self.addForm('BROWSE_TROPES', RecordBrowse,
			menu_title='TROPES MENU',
			show_category=False,
			get_all=self.dbhandler.get_all_tropes,
			create_form='CREATE_TROPE',
			delete_function=self.dbhandler.delete_trope,
			create_type='TROPE',
			display_name='TROPES'
		)
		
		self.browse_weapatts = self.addForm('BROWSE_WEAPATTS', RecordBrowse,
			menu_title='WEAPON ATT. MENU',
			show_category=False,
			get_all=self.dbhandler.get_all_weaponatts,
			create_form='CREATE_WEAPATT',
			delete_function=self.dbhandler.delete_attachment,
			create_type='WEAPON ATTACHMENT',
			display_name='WEAPON ATTACHMENTS'
		)
		
		self.browse_armatts = self.addForm('BROWSE_ARMATTS', RecordBrowse,
			menu_title='ARMOR ATT. MENU',
			show_category=False,
			get_all=self.dbhandler.get_all_armoratts,
			create_form='CREATE_ARMATT',
			delete_function=self.dbhandler.delete_attachment,
			create_type='ARMOR ATTACHMENT',
			display_name='ARMOR ATTACHMENTS'
		)
		
		# CREATE/EDIT MENUS
		
		# Setting Edit form
		self.edit_setting = self.addForm('EDIT_SETTING', EditSetting)
		
		# Skill Create/Edit form
		self.create_skill = self.addForm('CREATE_SKILL', RecordForm,
			std_name='GENESYS DATABASE - CREATE - SKILL',
			add_function=self.dbhandler.add_skill,
			update_function=self.dbhandler.update_skill
		)
		
		self.create_skill.fields = [
			self.create_skill.add(nps.TitleText, name='NAME', begin_entry_at=17),
			self.create_skill.add(nps.TitleText, name='CATEGORY', begin_entry_at=17),
			self.create_skill.add(nps.TitleText, name='CHARACTERISTIC', begin_entry_at=17),
			self.create_skill.add(InputBox, name='DESCRIPTION', max_height=6),
			self.create_skill.add(InputBox, name='SHOULD USE IF...', max_height=6),
			self.create_skill.add(InputBox, name='SHOULD NOT USE IF...', max_height=6)
		]
		
		# Talent Create/Edit form
		self.create_talent = self.addForm('CREATE_TALENT', RecordForm,
			std_name='GENESYS DATABASE - CREATE - TALENT',
			add_function=self.dbhandler.add_talent,
			update_function=self.dbhandler.update_talent
		)
		
		self.create_talent.fields = [
			self.create_talent.add(nps.TitleText, name='NAME'),
			self.create_talent.add(nps.TitleText, name='TIER'),
			self.create_talent.add(nps.TitleText, name='ACTIVATION'),
			self.create_talent.add(nps.Checkbox, name='RANKED'),
			self.create_talent.add(InputBox, name='DESCRIPTION')
		]
		
		# Weapon Create/Edit form
		self.create_weapon = self.addForm('CREATE_WEAPON', RecordForm,
			std_name='GENESYS DATABASE - CREATE - WEAPON',
			add_function=self.dbhandler.add_weapon,
			update_function=self.dbhandler.update_weapon
		)
		
		self.create_weapon.fields = [
			self.create_weapon.add(nps.TitleText, name='NAME'),
			self.create_weapon.add(nps.TitleText, name='CATEGORY'),
			self.create_weapon.add(nps.TitleText, name='SKILL'),
			self.create_weapon.add(nps.TitleText, name='DAMAGE'),
			self.create_weapon.add(nps.TitleText, name='CRITICAL'),
			self.create_weapon.add(nps.TitleText, name='RANGE'),
			self.create_weapon.add(nps.TitleText, name='ENCUMBRANCE'),
			self.create_weapon.add(nps.TitleText, name='PRICE'),
			self.create_weapon.add(nps.TitleText, name='RARITY'),
			self.create_weapon.add(nps.TitleText, name='SPECIAL'),
			self.create_weapon.add(InputBox, name='DESCRIPTION')
		]
		
		# Weapon Attachment Create/Edit form
		self.create_weapon_att = self.addForm('CREATE_WEAPATT', RecordForm,
			std_name='GENESYS DATABASE - CREATE - WEAPON ATTACHMENT',
			add_function=self.dbhandler.add_attachment,
			update_function=self.dbhandler.update_attachment
		)
		
		self.create_weapon_att.fields = [
			self.create_weapon_att.add(nps.TitleText, name='NAME'),
			self.create_weapon_att.add(nps.TitleText, name='HARDPOINTS'),
			self.create_weapon_att.add(nps.TitleText, name='PRICE'),
			self.create_weapon_att.add(nps.TitleText, name='RARITY'),
			self.create_weapon_att.add(InputBox, name='DESCRIPTION')
		]
		
		self.create_weapon_att.extra_data = { 'armor': False }
		
		# Armor Create/Edit form
		self.create_armor = self.addForm('CREATE_ARMOR', RecordForm,
			std_name='GENESYS DATABASE - CREATE - ARMOR',
			add_function=self.dbhandler.add_armor,
			update_function=self.dbhandler.update_armor
		)
		
		self.create_armor.fields = [
			self.create_armor.add(nps.TitleText, name='NAME'),
			self.create_armor.add(nps.TitleText, name='CATEGORY'),
			self.create_armor.add(nps.TitleText, name='DEFENSE'),
			self.create_armor.add(nps.TitleText, name='SOAK'),
			self.create_armor.add(nps.TitleText, name='ENCUMBRANCE'),
			self.create_armor.add(nps.TitleText, name='PRICE'),
			self.create_armor.add(nps.TitleText, name='RARITY'),
			self.create_armor.add(InputBox, name='DESCRIPTION')
		]
		
		# Armor Attachment Create/Edit form
		self.create_armor_att = self.addForm('CREATE_ARMATT', RecordForm,
			std_name='GENESYS DATABASE - CREATE - ARMOR ATTACHMENT',
			add_function=self.dbhandler.add_attachment,
			update_function=self.dbhandler.update_attachment
		)
		
		self.create_armor_att.fields = [
			self.create_armor_att.add(nps.TitleText, name='NAME'),
			self.create_armor_att.add(nps.TitleText, name='HARDPOINTS'),
			self.create_armor_att.add(nps.TitleText, name='PRICE'),
			self.create_armor_att.add(nps.TitleText, name='RARITY'),
			self.create_armor_att.add(InputBox, name='DESCRIPTION')
		]
		
		self.create_armor_att.extra_data = { 'armor': True }
		
		# Gear Create/Edit form
		self.create_gear = self.addForm('CREATE_GEAR', RecordForm,
			std_name='GENESYS DATABASE - CREATE - GEAR',
			add_function=self.dbhandler.add_gear,
			update_function=self.dbhandler.update_gear
		)
		
		self.create_gear.fields = [
			self.create_gear.add(nps.TitleText, name='NAME'),
			self.create_gear.add(nps.TitleText, name='CATEGORY'),
			self.create_gear.add(nps.TitleText, name='ENCUMBRANCE'),
			self.create_gear.add(nps.TitleText, name='PRICE'),
			self.create_gear.add(nps.TitleText, name='RARITY'),
			self.create_gear.add(InputBox, name='DESCRIPTION')
		]
		
		# Trope Create/Edit form
		self.create_trope = self.addForm('CREATE_TROPE', RecordForm,
			std_name='GENESYS DATABASE - CREATE - TROPE',
			add_function=self.dbhandler.add_trope,
			update_function=self.dbhandler.update_trope
		)
		
		self.create_trope.fields = [
			self.create_trope.add(nps.TitleText, name='NAME'),
			self.create_trope.add(InputBox, name='DESCRIPTION')
		]
		
		# Tone Create/Edit form
		self.create_tone = self.addForm('CREATE_TONE', RecordForm,
			std_name='GENESYS DATABASE - CREATE - TONE',
			add_function=self.dbhandler.add_tone,
			update_function=self.dbhandler.update_tone
		)
		
		self.create_tone.fields = [
			self.create_tone.add(nps.TitleText, name='NAME'),
			self.create_tone.add(InputBox, name='DESCRIPTION')
		]
		

####################################
# Main Function
####################################

if __name__ == '__main__':
	App = GenDB().run()
