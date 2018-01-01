import sublime, sublime_plugin

from os.path import basename, splitext

# List of variable names we want to support
custom_var_list = [
	"compiler",
	"build_path",
	"single_build_path",
	"run",
	"single_run",
	"options",
	"single_options"
]

# Build Command for CProjekt
class BuildCprojectCommand(sublime_plugin.WindowCommand):
	"""
	Provide custom build variables to a build system, such as a value that needs
	to be specific to a current project.
	This example only allows for variables in the "cmd" field, but could be
	easily extended.
	"""
	def createExecDict(self, sourceDict):
		global custom_var_list

		# Get the project specific settings
		project_data = self.window.project_data ()
		project_settings = (project_data or {}).get ("c_projects_settings", {})

		# Get the view specific settings
		view_settings = self.window.active_view ().settings ()

		# Variables to expand; start with defaults, then add ours.
		variables = self.window.extract_variables ()
		
		# Create source_file and source_base_name
		variables["source_file"] = sublime.expand_variables(view_settings.get( "c_projects_source_file",
				project_settings.get("source_file", "")), variables)
		variables["source_base_name"] = basename(splitext(variables["source_file"])[0])

		for custom_var in custom_var_list:
			variables[custom_var] = sublime.expand_variables(view_settings.get( "c_projects_" + custom_var,
				project_settings.get(custom_var, "")), variables)
		
		# Load object_files
		object_file_list = sublime.expand_variables(view_settings.get( "c_projects_object_files",
			project_settings.get("object_files", {})), variables)

		variables["object_files"] = ""

		for object_file in object_file_list:
			variables["object_files"] += " " + object_file

		# Load includes
		include_list = sublime.expand_variables(view_settings.get( "c_projects_includes",
			project_settings.get("includes", {})), variables)

		variables["includes"] = ""

		for include in include_list:
			variables["includes"] += " -I" + include

		# Load library paths
		library_path_list = sublime.expand_variables(view_settings.get( "c_projects_library_paths",
			project_settings.get("library_paths", {})), variables)

		variables["library_paths"] = ""

		for library_path in library_path_list:
			variables["library_paths"] += " -L" + library_path

		# Load libraries
		library_list = sublime.expand_variables(view_settings.get( "c_projects_libraries",
			project_settings.get("libraries", {})), variables)

		variables["libraries"] = ""

		for library in library_list:
			variables["libraries"] += " -l" + library


		# Create arguments to return by expanding variables in the
		# arguments given.
		args = sublime.expand_variables(sourceDict, variables)

		# Rename the command parameter to what exec expects.
		args["cmd"] = args.pop ("command", [])

		return args

	def run(self, **kwargs):
		self.window.run_command ("exec", self.createExecDict (kwargs))