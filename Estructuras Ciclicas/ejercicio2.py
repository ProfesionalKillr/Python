import random
total_clientes = int(input("Ingrese el número total de clientes: "))
DESCUENTO_ROJO = 0.4
DESCUENTO_AMARILLO = 0.25
DESCUENTO_BLANCO = 0
cantidad_rojo = 0
cantidad_amarillo = 0
cantidad_blanco = 0
for i in range(total_clientes):
    color_bolita = random.randint(1, 3)
    if color_bolita == 1:
        descuento = DESCUENTO_ROJO
        cantidad_rojo += 1
    elif color_bolita == 2:
        descuento = DESCUENTO_AMARILLO
        cantidad_amarillo += 1
    else:
        descuento = DESCUENTO_BLANCO
        cantidad_blanco += 1
    monto_compra = float(input("Ingrese el monto total de la compra del cliente: "))
    monto_pagar = monto_compra * (1 - descuento)
    print("El cliente debe pagar:", monto_pagar)
print("Cantidad de clientes con bolita roja:", cantidad_rojo)
print("Cantidad de clientes con bolita amarilla:", cantidad_amarillo)
print("Cantidad de clientes con bolita blanca:", cantidad_blanco)
