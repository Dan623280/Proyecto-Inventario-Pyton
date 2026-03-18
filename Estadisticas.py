#Importar la lista donde estan los productos
from Lista import Inventario_Dict

#importar colores
from Color import rojo, reset, verde

#-------------------------------------------------
# Estadisticas
#-------------------------------------------------

#Vericar que el inventario tenga datos
def Estadistica():

    #verifica si el inventario no tiene elementos
    if len(Inventario_Dict) == 0:

        print(rojo+"==================")
        print("=Inventario Vacio=")
        print("=================="+reset)

    else:

        #calcula valor total
        Valor_Total = 0

        #Recorre la lista
        for elemento in Inventario_Dict:

            #calcula el valor total
            Valor_Total = Valor_Total + (elemento['Precio'] * elemento['Cantidad'])
            
        #imprime el valor total y la cantidad
        print(verde+"")
        print(f"El valor total del inventario es {Valor_Total}")
        print(f"La Cantidad de Productos registrados del inventario es: {len(Inventario_Dict)}")
        print(""+reset)