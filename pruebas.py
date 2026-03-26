import csv

with open("inventario.csv", "r",encoding="UTF-8") as leer:
    reader = csv.reader(leer)

    for elemento in reader:

        print(elemento)

