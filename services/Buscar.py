# Lista inventario
from Lista import Inventario_Dict

# importa las funciones de error al ingresar dato
from funciones_secundarias.Funciones_error import error_string

# importa la utenticacion de un elemento para ver si se encuentra en la lista
from funciones_secundarias.autenticacion import autenticacion

#Traer colores
from  funciones_secundarias.Color import rojo, reset

#------------------------------
# Buscar
#------------------------------

def buscar():
    """
    Busca un producto por su nombre dentro del inventario.

    - Si el producto existe, muestra sus datos (Nombre, Precio y Cantidad).
    - Si no existe, muestra un mensaje de error.
    """

    # Solicita al usuario el nombre del producto
    valor = error_string("Nombre de producto: ")

    # Verifica si el producto existe usando la función de autenticación
    confir = autenticacion(valor)

    # Si el producto existe
    if confir:
        
        for elemento in Inventario_Dict:

            # Busca el producto dentro del inventario
            if elemento['Nombre'] == confir:

                # Muestra la información del producto
                print("")
                print(f"Producto: {elemento['Nombre']}, Precio: {elemento['Precio']}, Cantidad: {elemento['Cantidad']}")
                print("")
    else:
        # Muestra mensaje de error si el producto no existe
        print(rojo + "======================")
        print("= Producto no existe =")
        print("======================" + reset)

# para llamar
# from Buscar import buscar