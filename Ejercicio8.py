'''Una máquina de alimentos tiene productos de tres tipos, A, B y C, que valen
respectivamente $270, $340 y $390. La máquina acepta y da de vuelto monedas de $10,
$50 y $100.
Escriba un programa que pida al usuario elegir el producto y luego le pida ingresar las
monedas hasta alcanzar el monto a pagar. Si el monto ingresado es mayor que el precio
del producto, el programa debe entregar las monedas de vuelto, una por una.'''



A = 270
B = 340
C = 390

producto = input("Ingresa el producto que deseas comprar A = 270$ , B = 340$ , C = 390$: ")
if producto in ["A" , "B" , "C"]:
    if producto == "A":
        precio_producto = A
    elif producto == "B":
        precio_producto = B
    else:
        precio_producto = C

    monto_ingresado = 0
    vuelto = 0

    while monto_ingresado < precio_producto:
        print("Ingresa una moneda: ")
        print("moneda_1 = 10$")
        print("moneda_2 = 50$")
        print("moneda_3 = 100$")
        monedas=int(input("Ingresa la moneda con la que pagaras: "))

        if monedas in [1,2,3]:
            if monedas == 1:
                monto_ingresado += 10
            elif monedas == 2:
                monto_ingresado += 50
            else:
                monto_ingresado += 100
        else:
            print("El valor que ingresaste es incorrecto.")

    if monto_ingresado > precio_producto:
        vuelto = monto_ingresado - precio_producto
        while vuelto > 0:
            if vuelto >= 50:
                print("Su vuelto es de 50$.")
                vuelto -= 50
            else:
                print("Su vuelto es 10$.")
                vuelto -= 10
else:
    print("Ingresa un producto valido.")
