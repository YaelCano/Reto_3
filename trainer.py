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
    os.system("clear")
    print("\n----menu---de---Registro---trainers----")
    print("1. Registro de trainers: ")
    print("2. Busqueda de trainers: ") 
    print("3. Editor de trainers: ")
    print("4. volver al menu pricipa: ")
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
        print("|{:^16}{}{:^15}|".format(' ','BUSCADOR DE TRAINERS',' '))
        print('+','-'*55,'+')
        codBusq = input("Ingrese el codigo del trainer a buscar: ")
        for i,item in enumerate(dictTrainers["trainer"]):
            if codBusq in item["id"]:
                print(f'Id del Trainer: {item["id"]}')
                print(f'Nombre del Trainer: {item["nombre"]}')
                print(f'email personal: {item["email_personal"]}')
                print(f'email coporativo: {item["email_corporativo"]}')
                print(f'Telefono corporativo: {item["telefono_movil"]}')
                print(f'Telefono movil: {item["telefono_movil"]}')
                print(f'Telefono residencial: {item["telefono_residencia"]}')
                print(f'Telefono de la empresa: {item["telefono_empresa"]}')
                print(f'Telefono movil empresarial: {item["telefono_movilEmpresarial"]}')            
            input("presione enter para continuar...")
    elif (opcion == 3):
        pass  
    elif (opcion == 4):
        pass       