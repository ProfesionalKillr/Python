n1=int(input("Digite el primer numero:"))
n2=int(input("Digite el segundo numero:"))
if n1==n2:
    total=n1*n2
    input(total)
elif n1>n2:
    total=n1-n2
    input(total)
else:
    total=n1+n2
    input(total)