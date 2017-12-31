import sublime, sublime_plugin

# Command set_source_cproject to set a new source file.
class SetSourceCprojectCommand(sublime_plugin.WindowCommand):

	project_data = {}
	variables = {}
	open_files = []

	#On set_source_cproject window command.
	def run(self):

		# Get the project data
		self.project_data = self.window.project_data()
		self.project_data = (self.project_data or {})

		# Extract System Variables
		self.variables = self.window.extract_variables()

		# Reset open files
		self.open_files = []

		if 0 < len(self.getSettings()):
			current_file = 0;

			# Load cpp files for quick panel
			for view in self.window.views():
				if None != view.file_name():
					if -1 < view.file_name().find(".cpp"):
						self.open_files.append(
							view.file_name().replace(self.variables["project_path"], ".")
						)

						if view.file_name() == self.variables["file"]:
							current_file = len(self.open_files) - 1

			# Show quick panel to choose file.
			if 0 < len(self.open_files):
				self.quickPanel(self.open_files, self.setSourceFile, sublime.KEEP_OPEN_ON_FOCUS_LOST, current_file)

		else:
			self.error("There is no valid cProject.")

	def setSourceFile(self, index):
		if -1 < index:
			self.project_data["c_projects_settings"]["source_files"] = self.open_files[index]
			self.window.set_project_data(self.project_data)
			self.message("New source file: \"" + self.open_files[index] + "\" - OK" )
		else:
			self.message("Old source file: \"" + self.project_data["c_projects_settings"]["source_files"] + "\" - OK" )

	def getSettings(self):
		return self.project_data.get("c_projects_settings", {})

	def quickPanel(self, items, on_done, flags, index):
		self.window.show_quick_panel(items, on_done, flags, index)

	def error(self, message):
		sublime.error_message(message)

	def message(self, message):
		self.window.status_message(message)