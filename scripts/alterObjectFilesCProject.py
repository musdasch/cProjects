import sublime, sublime_plugin

# Command alter_object_files_cprojekct enables you to change the object files.
class AlterObjectFilesCprojectCommand(sublime_plugin.WindowCommand):

	project_data = {}
	variables = {}
	index = 0;
	chosen = -1
	open_files = []
	current_file = 0

	def run(self):

		# Get the project data
		self.project_data = self.window.project_data()
		self.project_data = (self.project_data or {})

		# Extract System Variables
		self.variables = self.window.extract_variables()

		# Reset
		self.chosen = -1
		self.open_files = []
		self.current_file = 0

		if 0 < len(self.getSettings()):

			# Load cpp files for quick panel
			for view in self.window.views():
				if None != view.file_name():
					if -1 < view.file_name().find(".cpp"):
						self.open_files.append(
							view.file_name().replace(self.variables["project_path"], ".")
						)

						if view.file_name() == self.variables["file"]:
							self.current_file = len(self.open_files) - 1
			
			items = ["Add object file", "Add from opened file"]

			if(0 < len(self.getSettings()["object_files"])):
				items.append("Alter object file")
				items.append("Delete object files")

			self.quickPanel(items, self.selectAction, sublime.KEEP_OPEN_ON_FOCUS_LOST, self.index)
		else:
			self.error("There is no valid cProject.")

	def selectAction(self, option):
		if -1 < option:
			self.index = option
			if 0 == option:
				self.askForNew()
			elif 1 == option:
				self.selectOpended()
			elif 2 == option:
				self.selectToAlter()
			elif 3== option:
				self.selectToDel()

	def askForNew(self):
		self.input("New object file:", "." + self.delim() + "src" + self.delim() + "sources" + self.delim(), self.add, None, None)

	def add(self, path):
		self.project_data["c_projects_settings"]["object_files"].append(path)
		
		self.window.set_project_data(self.project_data)
		self.message("Add new object file: \"" + path + "\" - OK" )

	def selectOpended(self):
		if 0 < len(self.open_files):
			self.quickPanel(self.open_files, self.addFromOpended, sublime.KEEP_OPEN_ON_FOCUS_LOST, self.current_file)
		else:
			self.error("There no object files opened.")

	def addFromOpended(self, index):
		self.project_data["c_projects_settings"]["object_files"].append(self.open_files[index])
		
		self.window.set_project_data(self.project_data)
		self.message("Add new object file: \"" + self.open_files[index] + "\" - OK" )

	
	def selectToAlter(self):
		self.quickPanel(self.project_data["c_projects_settings"]["object_files"], self.askForAlter, sublime.KEEP_OPEN_ON_FOCUS_LOST, 0)

	def askForAlter(self, index):
		self.chosen = index
		self.input("Alter library path:", self.project_data["c_projects_settings"]["object_files"][index], self.alter, None, None)

	def alter(self, path):
		if -1 < self.chosen:
			self.project_data["c_projects_settings"]["object_files"][self.chosen] = path
		
			self.window.set_project_data(self.project_data)
			self.message("Alter object file: \"" + path + "\" - OK" )

	def selectToDel(self):
		self.quickPanel(self.project_data["c_projects_settings"]["object_files"], self.delete, sublime.KEEP_OPEN_ON_FOCUS_LOST, 0)

	def delete(self, index):
		path = self.project_data["c_projects_settings"]["object_files"][index]
		del self.project_data["c_projects_settings"]["object_files"][index]
		
		self.window.set_project_data(self.project_data)
		self.message("Delete object file: \"" + path + "\" - OK" )

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