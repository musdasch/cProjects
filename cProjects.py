import sublime, sublime_plugin
import sys
from os.path import dirname, realpath, expanduser

scripts_path = dirname(realpath(__file__)) + "/scripts"
isset = False
for path in sys.path:
	if path == scripts_path:
		isset = True

if not isset:
	sys.path.append(scripts_path)

# Import all Scripts
from buildCProject import *
from newCProject import *
from setBuildPathCProject import *
from setSingleBuildPathCProject import *
from setCompilerCProject import *
from setOptionsCProject import *
from setSingleOptionsCProject import *
from setRunCProject import *
from setSourceCProject import *
from alterIncludesCProject import *
from alterLibrariesCProject import *
from alterLibraryPathsCProject import *
from alterObjectFilesCProject import *
from shortMenuCProject import *
from autocompleteCProject import *
