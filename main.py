import os
import trainer


if __name__ == '__main__':
    isActive = True
    opcion = 0
    while isActive:
        os.system("clear")
        
        print('+','-'*55,'+')
        print("|{:^20}{}{:^23}|".format(' ','MENU---PRINCIPAL',' '))
        print('+','-'*55,'+')
        print('+','-'*55,'+')
        print("|{:^20}{}{:^28}|".format(' ','CAMPUSLANDS',' '))
        print('+','-'*55,'+')
        print("1. Registro de trainer: ")
        print("2. Registro de equipos:") 
        print("3. Registro de incidencias: ")
        print("4. Salir de programa:")
        opcion = int(input(":<"))
        if (opcion == 1):
            trainer.LoadInfoTrainers()
            trainer.mainMenu()
        elif (opcion == 2):
            pass
        elif (opcion == 3):
            pass
        elif (opcion == 4):
            isActive = False
            print("Adios de programa--------------------------------")
        else:
            print("Općion no valida....")
            input("presione enter para continuar...") 