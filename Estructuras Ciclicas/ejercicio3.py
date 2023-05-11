cant_alumnos = 40
cant_materias = 5
contador_no_aprobados = 0

for i in range(cant_alumnos):
    calificaciones = []
    for j in range(cant_materias):
        calificacion = float(input(f"Ingrese la calificación de la materia {j+1} del alumno {i+1}: "))
        calificaciones.append(calificacion)
    promedio = sum(calificaciones) / cant_materias
    if promedio < 70:
        contador_no_aprobados += 1

print(f"La cantidad de alumnos que no tienen derecho al examen de nivelación es: {contador_no_aprobados}")
