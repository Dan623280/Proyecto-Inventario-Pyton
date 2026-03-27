import csv

from Lista import Inventario_Dict
datos = [

]

with open('inventario.csv', 'r', newline='') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        datos.append(fila)



with open('personas.csv', mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows(datos)



# Paso 1: Leer y modificar
filas = []
#with open('personas.csv', mode='r', newline='', encoding='utf-8') as file:
#    reader = csv.DictReader(file)
    
#    for row in reader:
        
#        if row['Nombre'] == 'Ana':

#           row['edad'] = '25'  # Actualizar valor

#        filas.append(row)


#Paso 2: Guardar cambios
with open('personas.csv', mode='w', newline='', encoding='utf-8') as file:
    fieldnames = Inventario_Dict[0].keys()  # Usa las claves del primer diccionario
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(Inventario_Dict)   