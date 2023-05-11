menor_50 = 0
entre_50_y_70 = 0
entre_70_y_80 = 0
mayor_80 = 0
for i in range(100):
    calificacion = float(input(f"Calificación del estudiante #{i+1}: "))
    if calificacion < 50:
        menor_50 += 1
    elif calificacion < 70:
        entre_50_y_70 += 1
    elif calificacion < 80:
        entre_70_y_80 += 1
    else:
        mayor_80 += 1
print(f"Cantidad de estudiantes con calificación menor a 50: {menor_50}")
print(f"Cantidad de estudiantes con calificación entre 50 y 70: {entre_50_y_70}")
print(f"Cantidad de estudiantes con calificación entre 70 y 80: {entre_70_y_80}")
print(f"Cantidad de estudiantes con calificación mayor o igual a 80: {mayor_80}")