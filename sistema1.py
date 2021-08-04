#Programing by David Ezequeil Monteros Folguera 3/08/2021
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'        
    os.system(command)



#---------- menu principal
Codigo = []
Nombre = []
Puesto = []
Telefono = []

CodigoR = open("Codigo.txt","r")
NombreR = open("Nombre.txt","r")
PuestoR = open("Puesto.txt","r")
TelefonoR = open("Telefono.txt","r")


for cr in CodigoR.readline().split(","):
    if cr != "":
        Codigo.append(cr)
for nr in NombreR.readline().split(","):
    if nr != "":
        Nombre.append(nr)
for pr in PuestoR.readline().split(","):
    if pr != "":
        Puesto.append(pr)
for tr in TelefonoR.readline().split(","):
    if tr != "":
        Telefono.append(int(tr))                        
        


CodigoR.close()
NombreR.close()
PuestoR.close()
TelefonoR.close()

clearConsole()
menuprincipal = int(input("1Menu Principal: \n 1- ver planilla \n 2- insertar persona \n 3- eliminar persona \n 4- modificar persona \n 5-change interfaz \n 0- salir \n"))
while menuprincipal != 0:
    clearConsole()
    if menuprincipal == 1:
        clearConsole()
        print("----------------------------------------------------------------------------------")
        print("Corigo |  Nombre                |   Puesto               | Telefono             ")
        for x in range(len(Codigo)):
            print(Codigo[x],"              ",Nombre[x],"              ",Puesto[x],"              ",Telefono[x])
        print("----------------------------------------------------------------------------------")
        print("")
        print("")
                    
    elif menuprincipal == 2:
        clearConsole()
        print("-----------INGRESO DE PERSONAS--------------")
        print("")
        print("")
        print("llena los siguientes datos: ")
        Codigo.append(input("Codigo de la persona: "))
        Nombre.append(input("Nombre de la persona: "))
        Puesto.append(input("Puesto de la persona: "))
        Telefono.append(int(input("Telefono de la persona: ")))
        print("")
        print("-----------PERSONA INGRESADA--------------")
        print("")
        input("")
          
        clearConsole()
        
    elif menuprincipal == 3:
        
        clearConsole()
        print("-----------ELIMINACION DE PERSONAS--------------")
        print("")
        print("")
        cod = input("Ingresa el codigo a eliminar: ")
        for i in range(len(Codigo)-1,-1,-1):
            if Codigo[i] == cod:
                Codigo.pop(i)
                Nombre.pop(i)
                Telefono.pop(i)
                Puesto.pop(i)
        print("")
        print("-----------PERSONA ELIMINADA--------------")
        print("")
        input("")
        clearConsole()
        
        
                
        
        
        
    elif menuprincipal == 4:
        
        clearConsole()
        print("-----------MODIFICACION DE PERSONAS--------------")
        print("")
        print("")
        cod = input("Ingresa el codigo a modificar: ")
        
        for x in range(len(Codigo)-1,-1,-1):
            if Codigo[x] == cod:
                Nombre[x] = input("Cual es el nuevo nombre: ")
                Puesto[x] = input("Cual es el nuevo puesto: ")
                Telefono[x] = int(input("Cual es el nuevo telefono: "))
                 
        print("")
        print("-----------PERSONA MODIFICADA--------------")
        print("")
        input("")
        clearConsole()        
                
    elif menuprincipal == 5:
        
        clearConsole()
        print("-----------CAMBIAR INTERFAZ GRAFICA--------------")
        print("")
        print("")
        
        igrafica = int(input("escoja una nueva interfaz grafica: \n 1-dark  \n 2-lihgt  \n 3-hacker  \n 0-salir \n "))
    
        while igrafica != 0:
            
            
            
            if igrafica == 1:
                os.system("color 0f")
                igrafica = 0    
                print("")
                print("-----------INTERFAZ GRAFICA DARK--------------")
                print("")
                input("")
                clearConsole()
        
            elif igrafica == 2:
                os.system("color f1")
                igrafica = 0    
                print("")
                print("-----------INTERFAZ GRAFICA LIGHT--------------")
                print("")
                input("")
                clearConsole()
            elif igrafica == 3:
                os.system("color 0a")
                igrafica = 0                
                print("")
                print("-----------INTERFAZ GRAFICA HACKER--------------")
                print("")
                input("")
                clearConsole()
            else: 
                clearConsole()
                print("opcion invalidad intente nuevamente")
                input("")
                clearConsole()   
                
                             
            igrafica = int(input("2Escoja una nueva interfaz grafica: \n 1-dark  \n 2-lihgt  \n 3-hacker  \n 0-salir \n "))
                                                      
    else:
        clearConsole() 
        print("")
        print("-----------OPCION NO VALIDAD INTENTE NUEVAMENTE--------------")
        print("")
        input("")
        clearConsole() 
        
      
    menuprincipal = int(input("2Menu Principal: \n 1- ver planilla \n 2- insertar persona \n 3- eliminar persona \n 4- modificar persona \n 5-change interfaz \n 0- salir \n"))

CodigoT = open("Codigo.txt","w")    
NombreT = open("Nombre.txt","w")    
PuestoT = open("Puesto.txt","w")    
TelefonoT = open("Telefono.txt","w")  
  
for x in range(len(Codigo)):
    CodigoT.write(Codigo[x]+",")
    NombreT.write(Nombre[x]+",")
    PuestoT.write(Puesto[x]+",")
    TelefonoT.write(str(Telefono[x])+",")
    
CodigoT.close()
NombreT.close()
PuestoT.close()
TelefonoT.close()


