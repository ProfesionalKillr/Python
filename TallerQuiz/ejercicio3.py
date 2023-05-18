personas=0
niño=0
joven=0
adulto=0
viejo=0
pesoniño=0
pesojoven=0
pesoadulto=0
pesoviejo=0
while personas < 50: 
 edad=int(input("Digite la edad de la persona: "))
 peso=int(input("Digite el peso de la persona en kilogramos: "))

 if edad <=12:
    niño+=1
    pesoniño+=peso

 elif edad >= 13 and edad <= 29:
    joven+=1
    pesojoven+=peso

 elif edad >= 30 and edad <= 59:
    adulto+=1
    pesoadulto+=peso

 elif edad >= 60:
    viejo+=1
    pesoviejo+=peso

 personas+=1

print(f"La cantidad de niños es: {niño} y el promedio de peso es: {pesoniño/niño}")
print(f"La cantidad de jovenes es: {joven} y el promedio de peso es: {pesojoven/joven} ")
print(f"La cantidad de adultos es: {adulto} y el promedio de peso es: {pesoadulto/adulto}")
print(f"La cantidad de viejos es: {viejo} y el promedio de peso es: {pesoviejo/viejo}")