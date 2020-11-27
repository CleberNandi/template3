# encoding: utf-8
import inspect
import os
import sys

from configparser import ConfigParser

ModuleFolder = os.path.realpath(os.path.dirname(inspect.getfile(inspect.currentframe())))
if ModuleFolder not in sys.path:
	sys.path.insert(0, ModuleFolder)

from MyEnvironment import GetShortHostname, GetHostnameLong, GetDCLocation, GetEnvironment

__version__ = "01.20201125.01"

ConfFile = "config.conf"

Conf = ConfigParser()
if os.path.exists(ConfFile):
	Conf.read(ConfFile)
else:
	raise TypeError(f"Erro ao ler arquivo de config")

SCRIPT_FRIENDLYNAME = Conf.get("APP", "SCRIPT_FRIENDLYNAME")
VERSION_APP = Conf.get("APP", "VERSION_APP")
ROOT_PATH = os.path.abspath(os.getcwd())
MODULE_PATH = Conf.get("PATH", "MODULES_PATH")
LOGGING_DIR = os.path.join(ROOT_PATH, "logs")
LOGGING_NAME_PATH = os.path.join(LOGGING_DIR, SCRIPT_FRIENDLYNAME + ".log")
START_SCRIPT_MESSAGE = " BEGIN ".center(72, "=")
END_SCRIPT_MESSAGE = " END ".center(72, "=")
HOSTNAME = GetShortHostname()
HOSTNAME_LONG = GetHostnameLong()
ENVIRONMENT = GetEnvironment(HOSTNAME)
LOCATION = GetDCLocation(HOSTNAME)

if __name__ == "__main__":
	print(SCRIPT_FRIENDLYNAME)
	print(VERSION_APP)
	print(MODULE_PATH)