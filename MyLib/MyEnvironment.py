# encoding: utf-8
import inspect
import os
import socket
import sys

ModuleFolder = os.path.realpath(os.path.dirname(inspect.getfile(inspect.currentframe())))
if ModuleFolder not in sys.path:
	sys.path.insert(0, ModuleFolder)

__version__ = "01.20201125.01"

def GetHostnameLong():
    return socket.getfqdn()

def GetShortHostname():
    Result = ""
    Hostname = socket.gethostname().upper()
    
    if Hostname.split("."):
        Result = Hostname.split(".")[0]
    
    return Result

def GetEnvironment(StrHostname):
    Result = "PD"
    ListTemp = StrHostname.split("-")
    
    if len(ListTemp) > 2:
        Result = ListTemp[1].upper()    
    elif StrHostname[:11] == "DOMINIO-APP" or StrHostname == "SRV-AD-A" or StrHostname == "SRV-AD-B":
        Result = "PD"
    
    return Result

def GetDCLocation(StrHostname):
    Result = "LCW"
    ListHostname = StrHostname.split("-")
    
    if StrHostname[:11] == 'DOMINIO-APP' or StrHostname == 'SRV-AD-A' or StrHostname == 'SRV-AD-B':
        Result = "SKY"
    elif len(ListHostname) > 2:
        Result = ListHostname[2].upper()
    else:
        Result = "LCW"
    
    return Result
    

def main():
    ...

if __name__ == "__main__":
    main()