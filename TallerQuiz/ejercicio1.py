hipoteca=int(input("Digite el valor de la hipoteca: "))
inversion=int(input("Digite el valor de la casa: "))
if hipoteca<1000000:
    inversion1 = inversion/2
    print(f"La hipoteca tiene un valor menor a 1'000.000, tienes que invertir {inversion1} y el socio {inversion1}")
elif hipoteca>=1000000:
    hipoteca1 = inversion-1000000
    socio = hipoteca1/2
    hipoteca2 =socio+1000000
    print(f"La hipoteca tiene un valor mayor a 1'000.000, tienes que invertir {hipoteca2} y el socio {socio}")