votos = {} 
for i in range(2500000):
    candidato = int(input(f"Voto #{i+1}: "))
    if candidato in votos:
        votos[candidato] += 1 
    else:
        votos[candidato] = 1 
candidato_ganador = max(votos, llave=votos.get)
print(f"El candidato ganador es el número {candidato_ganador} con {votos[candidato_ganador]} votos.")
