from Lista import Inventario_Dict

from Funciones_error import error_string

from autenticacion import autenticacion

from  Color import rojo, reset

def buscar():

    valor = error_string("nombre de producto: ")

    confir = autenticacion(valor)

    if confir:
        
        for elemento in Inventario_Dict:

            if elemento['Nombre'] == confir:

                print("")
                print(f"Producto: {elemento['Nombre']}, Precio: {elemento['Precio']}, Cantidad: {elemento['Cantidad']}")
                print("")

    else:
        #Mostar mensaje del numero no valido
        print(rojo+"======================")
        print("= Producto no existe =")
        print("======================"+reset)



#from Buscar import buscar