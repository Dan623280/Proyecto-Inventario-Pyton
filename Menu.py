#importar colores
from funciones_secundarias.Color import azul,reset

#llamar para detectar error
from funciones_secundarias.Funciones_error import error_number_int

#-------------------------------------------------
# Menu
#-------------------------------------------------

def menu_principal():
    
    """Este muestra el menu y pide al usuario que elija una opcion luego retorna esa opcion"""
    #Mostrar menu
    print(azul + "")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar Producto")
    print("4. Actualizar Producto")
    print("5. Eliminar Producto")
    print("6. Calcular estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")
    print("" + reset)

    # Preguntar Opcion a elegir
    pregunta = error_number_int("el numero de la acción que desea realizar: ")
    print("")

    return pregunta


#Para llamar
#from Menu import menu_principal()
