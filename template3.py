# -*- utf-8 -*-
import os
import sys

from winreg import HKEY_LOCAL_MACHINE, REG_SZ

from my_lib.my_message import print_message
from my_lib.my_text import ListFilesOnDir
from my_lib.my_email import SendEmail, SendEmailInfo, SendEmailWarnig, SendEmailError, SendEmailGmail
from my_lib.my_regedit import connect_root_key, search_registry_way, setKeyReg

from my_lib.my_constants import START_SCRIPT_MESSAGE, END_SCRIPT_MESSAGE, HOSTNAME, ENVIRONMENT, LOCATION
from my_lib.my_constants import ROOT_PATH, MODULE_PATH, SCRIPT_FRIENDLYNAME, VERSION_APP

__version__ = VERSION_APP

#  ================= Variables Globals ================

#  ==================== Start Loggin ==================
print_message(START_SCRIPT_MESSAGE, LogOnly=True)

print_message(f"Script version: {__version__}", LogOnly=True)
print_message(f"Conputer name: {HOSTNAME}", LogOnly=True)
print_message(f"Environment: {ENVIRONMENT}", LogOnly=True)
print_message(f"Location: {LOCATION}", LogOnly=True)
#  =================== Start Script ===================

root_key = connect_root_key(HKEY_LOCAL_MACHINE)
path_key = r'SOFTWARE\WOW6432Node\Classes\CLSID'
key_path_list = []
key_value_data = r"C:\Dominio\Contabil\101c.00.B\Utilitários\MailBee.dll"

search_registry_way(root_key, path_key, key_path_list, search_key="InprocServer32", search_value="MailBee.dll")

for key in key_path_list:
    setKeyReg(root_key, key, "", REG_SZ, key_value_data)


#  ==================== End Script ====================
print_message(END_SCRIPT_MESSAGE, LogOnly=True)