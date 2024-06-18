#Servicio Nacional del Consumidor (SERNAC), está probando una forma simplificada para registrar y gestionar los
#reclamos de los consumidores. Para ello utiliza solo cuatro campos de información:
import csv


with open('nuevo_archivo.csv', 'w', newline='') as archivo_csv: 
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(['Rut', 'Fecha', 'Monto', 'Reclamo'])
    escritor_csv.writerows(['26.522.342-7', '18-06-2024', '98892', '73413'])


import csv
with open('nuevo_archivo.csv', 'r', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)



rut = ""
fecha = ""

monto = int(input("Ingrese El Valor de la compra en miles de pesos: "))
reclamo = print("Reseña del reclamo del texto libre, de no más de veinte caracteres",monto)

numrut = input("Por favor ingrese su RUT: ")
numfecha = input("Por favor ingrese su fecha: ")
numreclamo = int(input("Por favor ingrese el numero del dinero que reclama por su monto fallido: "))

{input("El registro del reclamo se encontrara en este menu de opciones, 1 Para Lista de reclamos, 2 Para Respetar reclamos, Presione 3 para salir: ")}
print("3",exit)