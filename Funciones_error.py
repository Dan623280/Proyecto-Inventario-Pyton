#importar colores
from Color import rojo, reset


# -------------------------------------------------
# VALIDACIONES DE ENTRADA DE DATOS
# -------------------------------------------------

# -------------------------------------------------
# Error String
# -------------------------------------------------
def error_string(var):
    """
    Valida que el dato ingresado por el usuario sea texto (string).

    Parámetros:
    var (str): Mensaje que se mostrará al usuario.

    Retorna:
    str: Texto ingresado por el usuario.
    """

    # Bucle infinito hasta que el usuario ingrese un valor válido
    while True:
        try:
            # Solicita el dato al usuario
            valor = input(f"{var}")
            
            # Retorna el valor ingresado (input siempre devuelve string)
            return valor

        except:
            # Captura cualquier error inesperado
            print(rojo + "Valor no válido, debe ser texto" + reset)

# -------------------------------------------------
# Error numero entero
# -------------------------------------------------

def error_number_int(var):
    """
    Valida que el dato ingresado por el usuario sea un número entero positivo.

    Parámetros:
    var (str): Nombre del dato que se le pedirá al usuario.

    Retorna:
    int: Número entero válido (mayor o igual a 0).
    """

    while True:
        try:
            # Solicita el dato y lo convierte a entero
            valor = int(input(f"Colocar {var}: "))

            # Verifica que no sea negativo
            if valor >= 0:
                return valor
            else:
                print(rojo + "Los valores negativos no son válidos" + reset)

        except:
            # Error si el usuario no ingresa un número entero
            print(rojo + "Valor no válido, debe ser un número entero" + reset)

# -------------------------------------------------
# Error numero flotante
# -------------------------------------------------

def error_number_float(var):
    """
    Valida que el dato ingresado por el usuario sea un número (decimal o entero)
    y que sea positivo.

    Parámetros:
    var (str): Nombre del dato que se le pedirá al usuario.

    Retorna:
    int: Número válido convertido a entero.
    """

    while True:
        try:
            # Solicita el dato y lo convierte a flotante
            valor = float(input(f"Colocar {var}: "))

            # Convierte el valor a entero (pierde decimales)
            valor = int(valor)

            # Verifica que no sea negativo
            if valor >= 0:
                return valor
            else:
                print(rojo + "Los valores negativos no son válidos" + reset)

        except:
            # Error si el usuario no ingresa un número válido
            print(rojo + "Valor no válido, debe ser un número" + reset)

#Para llamar  
#from Funciones_error import error_string, error_number_int, error_number_float


