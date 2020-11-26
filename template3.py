# encoding: utf-8
import os

from MyLib.MyPath import RootPath
from MyLib.MyMessage import PrintMessage
from MyLib.MyText import ListFilesOnDir
from MyLib.MyEmail import SendEmail, SendEmailInfo, SendEmailWarnig, SendEmailError, SendEmailGmail

from MyLib.MyConstants import START_SCRIPT_MESSAGE, END_SCRIPT_MESSAGE, HOSTNAME, ENVIRONMENT, LOCATION

__version__ = "01.20201125.01"

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