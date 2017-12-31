import sublime, sublime_plugin

import os
from os.path import dirname, realpath, expanduser, join

import collections
import json

class IncludeAutoComplete(sublime_plugin.EventListener):

	project_data = {}
	project_path = ""
	paths = []
	files = []
	ext = []

	def on_query_completions(self, view, prefix, locations):
		## Check if completion is needed. 
		# If we have more than one location, forget about it.
		if len(locations) != 1:
			return None

		# If we're not in an include statement, forget about it.
		if not view.match_selector(locations[0],
								   "meta.preprocessor.include & "
								   "(string.quoted.other | "
								   "string.quoted.double)"):
			return None

		self.project_data = view.window().project_data()
		self.project_data = (self.project_data or {})

		# If we're not in a CProject, forget about it.
		if 1 > len(self.getSettings()):
			return None

		# Reset completion data.
		self.paths = []
		self.files = []
		self.ext = []
		self.project_path = ""
		completions = None

		# Load project path
		self.project_path = dirname(view.window().project_file_name())

		# Set the current working directory to the project directory.
		os.chdir(self.project_path)

		# Load folders.
		self.addPath(dirname(view.file_name()))
		for path in self.getSettings()["includes"]:
			self.addPath(path)

		# Load extensions
		extensions = self.getSettings()["header_ext"]
		for extention in extensions:
			self.ext.append(extention)

		# Find files.
		self.findFile(self.ext)

		# Create completions if there are files.
		if 0 < len(self.files):
			completions = []
			for file in self.files:
				completions.append(
					[file + "\tinclude", file]
				)

		return completions

	def addPath(self, path):
		path = realpath(path)
		if not path in self.paths:
			self.paths.append(path)

	def addFile(self, file):
		if not file in self.files:
			self.files.append(file)

	def findFile(self, ext):
		for path in self.paths:
			dirs = os.listdir(path)
			for file in dirs:
				if file.endswith(tuple(ext)):
					self.files.append(file)

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