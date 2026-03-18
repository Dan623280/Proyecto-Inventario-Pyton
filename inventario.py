from Color import rojo, reset, verde

#Mostrar menu y pedir Dato del menu
from Menu import menu_principal

#Guardar Registro
from Registro import Agregar_Producto

#Mostrar Datos
from Mostrar import Mostrar

#importa la funcion de estadistica
from Estadisticas import Estadistica
confirmo = "Y"


while confirmo == "Y":

    # Traer el menu y pedir numero
    numero = menu_principal()

    #Verifica si el numero es 1
    if numero == 1:

        #Ejecuta la funcion agregar producto
        Agregar_Producto()

    elif numero == 2:
        #Ejecuta la funcion Mostrar producto
        Mostrar()

    elif numero == 3:

        #ejecuta la funcion de estadisticas
        Estadistica()

    elif numero == 4:

        #Mostrar mensaje de salida
        print(verde+"==================================================")
        print("=Salida exitosa Gracias por usar nuestro Programa=")
        print("=================================================="+reset)
        confirmo = "N"

    else:

        #Mostar mensaje del numero no valido
        print(rojo+ "==================")
        print("=Numero no valido=")
        print("=================="+reset)



