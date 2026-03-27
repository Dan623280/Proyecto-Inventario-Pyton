#importar colores
from Color import rojo, reset

#-------------------------------------------------
# FUNCIONES PARA VALIDAR DATOS
#-------------------------------------------------

# Función para validar texto
def error_string(var):

    #inicio del ciclo
    while True:
        
        try:

            valor = input(f"{var}")
            return valor
        
        except:

            print(rojo + "Valor no válido, debe ser texto" + reset)


# Función para validar números enteros
def error_number_int(var):

    #inicio del ciclo
    while True:

        try:

            valor = int(input(f"Colocar {var}"))
            
            if valor >= 0:

                return valor
            
            else:

                print(rojo + "Los valores negativos no son válidos" + reset)
                
        except:

            print(rojo + "Valor no válido, debe ser un número entero" + reset)


# Función para validar números decimales
def error_number_float(var):
    #inicio del ciclo
    while True:

        try:

            valor = float(input(f"Colocar {var}"))
            valor = int(valor)

            if valor >= 0:

                return valor
            
            else:

                print(rojo + "Los valores negativos no son válidos" + reset)
                
        except:

            print(rojo + "Valor no válido, debe ser un número" + reset)

#Para llamar  
#from Funciones_error import error_string, error_number_int, error_number_float


