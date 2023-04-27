n_llantas=int(input("Buen dia le desea Ponchadas, Digite cual es la cantidad de llantas a comprar:"))
if n_llantas<5:
    total=n_llantas*300
    input(f"El valor de cada llanta sale por $300 y el total es {total}")
elif n_llantas>=5 and n_llantas<=10: 
    total=n_llantas*250
    input(f"El valor de cada llanta sale por $250 y el total es {total}")
elif n_llantas>10:
    total=n_llantas*200
    input(f"El valor de cada llanta sale por $200 y el total es {total}")