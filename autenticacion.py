from Lista import Inventario_Dict

from Funciones_error import error_number_int, error_string

from Color import rojo, reset, verde


def autenticacion(valor):

    """Esta funcion verifica si el nombre ya existe"""
    for elemento in Inventario_Dict:

        if elemento['Nombre'] == valor:

            return valor

def autenticacion_nombre(var):

    """Verifica si existe el nombre y si el nombre no existe devuelve el nombre de lo contrario imprime mensaje de error"""
    while True:
            
        nombre = error_string(f"{var}")

        cantidad = 0

        for elemento in Inventario_Dict:

            if elemento['Nombre'] == nombre:
                cantidad = cantidad + 1

        if cantidad == 1:

            print(rojo + "===================================================")
            print("= El nombre ya existe coloque un nombre diferente =")
            print("===================================================" + reset)

        else:

            return nombre


        

def autenticacion_indice():

    """Autentica si el indice existe, si exciste devuelve el numero"""
    while True:

        numero = error_number_int("Indice: ")
        
        var_indice  = 0

        if len(Inventario_Dict) == 0:
            print(verde + "=================================")
            print("= no hay datos en el inventario =")
            print("=================================" + reset)
        
        else:
            
            for indice, valor in enumerate(Inventario_Dict):

                var_indice = indice

            if numero <= var_indice:

                return numero

            else:

                print(rojo + "====================")
                print("= Indice no existe =")
                print("====================" + reset)

    
