#Traer colores
from Color import rojo, reset, verde

#Mostrar menu y pedir Dato del menu
from Menu import menu_principal

#Guardar Registro
from Registro import Agregar_Producto

#Mostrar Datos
from Mostrar import Mostrar

#importa la funcion de estadistica
from Estadisticas import Estadistica

#importa la funcion para buscar
from Buscar import buscar

#importar actualizar producto
from actualizar import actualizar

from Eliminar import eliminar

#variable de confirmacion
confirmo = "Y"

#mientras que la confirmacion sea verdadera
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
        
        #Ejecuta la funcion Buscar producto
        buscar()

    elif numero == 4:
        
        #Ejecuta la funcion actualizar producto
        actualizar()

    elif numero == 5:
        
        #Ejecuta la funcion actualizar producto
        eliminar()

    elif numero == 6:

        #ejecuta la funcion de estadisticas
        Estadistica()

    #En desarrollo
    elif numero == 7:

        print("En desarrollo")
    
    #En desarrollo
    elif numero == 8:

        print("En desarrollo")

    elif numero == 9:

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

