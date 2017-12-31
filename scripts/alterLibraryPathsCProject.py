import sublime, sublime_plugin

# Command alter_library_paths_cprojekct enables you to change the library paths of the project.
class AlterLibraryPathsCprojectCommand(sublime_plugin.WindowCommand):

	project_data = {}
	variables = {}
	index = 0;
	chosen = -1;

	def run(self):

		# Get the project data
		self.project_data = self.window.project_data()
		self.project_data = (self.project_data or {})

		# Extract System Variables
		self.variables = self.window.extract_variables()

		# Reset chosen
		self.chosen = -1;

		if 0 < len(self.getSettings()):
			
			items = ["Add library path"]

			if(0 < len(self.getSettings()["library_paths"])):
				items.append("Alter library path")
				items.append("Delete library path")

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
		self.input("New library path:", "./lib/", self.add, None, None)

	def add(self, path):
		self.project_data["c_projects_settings"]["library_paths"].append(path)
		
		self.window.set_project_data(self.project_data)
		self.message("Add new library path: \"" + path + "\" - OK" )

	def selectToAlter(self):
		self.quickPanel(self.project_data["c_projects_settings"]["library_paths"], self.askForAlter, sublime.KEEP_OPEN_ON_FOCUS_LOST, 0)

	def askForAlter(self, index):
		self.chosen = index
		self.input("Alter library path:", self.project_data["c_projects_settings"]["library_paths"][index], self.alter, None, None)

	def alter(self, path):
		if -1 < self.chosen:
			self.project_data["c_projects_settings"]["library_paths"][self.chosen] = path
		
			self.window.set_project_data(self.project_data)
			self.message("Alter library path: \"" + path + "\" - OK" )

	def selectToDel(self):
		self.quickPanel(self.project_data["c_projects_settings"]["library_paths"], self.delete, sublime.KEEP_OPEN_ON_FOCUS_LOST, 0)

	def delete(self, index):
		path = self.project_data["c_projects_settings"]["library_paths"][index]
		del self.project_data["c_projects_settings"]["library_paths"][index]
		
		self.window.set_project_data(self.project_data)
		self.message("Delete library path: \"" + path + "\" - OK" )

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