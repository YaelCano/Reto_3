import os 
import core

dictTrainers ={"trainer":[]}

def LoadInfoTrainers():
    global dictTrainers
    if (core.checkFile("trainers.json")):
        dictTrainers = core.LoadInfo("trainers.json")
    else:
        core.crearInfo("trainers.json",dictTrainers)
def mainMenu():
    isCliRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^20}{}{:^21}|".format(' ','REGISTRO--TRAINERS',' '))
    print('+','-'*55,'+')
    print('+','-'*55,'+')
    print("1. Registro de trainers: ")
    print("2. Busqueda de trainers: ") 
    print("3. Editor de trainers: ")
    print("4. Eliminar trainers:")
    print("5. volver al menu principal:")
    opcion = int(input(":<"))

    if (opcion == 1):
        Block = False
        for i in dictTrainers["trainer"]:
            Block = True
            consecutivo = i["id"]
        if Block == True:    
            idactual = int(consecutivo)+1
            idAgregar = str(idactual).zfill(3)
        if Block  == False:
            idAgregar="001"    
            print(idAgregar)
        trainer = {
            "id": idAgregar,
            "nombre":input("Ingrese el nombre de trainer: "),
            "email_personal":input("Ingrese el email personal: "),
            "email_corporativo":input("Ingrese el email corporativo:"),
            "telefono_movil":input("Ingrese el telefono movil:"),
            "telefono_residencia":input("Ingrese el telefono residencial:"),
            "telefono_empresa":input("Ingrese el telefono empresa: "),
            "telefono_movilEmpresarial":input("Ingrese el telefono empresarial:")
        }
        dictTrainers["trainer"].append(trainer)
        core.crearInfo("trainers.json",trainer)           

    if (opcion == 2 ):
        print('+','-'*55,'+')
        print("|{:^16}{}{:^20}|".format(' ','BUSCADOR DE TRAINERS',' '))
        print('+','-'*55,'+')
        codBusq = input("Ingrese el codigo del trainer a buscar: ")
        for i,item in enumerate(dictTrainers["trainer"]):
            if codBusq in item["id"]:
                print(f'Id del Trainer: {item["id"]}')
                print(f'Nombre del Trainer: {item["nombre"]}')
                print(f'email personal: {item["email_personal"]}')
                print(f'email coporativo: {item["email_corporativo"]}')
                print(f'Telefono movil: {item["telefono_movil"]}')
                print(f'Telefono residencial: {item["telefono_residencia"]}')
                print(f'Telefono de la empresa: {item["telefono_empresa"]}')
                print(f'Telefono movil empresarial: {item["telefono_movilEmpresarial"]}')            
            input("presione enter para continuar...")
    if (opcion == 3):
        print('+','-'*55,'+')
        print("|{:^16}{}{:^15}|".format(' ','EDICION DE TRAINERS: ',' '))
        print('+','-'*55,'+')
        codBusq = input("Ingrese el codigo del trainers :")
        for i,item in enumerate(dictTrainers["trainer"]):
            if codBusq in item["id"]:
                item["nombre"] = input("Ingrese el nuevo nombre o presione enter para omitir: ") or item["nombre"]
                item["email_personal"] = input("Ingrese el nuevo email personal o presione enter para omitir") or item["email_personal"]
                item["email_corporativo"] = input("Ingrese el nuevo email corporativo o presione enter para omitir") or item["email_corporativo"]
                item["telefono_movil"] = input("Ingrese el nuevo telefono o presione enter para omitir") or item["telefono_movil"]
                item["telefono_residencia"] = input("Ingrese el nuevo telefono residencia o presione enter para omitir") or item["telefono_residencia"]
                item["telefono_empresa"] = input("Ingrese el nuevo telefono empresa o presione enter para omitir") or item["telefono_empresa"]
                item["telefono_movilEmpresarial"]= input("Ingrese el nuevo telefono empresarial o presione enter para omitir") or item["telefono_movilEmpresarial"]
                core.editInfo("trainers.json")
            input("presione enter para continuar...____")
    elif (opcion == 4):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','ELIMINACIÓN DEL TRAINER',' '))
        print('+','-'*49,'+')
        codElim = input("Ingrese el codigo del trainer a buscar: ")
        for i,item in enumerate(dictTrainers["trainer"]):
            if codElim == item["id"]:
                dictTrainers["trainer"].pop(i)
                core.editInfo("trainers.json",dictTrainers)
                input("Presione enter para continuar....")

    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        mainMenu()                  