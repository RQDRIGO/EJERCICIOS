'''Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no.'''
    # Un numero es primo si es divisible entre 1 y si mismo.

try:
    num=int(input("Ingrese un numero: "))
    if num <= 1:
        print("No es un numero primo.")
    elif num == 2:
        print("Es un numero primo.")
    else:
        for i in range (2,num):
            if num % i == 0:            
                print(f"No es un numero primo")
                break 
            else:
                print("Es primo.")
                break
except ValueError:
    print("Ingrese un *Numero Entero* correcto.")