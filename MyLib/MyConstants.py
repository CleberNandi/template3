# encoding: utf-8
import os

from MyLib.MyPath import RootPath
from MyLib.MyPath import LooginPath
from MyLib.MyEnvironment import GetShortHostname, GetHostnameLong, GetDCLocation, GetEnvironment

__version__ = "01.20201125.01"

SCRIPT_FRIENDLYNAME = "MyLib"
ROOT_PATH = RootPath
LOGGING_DIR = LooginPath
LOGGING_NAME_PATH = os.path.join(LOGGING_DIR, SCRIPT_FRIENDLYNAME + ".log")
START_SCRIPT_MESSAGE = " BEGIN ".center(72, "=")
END_SCRIPT_MESSAGE = " END ".center(72, "=")
HOSTNAME = GetShortHostname()
HOSTNAME_LONG = GetHostnameLong()
ENVIRONMENT = GetEnvironment(HOSTNAME)
LOCATION = GetDCLocation(HOSTNAME)