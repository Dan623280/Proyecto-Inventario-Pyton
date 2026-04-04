from Lista import Inventario_Dict

from Funciones_error import error_string,error_number_int, error_number_float

from Mostrar import Mostrar

from autenticacion import autenticacion_indice

from  Color import rojo, reset, verde

def actualizar():

    """
    Esta funcion Verific los datos y si pasa la verificacion actualiza los datos
    """
    print("")
    print("Coloque el indice del producto que quiere actualizar")
    print("")

    Mostrar()

    print("")

    indice = autenticacion_indice()

    # Nombre del producto
    nombre = error_string("nuevo nombre del Producto: ")
    
    # Precio unitario
    precio = error_number_float("nuevo precio unitario del Producto: ")
    
    # Cantidad de productos
    cantidad = error_number_int("nueva cantidad del Producto: ")
    
    #Actualizar inventario
    Inventario_Dict[indice]['Nombre'] = nombre
    Inventario_Dict[indice]['Precio'] = precio
    Inventario_Dict[indice]['Cantidad'] = cantidad
    
    #Mostrar mensaje de salida
    print(verde+ "====================================")
    print("= Datos actualizados Correctamente =")
    print("===================================="+reset)   
    
