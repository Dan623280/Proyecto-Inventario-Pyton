
from Lista import Inventario_Dict

from Funciones_error import error_string

from Color import rojo, reset

import csv

def Valor():

    
    while True:

        valor = error_string("¿Sobrescribir inventario actual? (S/N): ")

        if valor == "S" or valor == "N" :

            return valor
        
        else:

            print(rojo+"IOpcion no valido"+ reset)
        
    

            


def cargar():
    nombres = []

    for elemento in Inventario_Dict:

        nombres.append(elemento['Nombre'])

    valor = Valor()

    if valor == "S":

        with open('inventario.csv', mode='r', newline='', encoding='utf-8') as file:
        
            reader = csv.DictReader(file)
        
            for row in reader:
            
                if row['Nombre'] in nombres:
                    
                    for elemento in Inventario_Dict:
                    
                        
                    
                    
                        
                else:
                
                    Inventario_Dict.append(row) 
    else:

