


#-------------------------------------------------
# Agregar Producto
#-------------------------------------------------

from Registro import Agregar_Producto

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

#-------------------------------------------------
# Mostar datos de la lista
#-------------------------------------------------

from Mostrar import Mostrar

"""
    Muestra en consola todos los productos almacenados en el inventario.

    Descripción:
    Esta función recorre la lista del inventario y presenta cada producto
    junto con su índice, nombre, precio y cantidad disponible. El índice
    mostrado permite al usuario identificar la posición del producto para
    operaciones posteriores como actualizar o eliminar.

    Comportamiento:
    - Si el inventario está vacío, muestra un mensaje indicando que no hay datos.
    - Si existen productos, los lista en formato ordenado con su respectivo índice.

    Parámetros:
    No recibe parámetros.

    Retorna:
    No retorna ningún valor. La información se muestra directamente en consola.

    Notas:
    - Utiliza la función enumerate() para generar los índices automáticamente.
    - El inventario debe estar estructurado como una lista de diccionarios.
    - Cada producto contiene las claves: 'Nombre', 'Precio' y 'Cantidad'.
    """

#------------------------------
# Buscar
#------------------------------

#importa la funcion para buscar
from Buscar import buscar

"""
    Busca un producto por su nombre dentro del inventario.

    - Si el producto existe, muestra sus datos (Nombre, Precio y Cantidad).
    - Si no existe, muestra un mensaje de error.
    """

#------------------------------
# Actualizar
#------------------------------

from actualizar import actualizar

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

#------------------------------
# Eliminar
#------------------------------
from Eliminar import eliminar

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

#------------------------------
# Calculo estadistica
#------------------------------

#importa la funcion de estadistica
from Estadisticas import calcular_estadisticas

"""
    Calcula y muestra estadísticas del inventario.

    Funcionalidades:
    - Calcula el total de unidades disponibles en el inventario.
    - Calcula el valor total del inventario (Precio * Cantidad).
    - Identifica el producto más caro.
    - Identifica el producto con mayor cantidad en stock.

    Retorna:
        dict | None:
            - Retorna un diccionario con las estadísticas si hay datos.
            - Retorna None si el inventario está vacío.
    """




