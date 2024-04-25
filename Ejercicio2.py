'''Escriba un programa que pregunte al usuario la hora actual t del reloj y un número
entero de horas h, que indique qué hora marcará el reloj dentro de h horas:'''
hora_actual = int(input(f"Introduce la hora actual (0-23): "))
horas_transcurridas = int(input("Introduce el número de horas transcurridas: "))
    

# Calcula la hora futura
hora_futura = (hora_actual + horas_transcurridas) % 24

# Muestra el resultado
print(f"En {horas_transcurridas} horas, el reloj marcará las {hora_futura}.")