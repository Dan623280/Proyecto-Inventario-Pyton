def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario.
    Retorna un diccionario con métricas.
    """

    if not inventario:
        return None

    subtotal = lambda p: p["Precio"] * p["Cantidad"]

    unidades_totales = sum(p["Cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)

    producto_mas_caro = max(inventario, key=lambda x: x["Precio"])
    producto_mayor_stock = max(inventario, key=lambda x: x["Cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["Nombre"], producto_mas_caro["Precio"]),
        "producto_mayor_stock": (producto_mayor_stock["Nombre"], producto_mayor_stock["Cantidad"])
    }