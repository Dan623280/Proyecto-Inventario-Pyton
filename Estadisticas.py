from Lista import Inventario_Dict

#------------------------------
# Calculo estadistica
#------------------------------

def calcular_estadisticas():
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

    
    # VALIDAR SI EL INVENTARIO ESTÁ VACÍO
    
    if not Inventario_Dict:
        print("Inventario vacío")
        return

    
    # FUNCIÓN LAMBDA PARA CALCULAR SUBTOTAL POR PRODUCTO
    # (Precio * Cantidad)
    
    subtotal = lambda p: p["Precio"] * p["Cantidad"]

    
    # CÁLCULO DE UNIDADES TOTALES
    # Suma todas las cantidades de los productos
    
    unidades_totales = sum(p["Cantidad"] for p in Inventario_Dict)

    
    # CÁLCULO DEL VALOR TOTAL DEL INVENTARIO
    # Suma todos los subtotales (precio * cantidad)
    
    valor_total = sum(subtotal(p) for p in Inventario_Dict)

    
    # PRODUCTO MÁS CARO
    # Se obtiene el producto con mayor precio
    
    producto_mas_caro = max(Inventario_Dict, key=lambda x: x["Precio"])

    
    # PRODUCTO CON MAYOR STOCK
    # Se obtiene el producto con mayor cantidad disponible
    
    producto_mayor_stock = max(Inventario_Dict, key=lambda x: x["Cantidad"])

    
    # MOSTRAR RESULTADOS EN PANTALLA
    
    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total del inventario: {valor_total}")
    print(f"Producto más caro: ({producto_mas_caro['Nombre']}, {producto_mas_caro['Precio']})")
    print(f"Producto con mayor stock: ({producto_mayor_stock['Nombre']}, {producto_mayor_stock['Cantidad']})")

    
    # RETORNAR RESULTADOS COMO DICCIONARIO
    
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["Nombre"], producto_mas_caro["Precio"]),
        "producto_mayor_stock": (producto_mayor_stock["Nombre"], producto_mayor_stock["Cantidad"])
    }
#para llamar
#from Estadisticas import calcular_estadisticas