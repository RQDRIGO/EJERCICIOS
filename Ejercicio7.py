'''La secuencia de Collatz de un número entero se construye de la siguiente forma:
Comenzamos con un número entero positivo.
1 ~ Si el número es par, lo dividimos por dos.
2 ~ Si el número es impar, lo multiplicamos por tres y le sumamos uno.
3 ~ Repetimos los pasos 2 y 3 hasta que lleguemos al número 1.'''

def secuencia_de_collatz(numero):
    while numero != 1:
        print(numero, end="->")
        if numero % 2 == 0:
            numero = numero // 2
        else:
            numero = 3 * numero + 1
    print(1)
try:
    numero = int(input("Ingresa un número entero positivo: "))
    if numero <= 0:
        print("Por favor, ingresa un número positivo mayor que cero.")
    else:
        print(f"Secuencia de Collatz para {numero}:")
        secuencia_de_collatz(numero)
except ValueError:
    print("Ingresa un número válido.")