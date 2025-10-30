"""
Evaluación de estudiantes:
Dado un array de estudiantes (nombre, notas[]), calcula el promedio individual y
muestra los que aprobaron (promedio ≥ 11) y su mención (suficiente, bueno, excelente).

"""

estudiantes = [
    {"nombre": "Ana", "notas": [12, 15, 14]},
    {"nombre": "Luis", "notas": [9, 10, 8]},
    {"nombre": "María", "notas": [18, 17, 16]},
    {"nombre": "Carlos", "notas": [11, 12, 10]},
    {"nombre": "Sofía", "notas": [14, 13, 15]}
]
print("Resultados de las notas de los alumnos del curso de Python:")
for e in estudiantes:
    # Calcular promedio
    promedio = sum(e["notas"]) / len(e["notas"])
    
    if promedio >= 11:
        
        if promedio < 13:
            mencion = "Suficiente"
        elif promedio < 16:
            mencion = "Bueno"
        else:
            mencion = "Excelente"
            
        print(f"{e['nombre']} - Promedio: {promedio:.2f} - Mención: {mencion}")
