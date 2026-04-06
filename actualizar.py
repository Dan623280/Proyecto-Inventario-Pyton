
# Lista inventario
from Lista import Inventario_Dict

# importa las funciones de error al ingresar dato
from Funciones_error import error_string,error_number_int, error_number_float

#Mostrar Datos
from Mostrar import Mostrar

# importa la utenticacion de un elemento para ver si se encuentra en la lista
from autenticacion import autenticacion_indice

#Traer colores
from  Color import rojo, reset, verde

#------------------------------
# Actualizar
#------------------------------

def actualizar():

    """
    Actualiza la información de un producto existente en el inventario.

    Descripción:
    Esta función permite modificar los datos de un producto previamente
    registrado, identificándolo mediante su índice. El usuario puede cambiar
    el nombre, el precio unitario y la cantidad disponible del producto.

    Proceso:
    1. Muestra un mensaje indicando la acción a realizar.
    2. Presenta el inventario actual con sus índices.
    3. Solicita un índice válido del producto a actualizar.
    4. Solicita los nuevos datos (nombre, precio y cantidad).
    5. Valida cada entrada mediante funciones auxiliares.
    6. Actualiza la información del producto en el inventario.
    7. Muestra un mensaje de confirmación.

    Parámetros:
    No recibe parámetros.

    Retorna:
    No retorna ningún valor. Los cambios se aplican directamente al inventario.

    Notas:
    - Depende de funciones de validación para garantizar datos correctos.
    - El inventario está estructurado como una lista de diccionarios.
    - Cada producto contiene las claves: 'Nombre', 'Precio' y 'Cantidad'.
    - El índice es fundamental para identificar el producto dentro de la lista.
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
    
# para llamar
# from actualizar import actualizar