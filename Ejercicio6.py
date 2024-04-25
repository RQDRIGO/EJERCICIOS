'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo con tantos renglones como indique el
usuario.'''

def main():
    try:
        numero=int(input("Ingresa un numero: "))
        if numero == 0:
            print("Ingresa un numero mayor o menor que 0.")
        else:
            for i in range(1 , numero +1):
                print("▽" * i )
    except ValueError:
        print("Debes ingresar un número entero válido.")
main()