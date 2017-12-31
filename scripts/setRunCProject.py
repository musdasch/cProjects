import sublime, sublime_plugin

# Command set_run_cprojekct to alter the run command.
class SetRunCprojectCommand(sublime_plugin.WindowCommand):

	project_data = {}
	variables = {}

	def run(self):

		# Get the project data
		self.project_data = self.window.project_data()
		self.project_data = (self.project_data or {})

		# Extract System Variables
		self.variables = self.window.extract_variables()

		if 0 < len(self.getSettings()):
			self.input("Run options:", self.getSettings()["run"], self.setValue, None, None)
		else:
			self.error("There is no valid cProject.")

	def setValue(self, value):
		self.project_data["c_projects_settings"]["run"] = value
		
		self.window.set_project_data(self.project_data)
		self.message("New run options: \"" + value + "\" - OK" )

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