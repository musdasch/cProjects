import sublime, sublime_plugin

import os
from os.path import dirname, realpath, expanduser
from shutil import copyfile

#Creat new CProject
class NewCprojectCommand(sublime_plugin.WindowCommand):
	project_name = ''
	project_path = ''
	plugin_path = ''

	def run(self):
		self.message('Create cProject')
		self.plugin_path = dirname(realpath(__file__))
		self.inputName()

	def folder(self, index):
		out = expanduser("~")
		if index < len(self.window.folders()):
			out = self.window.folders()[index] 
		return out

	def makedirs(self, path):
		if not os.path.isdir(path):
			os.makedirs(path)
			self.message(path + ' - Created')
		else:
			self.message(path + ' - OK')

	def input(self, caption, initial_text, on_done, on_change, on_cancel):
		self.window.show_input_panel(caption, initial_text, on_done, on_change, on_cancel)

	def message(self, message):
		self.window.status_message(message)
	
	def inputName(self):
		self.input('Project Name:', '', self.inputPath, None, None)

	def inputPath(self, name):
		self.setName(name)
		self.input('Project Path:', self.folder(0), self.createProject, None, None)

	def createProject(self, path):
		self.setPath(path)
		self.makedirs(self.project_path)
		self.makedirs(self.project_path + self.delim() + 'bin')
		self.makedirs(self.project_path + self.delim() + 'bin' + self.delim() + 'builds')
		self.makedirs(self.project_path + self.delim() + 'src')
		self.makedirs(self.project_path + self.delim() + 'src' + self.delim() + 'sources')
		self.makedirs(self.project_path + self.delim() + 'src' + self.delim() + 'headers')
		self.makedirs(self.project_path + self.delim() + 'res')
		self.makedirs(self.project_path + self.delim() + 'lib')

		templatePath = self.plugin_path + self.delim() + '..' + self.delim() + 'templates' + self.delim()
		targetPath = self.project_path + self.delim() + self.project_name + '.sublime-project'

		if os.path.isfile(templatePath + 'template[' + sublime.platform() + '].sublime-project' ): 
			copyfile(templatePath + 'template[' + sublime.platform() + '].sublime-project', targetPath)
		else:
			copyfile(templatePath + 'template.sublime-project', targetPath)

		os.system('subl --project ' + self.project_path + self.delim() + self.project_name + '.sublime-project')

	def setName(self, name):
		self.message("Project Name: " + name)
		self.project_name = name

	def setPath(self, path):
		self.message("Project Path: " + path)
		self.project_path = path

	def delim(self):
		if 'windows' == sublime.platform():
			out = "\\"
		elif 'linux' == sublime.platform():
			out = "/"
		else:
			out = '/'

		return out
