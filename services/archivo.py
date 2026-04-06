#importa el modulo csv
import csv

# Lista inventario
from Lista import Inventario_Dict

# importa las funciones de error al ingresar dato
from funciones_secundarias.Funciones_error import error_string

#Traer colores
from funciones_secundarias.Color import rojo, reset, verde

# -------------------------------------------------
# GUARDAR CSV
# -------------------------------------------------

def Guardar():
    """
    Guarda el inventario en un archivo CSV.

    Reglas:
    - Usa encabezado: Nombre, Precio, Cantidad
    - Valida que el inventario no esté vacío
    - Maneja errores de escritura/permisos
    - Muestra la ruta si se guarda correctamente
    """

 
    if not Inventario_Dict:

        print(rojo + "-------------------------------------------------------" + reset)
        print(rojo + "- El inventario está vacío, no hay datos para guardar -" + reset)
        print(rojo + "-------------------------------------------------------" + reset)
        return

    ruta = "inventario.csv"

    try:
        with open(ruta, mode='w', newline='', encoding='utf-8') as file:

            fieldnames = ["Nombre", "Precio", "Cantidad"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for producto in Inventario_Dict:
                
                writer.writerow({
                    "Nombre": producto["Nombre"],
                    "Precio": producto["Precio"],
                    "Cantidad": producto["Cantidad"]
                })

        print(verde + f"Inventario guardado en: {ruta}" + reset)

    except PermissionError:
        print(rojo + "-------------------------------------------------------")
        print("- Error: No tienes permisos para escribir el archivo. -")
        print("-------------------------------------------------------"+ reset)

    except Exception as e:
        print(rojo + f"Error inesperado al guardar: {e}" + reset)


# -------------------------------------------------
# CONFIRMAR SOBRESCRITURA
# -------------------------------------------------

def Valor():
    """
    Pregunta al usuario si desea sobrescribir el inventario.

    Retorna:
        'S' → sobrescribir
        'N' → combinar
    """

    while True:
        valor = error_string("¿Sobrescribir inventario actual? (S/N): ").upper()

        if valor in ["S", "N"]:
            return valor
        else:
            print(rojo + "--------------------")
            print("- Opción no válida -")
            print("--------------------" + reset)


# -------------------------------------------------
# CARGAR CSV
# -------------------------------------------------

def cargar():
    """
    Carga datos desde un archivo CSV.

    Validaciones:
    - Encabezado exacto: Nombre, Precio, Cantidad
    - 3 columnas por fila
    - Precio → float (>=0)
    - Cantidad → int (>=0)
    - Omite filas inválidas y las cuenta

    Manejo de errores:
    - Archivo no encontrado
    - Problemas de codificación
    - Errores de conversión
    """

    ruta = "inventario.csv"
    errores = 0

    try:
        with open(ruta, mode="r", encoding="utf-8") as file:

            reader = csv.reader(file)

            encabezado = next(reader, None)

            # 🔴 VALIDACIÓN EXACTA DEL ENCABEZADO
            if encabezado != ["Nombre", "Precio", "Cantidad"]:
                
                print(rojo + "-------------------------------" + reset)
                print(rojo + "- Error: Encabezado inválido. -" + reset)
                print(rojo + "-------------------------------" + reset)
                return

            opcion = Valor()

            if opcion == "S":
                Inventario_Dict.clear()

            lista_temporal = []

            for fila in reader:

                if len(fila) != 3:
                    errores += 1
                    continue

                nombre, precio, cantidad = fila

                try:
                    precio = float(precio)
                    cantidad = int(cantidad)

                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue

                    lista_temporal.append({
                        "Nombre": nombre,
                        "Precio": precio,
                        "Cantidad": cantidad
                    })

                except ValueError:
                    errores += 1
                    continue

            # 🔵 COMBINAR o SOBRESCRIBIR
            if opcion == "N":

                for nuevo in lista_temporal:
                    encontrado = False

                    for actual in Inventario_Dict:
                        if actual["Nombre"] == nuevo["Nombre"]:
                            actual["Cantidad"] += nuevo["Cantidad"]
                            actual["Precio"] = nuevo["Precio"]
                            encontrado = True
                            break

                    if not encontrado:
                        Inventario_Dict.append(nuevo)

            else:
                Inventario_Dict.extend(lista_temporal)
            print(verde + "---------------------------------" + reset)
            print(verde + "- Datos cargados correctamente. -" + reset)
            print(verde + "---------------------------------" + reset)

            if errores > 0:
                print(rojo + f"{errores} filas inválidas omitidas." + reset)

    except FileNotFoundError:
        print(rojo + "Error: El archivo no existe." + reset)

    except UnicodeDecodeError:
        print(rojo + "Error: Problema de codificación del archivo." + reset)

    except Exception as e:
        print(rojo + f"Error inesperado: {e}" + reset)