import core
import os


diccIncidentes = {"data":[]}

def LoadInfoIncidentes():
    global diccIncidentes
    if core.checkFile("incidentes.json"):
        diccIncidentes = core.LoadInfo("incidentes.json")
    else:
        core.crearInfo("incidentes.json", diccIncidentes)  

def RegisterIncidentes():
    os.system("clear")
    print('+','´~'*55,'+')
    print("|{:^20}{}{:^21}|".format(' ', 'REGISTRO EQUIPO', ' '))
    print('+','~'*55,'+')          
    id = len(di)    