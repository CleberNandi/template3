# encoding: utf-8
from time import strftime

__version__ = "01.20201126.01"

def GetDateTime():
    return strftime("%Y%m%d-%H%M")