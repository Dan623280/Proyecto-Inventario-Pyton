#Mostrar Datos
from services.Mostrar import Mostrar

# importa la utenticacion de un elemento para ver si se encuentra en la lista
from funciones_secundarias.autenticacion import autenticacion_indice

# Lista inventario
from Lista import Inventario_Dict

#Traer colores
from funciones_secundarias.Color import verde, reset, rojo

#------------------------------
# Eliminar
#------------------------------

def eliminar():
    """
    Elimina un producto del inventario utilizando su índice.

    Flujo de la función:
    1. Verifica si el inventario está vacío.
    2. Muestra un mensaje indicando al usuario qué debe hacer.
    3. Muestra el inventario actual (para que el usuario vea los índices).
    4. Solicita un índice válido mediante la función de autenticación.
    5. Elimina el producto correspondiente a ese índice.
    6. Muestra un mensaje de confirmación.
    """

    # -------------------------------------------------
    # Validación: verificar si el inventario está vacío
    # -------------------------------------------------
    if len(Inventario_Dict) == 0:
        print(rojo + "=================================")
        print("= No hay datos para eliminar    =")
        print("=================================" + reset)
        return  # Sale de la función si no hay datos

    # Espacio visual
    print("")
    print("Coloque el índice del producto que quiere eliminar")
    print("")

    # Mostrar inventario actual
    Mostrar()

    print("")

    # Solicitar y validar índice
    indice = autenticacion_indice()

    # Eliminar producto
    Inventario_Dict.pop(indice)

    # Mensaje de confirmación
    print(verde + "==================================")
    print("= Índice eliminado correctamente =")
    print("==================================" + reset)

# para llamar
# from Eliminar import eliminar


