# Importar lista donde se van a guardar los datos
from Lista import Inventario_Dict

#importar colores
from Color import rojo, reset

#-------------------------------------------------
# Mostar datos de la lista
#-------------------------------------------------

def Mostrar():

    #Vericar que el inventario tenga datos
    if len(Inventario_Dict) == 0:

        #imprimir mensaje de inventario vacio
        print(rojo+"==================")
        print("=Inventario Vacio=")
        print("=================="+reset)

    else:

        #recorrer Lista
        for indice,elemento in enumerate(Inventario_Dict):

            #recorrer producto
            print(f"Indice: {indice}, Producto: {elemento['Nombre']}, Precio: {elemento['Precio']}, Cantidad: {elemento['Cantidad']}")

    
# Para llamar
# from funcionesCRUD.Mostrar import Mostrar
