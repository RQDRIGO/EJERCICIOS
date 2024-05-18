''' Anagrama. Escribe una función que reciba dos palabras y retorne
verdadero o falso según sean o no anagramas.
● Un Anagrama consiste en formar una palabra reordenando TODAS las letras de
otra palabra inicial.
● NO hace falta comprobar que ambas palabras existen.
● Dos palabras exactamente iguales no son anagrama.'''


def son_anagramas(palabra1, palabra2):
    # Cambiar las palabras a minuscula.

    palabra1 = str.lower(palabra1)
    palabra2 = str.lower(palabra2)

    # Pasar las palabras a listas.

    palabra1 = list(palabra1)
    palabra2 = list(palabra2)

    # Ordenar alfabeticamente.

    palabra1_ordenada = palabra1.sort()
    palabra2_ordenada = palabra2.sort()

    # Volver a transformarlo en cadena.

    palabra1_ordenada = str(palabra1_ordenada)
    palabra2_ordenada = str(palabra2_ordenada)
    
    # Verificar si las palabras ordenadas son iguales.

    return palabra1 == palabra2
   

    # Ejecutar programa.

palabra1 = input("Ingresa una palabra: ")
palabra2 = input("Ingresa otra palabra: ")
if palabra1 == palabra2:
    print(f"{palabra1} y {palabra2} No son anagramas.")
elif son_anagramas(palabra1, palabra2):
    print(f"{palabra1} y {palabra2} Son anagramas.")
else:
    print(f"{palabra1} y {palabra2} No son anagramas.")