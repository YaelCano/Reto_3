import os
import trainer
import equipos
import incidentes


if __name__ == '__main__':
    isActive = True
    opcion = 0
    while isActive:
        os.system("clear")
        
        print('+','-'*55,'+')
        print("|{:^20}{}{:^21}|".format(' ','MENU---PRINCIPAL',' '))
        print('+','-'*55,'+')
        print('+','-'*55,'+')
        print("|{:^20}{}{:^26}|".format(' ','CAMPUSLANDS',' '))
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
            equipos.LoadInfoEquipos
            equipos.RegEquipos()
        elif (opcion == 3):
            incidentes.LoadInfoIncidentes
            incidentes.mainMenu_1()
        elif (opcion == 4):
            isActive = False
            print("Adios de programa--------------------------------")
        else:
            print("Općion no valida....")
            input("presione enter para continuar...") 