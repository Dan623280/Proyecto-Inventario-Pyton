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
        cantidades = 0
        precio_mas_alto = 0
        cantidad_mas_alta = 0
        #Recorre la lista
        for elemento in Inventario_Dict:

            #calcula el valor total
            Valor_Total = Valor_Total + (elemento['Precio'] * elemento['Cantidad'])

            #añadir cantidad
            cantidades = cantidades + elemento['Cantidad']

            #añadir precio mas alto
            if elemento['Precio'] > precio_mas_alto:

                precio_mas_alto = elemento['Precio'] 

          
            
            print("cantidad", cantidad_mas_alta)
            #añadir cantidad mas alta
            if cantidad_mas_alta < elemento['Cantidad']:
                print(cantidad_mas_alta)
                cantidad_mas_alta = elemento['Cantidad'] 

            
            


        print("cantidad mas alta", elemento['Cantidad'])
            
        #imprime el valor total y la cantidad
        print(verde+"")
        print(f"El valor total del inventario es {Valor_Total}")
        print(f"La cantidades totales vendidas hoy son {cantidades}")
        print(f"Producto mas caro {[(d['Nombre'] , d['Precio']) for d in Inventario_Dict if d['Precio'] == precio_mas_alto]}")# Funcion para ver cual es el precio mas alto
        print(f"Cantidad mas vendido {[(d['Nombre'] , d['Cantidad']) for d in Inventario_Dict if d['Cantidad'] == cantidad_mas_alta]}")# Funcion para ver la cantidad mas alta
        print(f"La Cantidad de Productos registrados del inventario es: {len(Inventario_Dict)}")
        print(""+reset)

        print(Inventario_Dict)