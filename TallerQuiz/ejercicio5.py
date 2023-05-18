porcentajealto=0
porcentajeintermedio=0
porcentajebajo=0
precio_boleta=100
contador=0
while contador <10:
    edad=float(input("Digite su edad: "))
    if edad<5:
        print("No puede entrar")
    elif edad>=5 and edad <= 14:
        print("Tienes un 35% de descuento")
        descuento=0.35
        porcentajealto+= precio_boleta * descuento
    elif edad >= 15 and edad <= 19:
        print("Tienes un 25% de descuento")
        descuento=0.25
        porcentajeintermedio+= precio_boleta * descuento
    elif edad >= 20 and edad <=45:
        print("Tienes un 10% de descuento")
        descuento=0.10
        porcentajebajo+=precio_boleta * descuento
    elif edad >= 46  and edad <=65:
        print("Tienes un 25% de descuento")
        descuento=0.25
        porcentajeintermedio+=precio_boleta * descuento
    elif edad >= 66:
        print("Tienes un 35% de descuento")
        descuento=0.35
        porcentajealto+=precio_boleta * descuento
    contador+=1

cantidad_perdida=porcentajealto+porcentajeintermedio+porcentajebajo

print(f"La cantidad que perdio fue: {cantidad_perdida}")

