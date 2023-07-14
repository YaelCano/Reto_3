import core
import os
import trainer

diccIncidentes = {"data":[]}


def LoadInfoIncidentes():
    global diccIncidentes
    if core.checkFile("incidentes.json"):
        diccIncidentes = core.LoadInfo("incidentes.json")
    else:
        core.crearInfo("incidentes.json", diccIncidentes)


def mainMenu_1():
    os.system("clear")
    isActive = True
    print("\n--- Menu incidentes ---")
    print("1. Agregar incidente: ")
    print("2.")
    print("3.")
    print("4. Volver al menu principal:")
    opcion = int(input("=>"))
    
    
    if (opcion == 1):
        isActive =True
        print("1.leve\n2.moderada\n3.Critica")
        carte = int(input("Selecciona una opción:"))
        if (carte == 1):
            carte = "leve"
        elif (carte == 2):
            carte = "moderada"
        elif (carte == 3):
            carte = "critica"        
        dicctrainers = core.LoadInfo("trainers.json")
        
        data ={
            "categoria":carte,
            "id":input("Ingrese el id del incidente:"),
            "descripcion":input("Ingrese una descripcion sobre el incidente:"),
        }
        diccIncidentes["data"].append(data)
        core.crearInfo("incidentes.json",data)

    elif (opcion == 2):
        pass