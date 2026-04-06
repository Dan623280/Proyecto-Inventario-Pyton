
# Importar la lista donde estan los productos
from Lista import Inventario_Dict

# Trae la Funciones que verifican si los datos son correctos
from funciones_secundarias.Funciones_error import error_string, error_number_int, error_number_float

# Trae las variables de los colores
from funciones_secundarias.Color import azul, reset

from funciones_secundarias.autenticacion import autenticacion_nombre


#-------------------------------------------------
# Agregar Producto
#-------------------------------------------------

def Agregar_Producto():

    """
    Registra un nuevo producto en el inventario.

    Descripción:
    Esta función permite al usuario ingresar un producto desde la terminal,
    solicitando su nombre, precio unitario y cantidad disponible. El sistema
    valida cada entrada utilizando funciones auxiliares para asegurar que los
    datos sean correctos (nombre único, valores numéricos positivos, etc.).

    Proceso:
    1. Muestra un mensaje de bienvenida.
    2. Solicita el nombre del producto (validando que no exista previamente).
    3. Solicita el precio unitario (número positivo).
    4. Solicita la cantidad disponible (entero positivo).
    5. Calcula el costo total (precio * cantidad).
    6. Guarda el producto en la estructura de datos del inventario.
    7. Muestra un resumen del producto registrado.

    Parámetros:
    No recibe parámetros.

    Retorna:
    No retorna ningún valor. La información se almacena directamente en el inventario.

    Notas:
    - Utiliza funciones de validación para evitar errores en la entrada de datos.
    - El inventario se gestiona mediante una lista de diccionarios.
    - Cada producto contiene las claves: 'Nombre', 'Precio' y 'Cantidad'.
    """
    # MENSAJE DE BIENVENIDA

    print("")
    print(azul + "============================================================")
    print("== Bienvenido a nuestro Programa para registrar productos ==")
    print("============================================================" + reset)
    print("")


    # SOLICITAR DATOS DEL PRODUCTO

    # Nombre del producto
    nombre = autenticacion_nombre("nombre del producto: ")

    # Precio unitario
    precio = error_number_float("precio unitario del Producto: ")

    # Cantidad de productos
    cantidad = error_number_int("cantidad del Producto: ")


    # Calculo del costo total

    costo_total = precio * cantidad


    # Guardar en el Inventario     

    producto = {"Nombre": nombre,"Precio": precio, "Cantidad": cantidad}
    
    Inventario_Dict.append(producto)


    # MOSTRAR RESULTADOS

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