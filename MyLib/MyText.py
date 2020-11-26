# encoding: utf-8
import os

from MyLib.MyMessage import PrintMessage

__version__ = "01.20201126.01"

def IsStrNoBlank(StrText):
    Result = False
    Text = StrText
    
    if Text and Text.strip():
        Result = True
    
    return Result

def ListFilesOnDir(StrDir):
    Dir = StrDir
    Files = []
    
    try:
        for file in os.listdir(Dir):
            FilenameFull = os.path.join(Dir, file)
            
            if os.path.isfile(FilenameFull):
                Files.append(FilenameFull)
    except Exception as ErrorFiles:
        PrintMessage(f"Falha ao listar arquivos. Erro: {ErrorFiles}")
    
    return Files
            