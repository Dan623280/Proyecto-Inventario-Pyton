#Mostrar Datos
from Mostrar import Mostrar

from autenticacion import autenticacion_indice

from Lista import Inventario_Dict

from Color import verde, reset

def eliminar():

    """Esta funcion pide un indice y elimina los datos segun el indice"""
    print("")
    print("Coloque el indice del producto que quiere Eliminar")
    print("")

    Mostrar()

    print("")
    
    indice = autenticacion_indice()

    Inventario_Dict.pop(indice)

    print(verde + "==================================")
    print("= Indice Eliminado Correctamente =")
    print("==================================" + reset)



