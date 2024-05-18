'''Tiempo de viaje. Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él
tiene la duración en minutos de cada uno de los tramos del viaje.
Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y
entregue como resultado el tiempo total de viaje en formato horas:minutos.
El programa deja de pedir tiempos de viaje cuando se ingresa un 0.'''

total_minutos = 0
while True:
    try:
        total_tramo = int(input("Ingresa el tiempo del recorrido, luego ingresa 0 para avanzar: "))
        if total_tramo == 0:
            break
        total_minutos += total_tramo
    except ValueError:
        print("Ingrese un numero correcto.")
horas = total_minutos // 60
minutos = total_minutos % 60
print(f"El recorrido es de {horas} horas y {minutos} minutos.")


