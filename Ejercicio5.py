'''Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era
el calendario vigente en ese año.'''

# Un año es bisiesto si cumple con las siguientes condiciones:
# Es divisible por 4.
# No es divisible por 100, a menos que también sea divisible por 400.


año=int(input("Ingresa un año del calendario: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")

