import sublime, sublime_plugin

# Command alter_includes_cprojekct enables you to change the includes
class AlterIncludesCprojectCommand(sublime_plugin.WindowCommand):

	project_data = {}
	variables = {}
	index = 0;
	chosenInclude = -1;

	def run(self):

		# Get the project data
		self.project_data = self.window.project_data()
		self.project_data = (self.project_data or {})

		# Extract System Variables
		self.variables = self.window.extract_variables()

		# Reset chosen include
		self.chosenInclude = -1;

		if 0 < len(self.getSettings()):
			
			items = ["Add include"]

			if(0 < len(self.getSettings()["includes"])):
				items.append("Alter include")
				items.append("Delete include")

			self.quickPanel(items, self.selectAction, sublime.KEEP_OPEN_ON_FOCUS_LOST, self.index)
		else:
			self.error("There is no valid cProject.")

	def selectAction(self, option):
		if -1 < option:
			self.index = option
			if 0 == option:
				self.askForNew()
			elif 1 == option:
				self.selectToAlter()
			elif 2== option:
				self.selectToDel()

	def askForNew(self):
		self.input("New Include:", "." + self.delim() + "src" + self.delim(), self.add, None, None)

	def add(self, path):
		self.project_data["c_projects_settings"]["includes"].append(path)
		
		self.window.set_project_data(self.project_data)
		self.message("Add new include: \"" + path + "\" - OK" )

	def selectToAlter(self):
		self.quickPanel(self.project_data["c_projects_settings"]["includes"], self.askForAlter, sublime.KEEP_OPEN_ON_FOCUS_LOST, 0)

	def askForAlter(self, index):
		self.chosenInclude = index
		self.input("Alter Include:", self.project_data["c_projects_settings"]["includes"][index], self.alter, None, None)

	def alter(self, path):
		if -1 < self.chosenInclude:
			self.project_data["c_projects_settings"]["includes"][self.chosenInclude] = path
		
			self.window.set_project_data(self.project_data)
			self.message("Alter include: \"" + path + "\" - OK" )

	def selectToDel(self):
		self.quickPanel(self.project_data["c_projects_settings"]["includes"], self.delete, sublime.KEEP_OPEN_ON_FOCUS_LOST, 0)

	def delete(self, index):
		path = self.project_data["c_projects_settings"]["includes"][index]
		del self.project_data["c_projects_settings"]["includes"][index]
		
		self.window.set_project_data(self.project_data)
		self.message("Delete include: \"" + path + "\" - OK" )

	def getSettings(self):
		return self.project_data.get("c_projects_settings", {})

	def input(self, caption, initial_text, on_done, on_change, on_cancel):
		self.window.show_input_panel(caption, initial_text, on_done, on_change, on_cancel)

	def quickPanel(self, items, on_done, flags, index):
		self.window.show_quick_panel(items, on_done, flags, index)

	def error(self, message):
		sublime.error_message(message)

	def message(self, message):
		self.window.status_message(message)

	def delim(self):
		if 'windows' == sublime.platform():
			out = "\\"
		elif 'linux' == sublime.platform():
			out = "/"
		else:
			out = '/'

		return out