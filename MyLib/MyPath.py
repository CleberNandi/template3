# encoding: utf-8
import inspect
import os
import sys

ModuleFolder = os.path.realpath(os.path.dirname(inspect.getfile(inspect.currentframe())))
if ModuleFolder not in sys.path:
	sys.path.insert(0, ModuleFolder)

__version__ = "01.20201125.01"


# ModulesPath = MODULE_PATH