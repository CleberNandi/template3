# -*- utf-8 -*-
import os
import sys

from configparser import ConfigParser

ConfFile = "config.conf"

Conf = ConfigParser()
if os.path.exists(ConfFile):
	Conf.read(ConfFile)
else:
	raise TypeError(f"Erro ao ler arquivo de config")

sys.path.insert(0, Conf.get("PATH", "MODULES_PATH"))
from MyMessage import PrintMessage
from MyText import ListFilesOnDir
from MyEmail import SendEmail, SendEmailInfo, SendEmailWarnig, SendEmailError, SendEmailGmail

from MyConstants import START_SCRIPT_MESSAGE, END_SCRIPT_MESSAGE, HOSTNAME, ENVIRONMENT, LOCATION
from MyConstants import ROOT_PATH, MODULE_PATH, SCRIPT_FRIENDLYNAME, VERSION_APP

__version__ = VERSION_APP

#  ================= Variables Globals ================

#  ==================== Start Loggin ==================
PrintMessage(START_SCRIPT_MESSAGE, LogOnly=True)

PrintMessage(f"Script version: {__version__}", LogOnly=True)
PrintMessage(f"Conputer name: {HOSTNAME}", LogOnly=True)
PrintMessage(f"Environment: {ENVIRONMENT}", LogOnly=True)
PrintMessage(f"Location: {LOCATION}", LogOnly=True)
#  =================== Start Script ===================



#  ==================== End Script ====================
PrintMessage(END_SCRIPT_MESSAGE, LogOnly=True)