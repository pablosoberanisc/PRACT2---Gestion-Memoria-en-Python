print("Calculadora Simple")
dato = float(input("Ingrese el primer número: "))
tipodeoperacion = input("Ingrese la operación que desea realizar (suma, resta, multiplicacion, division): ")
dato2 = float(input("Ingrese el segundo número: "))

if tipodeoperacion == "suma":
    resultado = dato + dato2
    print("El resultado de la suma es:", resultado)
elif tipodeoperacion == "resta":
    resultado = dato - dato2
    print("El resultado de la resta es:", resultado)
elif tipodeoperacion == "multiplicacion":
    resultado = dato * dato2
    print("El resultado de la multiplicación es:", resultado)
elif tipodeoperacion == "division":
    if dato2 != 0:
        resultado = dato / dato2
        print("El resultado de la división es:", resultado)
    else:
        print("Error: No se puede dividir por cero.")
else:
    print("Operación no válida. Por favor, seleccione suma, resta, multiplicacion o division.")
