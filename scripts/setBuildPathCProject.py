import sublime, sublime_plugin

# Command set_build_path_cprojekct to alter the build path.
class SetBuildPathCprojectCommand(sublime_plugin.WindowCommand):

	project_data = {}
	variables = {}

	def run(self):

		# Get the project data
		self.project_data = self.window.project_data()
		self.project_data = (self.project_data or {})

		# Extract System Variables
		self.variables = self.window.extract_variables()

		if 0 < len(self.getSettings()):
			self.input("build_path:", self.getSettings()["build_path"], self.setBuildPath, None, None)
		else:
			self.error("There is no valid cProject.")

	def setBuildPath(self, path):
		self.project_data["c_projects_settings"]["build_path"] = path
		
		self.window.set_project_data(self.project_data)
		self.message("New build_path: \"" + path + "\" - OK" )

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
