hectareas=int(input("Digite la cantidad de hectareas: "))
convercion=hectareas*10000
if convercion<=1000000:
    print(f"El porcentaje para sembrar pino es del 50%({convercion/2} metros cuadrados)")
    print(f"El porcentaje para sembrar oyamel es del 30%({convercion*0.3} metros cuadrados)")
    print(f"El porcentaje para sembrar cedro es del 20%({convercion*0.2} metros cuadrados)")
elif convercion>1000000:
    print(f"El porcentaje para sembrar pino es del 70%({convercion*0.7} metros cuadrados)")
    print(f"El porcentaje para sembrar oyamel es del 20%({convercion*0.2} metros cuadrados)")
    print(f"El porcentaje para sembrar cedro es del 10%({convercion*0.1} metros cuadrados)")