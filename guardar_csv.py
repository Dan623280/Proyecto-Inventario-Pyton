from Lista import Inventario_Dict
import csv



with open('inventario.csv', mode='w', newline='', encoding='utf-8') as file:
    fieldnames = Inventario_Dict[0].keys()  # Usa las claves del primer diccionario
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(Inventario_Dict)   