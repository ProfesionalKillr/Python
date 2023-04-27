n_compu=int(input("Digite la cantidad de computadoras a comprar:"))
compu=15000
if n_compu<5:
    descuento=(compu*n_compu)*0.10
    valortotal=(compu*n_compu)-descuento
    input(f"Su descuento fue del 10% y el valor total es de {valortotal}")
elif n_compu>=5 and n_compu<10:
    descuento=(compu*n_compu)*0.20
    valortotal=(compu*n_compu)-descuento
    input(f"Su descuento fue del 20% y el valor total es de {valortotal}")
elif n_compu>=10:
    descuento=(compu*n_compu)*0.40
    valortotal=(compu*n_compu)-descuento
    input(f"Su descuento fue del 40% y el valor total es de {valortotal}")
else:
    input("Error")