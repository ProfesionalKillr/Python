trabajadores=int(input("Digite la cantidad de trabajadores:"))
for i in range(trabajadores):
 tiempo_trabajado=int(input("Digite la cantidad de horas que trabaja a la semana: "))
 if tiempo_trabajado <=40:
    print(f"El tiempo que trabajo es {tiempo_trabajado} y su pago es {20*tiempo_trabajado}")
 elif tiempo_trabajado >40:
    horas_extra=tiempo_trabajado-40
    print(f"El tiempo que trabajo es {tiempo_trabajado}, su pago es {20*tiempo_trabajado} y por las horas extra que trabajo se le paga adicional {25*horas_extra}")