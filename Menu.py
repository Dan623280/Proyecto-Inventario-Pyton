#importar colores
from Color import azul,reset

#llamar para detectar error
from Funciones_error import error_number_int

#-------------------------------------------------
# Menu
#-------------------------------------------------

def menu_principal():
    
    #Mostrar menu
    print(azul+"")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    print(""+reset)

    # Preguntar Opcion a elegir
    pregunta = error_number_int("el numero de la acción que desea realizar: ")
    print("")

    return pregunta


#Para llamar
#from Menu import menu_principal()
