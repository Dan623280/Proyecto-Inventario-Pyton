
from Lista import Inventario_Dict

from Funciones_error import error_string

from Color import rojo, reset, verde


import csv


def Valor():
    """l e pregunta al usuario si desea sobre escribir ls datos verifica el valor que coloca el usuario y lo retorna"""
    while True:

        valor = error_string("¿Sobrescribir inventario actual? (S/N): ")

        if valor == "S" or valor == "N" :

            return valor
        
        else:

            print(rojo+"Opcion no valido"+ reset)
        
    

def cargar():
    
    """Carga los datos dependiendiendo de el valor que coloque el usuario"""
    
    valor = Valor()

    if valor == "S":

        Inventario_Dict.clear()
        
        with open("inventario.csv", mode="r", encoding="utf-8") as file:
            
            reader = csv.DictReader(file)

            for fila in reader:
                
                fila["Precio"] = int(fila["Precio"])
                fila["Cantidad"] = int(fila["Cantidad"])
                
                Inventario_Dict.append(fila)
                
        print(verde+"================================")
        print("= Datos Cargados correctamente =")
        print("================================"+reset)
        
    else:

        
        with open("inventario.csv", mode="r", encoding="utf-8") as file:
            
                
            lista_nueva = []
            
            reader = csv.DictReader(file)


            for fila in reader:
                        
                for elemento in Inventario_Dict:
                    
                    if elemento['Nombre'] == fila["Nombre"]:
                    
                        fila["Precio"] = elemento['Precio']
                        fila["Cantidad"] = int(fila["Cantidad"]) + elemento['Cantidad']
                    
                lista_nueva.append(fila)    
        Inventario_Dict.clear()
        Inventario_Dict.extend(lista_nueva)
        print(verde+"================================")
        print("= Datos Cargados correctamente =")
        print("================================"+reset)
