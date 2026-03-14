#-------------------------------------------------
# COLORES PARA LA TERMINAL
#-------------------------------------------------

verde = "\033[92m"
rojo = "\033[91m"
azul = "\033[94m"
amarillo = "\033[93m"
reset = "\033[0m"


#-------------------------------------------------
# FUNCIONES PARA VALIDAR DATOS
#-------------------------------------------------

# Función para validar texto
def error_string(var):
    while True:
        try:
            valor = input(f"Colocar {var} del producto: ")
            return valor
        except:
            print(rojo + "Valor no válido, debe ser texto" + reset)


# Función para validar números enteros
def error_number_int(var):
    while True:
        try:
            valor = int(input(f"Colocar {var} del producto: "))
            
            if valor >= 0:
                return valor
            else:
                print(rojo + "Los valores negativos no son válidos" + reset)
                
        except:
            print(rojo + "Valor no válido, debe ser un número entero" + reset)


# Función para validar números decimales
def error_number_float(var):
    while True:
        try:
            valor = float(input(f"Colocar {var} del producto: "))
            valor = int(valor)
            if valor >= 0:
                return valor
            else:
                print(rojo + "Los valores negativos no son válidos" + reset)
                
        except:
            print(rojo + "Valor no válido, debe ser un número" + reset)


#-------------------------------------------------
# MENSAJE DE BIENVENIDA
#-------------------------------------------------

print("")
print(azul + "============================================================")
print("== Bienvenido a nuestro Programa para registrar productos ==")
print("============================================================" + reset)
print("")


#-------------------------------------------------
# SOLICITAR DATOS DEL PRODUCTO
#-------------------------------------------------

# Nombre del producto
nombre = error_string("nombre")

# Precio unitario
precio = error_number_float("precio unitario")

# Cantidad de productos
cantidad = error_number_int("cantidad")


#-------------------------------------------------
# CÁLCULO DEL COSTO TOTAL
#-------------------------------------------------

costo_total = precio * cantidad


#-------------------------------------------------
# MOSTRAR RESULTADOS
#-------------------------------------------------

print("")
print(verde + "=========== INFORMACIÓN DEL PRODUCTO ===========")
print(f"Nombre del producto: {nombre}")
print(f"Precio unitario: {precio}")
print(f"Cantidad: {cantidad}")
print(f"Total a pagar: {costo_total}")
print("================================================" + reset)
print("")

# Este programa permite registrar un producto desde la terminal.
# Solicita al usuario el nombre del producto, el precio unitario y la cantidad.
# Luego calcula el costo total multiplicando el precio por la cantidad.
# Finalmente muestra en pantalla la información del producto y el total.
# Si el usuario introduce un valor no válido, el programa solicita nuevamente el dato.