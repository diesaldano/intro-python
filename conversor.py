menu = """
Bienvenidos al conversor de monedas 

1 - Pesos colombianos
2 - Pesos argentinos
3- Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("Ingrese la cantidad de pesos colombianos que tiene:")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
elif opcion == 2:
    pesos = input("Ingrese la cantidad de pesos argentinos que tiene:")
    pesos = float(pesos)
    valor_dolar = 144
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
elif opcion == 3:
    pesos = input("Ingrese la cantidad de pesos mexicanos que tiene:")
    pesos = float(pesos)
    valor_dolar = 88
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
else:
    print("Ingrese una opción correcta por favor")

print("Tienes $"+ dolares + " dólares")