n = int(input("Ingrese el número de vendedores: "))
sueldo_base = float(input("Ingrese el sueldo base de los vendedores: "))
for i in range(n):
    ventas = 3
    comisiones = ventas * 0.1 * sueldo_base
    salario_total = sueldo_base + comisiones
    print("Vendedor", i+1)
    print("Comisiones: $", comisiones)
    print("Salario total: $", salario_total)