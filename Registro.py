
#Importar la lista donde estan los productos
from Lista import Inventario_Dict

#Trae la Funciones que verifican si los datos son correctos
from Funciones_error import error_string, error_number_int, error_number_float

# Trae las variables de los colores
from Color import azul, reset

#-------------------------------------------------
# Agregar Producto
#-------------------------------------------------

def Agregar_Producto():

    #-------------------------------------------------
    # MENSAJE DE BIENVENIDA
    #-------------------------------------------------

    print("")
    print(azul + "============================================================")
    print("== Bienvenido a nuestro Programa para registrar productos ==")
    print("============================================================" + reset)
    print("")


    #-------------------------------------------------
    # SOLICITAR DATOS DEL PRODUCTO
    #-------------------------------------------------

    # Nombre del producto
    nombre = error_string("nombre del Producto: ")

    # Precio unitario
    precio = error_number_float("precio unitario del Producto: ")

    # Cantidad de productos
    cantidad = error_number_int("cantidad del Producto: ")


    #-------------------------------------------------
    # CÁLCULO DEL COSTO TOTAL
    #-------------------------------------------------

    costo_total = precio * cantidad

    #-------------------------------------------------
    # Guardar en el Inventario     
    #-------------------------------------------------

    producto = {"Nombre": nombre,"Precio": precio, "Cantidad": cantidad}
    Inventario_Dict.append(producto)

    #-------------------------------------------------
    # MOSTRAR RESULTADOS
    #-------------------------------------------------

    print(azul+"")
    print("= Producto actualizado exitosamente =")
    print(f"Nombre del producto: {nombre}")
    print(f"Precio unitario: {precio}")
    print(f"Cantidad: {cantidad}")
    print(f"Total a pagar: {costo_total}")
    print("======================================" + reset)
    print("")

    # Esta funcion permite registrar un producto desde la terminal.
    # Solicita al usuario el nombre del producto, el precio unitario y la cantidad.
    # Luego calcula el costo total multiplicando el precio por la cantidad.
    # Finalmente muestra en pantalla la información del producto y el total.
    # Si el usuario introduce un valor no válido, el programa solicita nuevamente el dato.

# Pra llamar
# from Registro import Agregar_Producto