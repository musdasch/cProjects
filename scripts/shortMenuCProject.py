import sublime, sublime_plugin

from os.path import dirname, realpath, expanduser
import json

# Command short_menu_cproject opens the CProjekt short menu.
class ShortMenuCprojectCommand(sublime_plugin.WindowCommand):

	menu = {}
	index = 0

	def run(self):
		path = dirname(realpath(__file__))
		
		json_data = open(path + self.delim() + ".." + self.delim() + "menus" + self.delim() + "Main.sublime-menu").read()
		json_data = json.loads(json_data)
		
		self.menu = json_data[0]["children"][0]["children"]

		menu_items = []
		for item in self.menu:
			menu_items.append(item["caption"])

		self.quickPanel(menu_items, self.selectAction, sublime.KEEP_OPEN_ON_FOCUS_LOST, self.index)

	def selectAction(self, option):
		if -1 < option:
			self.index = option
			self.window.run_command(self.menu[option]["command"])

	def quickPanel(self, items, on_done, flags, index):
		self.window.show_quick_panel(items, on_done, flags, index)

	def delim(self):
		if 'windows' == sublime.platform():
			out = "\\"
		elif 'linux' == sublime.platform():
			out = "/"
		else:
			out = '/'

		return out