# Lista inventario
from Lista import Inventario_Dict

# importa las funciones de error al ingresar dato
from funciones_secundarias.Funciones_error import error_number_int, error_string

#Traer colores
from funciones_secundarias.Color import rojo, reset, verde

#------------------------------
# Autenticacion
#------------------------------

def autenticacion(valor):
    """
    Verifica si un nombre ya existe dentro del inventario.

    Parámetros:
    valor (str): Nombre a buscar.

    Retorna:
    str: Retorna el nombre si existe en el inventario.
    None: Si no se encuentra el nombre.
    """
    for elemento in Inventario_Dict:
        
        # Compara el nombre ingresado con cada producto
        if elemento['Nombre'] == valor:
            return valor  # Si lo encuentra, lo retorna

#------------------------------
# autenticacion Nombre
#------------------------------

def autenticacion_nombre(var):
    """
    Solicita un nombre al usuario y valida que NO exista en el inventario.

    Si el nombre ya existe, muestra un mensaje de error y vuelve a pedirlo.

    Parámetros:
    var (str): Mensaje que se le muestra al usuario al pedir el nombre.

    Retorna:
    str: Nombre válido (que no existe previamente en el inventario).
    """
    while True:
        # Solicita el nombre al usuario
        nombre = error_string(f"{var}")

        cantidad = 0  # Contador de coincidencias

        # Recorre el inventario buscando coincidencias
        for elemento in Inventario_Dict:
            
            if elemento['Nombre'] == nombre:
                cantidad += 1

        # Si el nombre ya existe, muestra error
        if cantidad == 1:
            print(rojo + "===================================================")
            print("= El nombre ya existe, coloque un nombre diferente =")
            print("===================================================" + reset)
        else:
            # Si no existe, lo retorna como válido
            return nombre


#------------------------------
# autenticacion Indice
#------------------------------

def autenticacion_indice():
    """
    Solicita un índice al usuario y valida que exista dentro del inventario.

    Si el inventario está vacío o el índice no existe, muestra un error.

    Retorna:
    int: Índice válido dentro del inventario.
    """
    while True:
        # Solicita el índice al usuario
        numero = error_number_int("Indice: ")

        # Verifica si el inventario está vacío
        if len(Inventario_Dict) == 0:
            print(verde + "=================================")
            print("= No hay datos en el inventario =")
            print("=================================" + reset)
        else:
            
            # Obtiene el último índice válido del inventario
            var_indice = len(Inventario_Dict) - 1

            # Verifica si el índice ingresado es válido
            if 0 <= numero <= var_indice:
                return numero
            else:
                print(rojo + "====================")
                print("= Índice no existe =")
                print("====================" + reset)

# para llamar             
# from autenticacion import autenticacion_indice, autenticacion, autenticacion_nombre