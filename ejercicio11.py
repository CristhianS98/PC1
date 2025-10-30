"""
Inversión y manipulación de arrays:
Crea un array de palabras. Muestra el array original, luego uno con los elementos
invertidos, y otro con cada palabra en mayúsculas si tiene más de 5 letras.

"""

palabras= ["Hola", "silla", "Paralelo", "Empezar", "Tiempo", "Sueño", "Oscuridad", "Laptop"]
invertido= palabras[::-1]
mayusculas= [p.upper() if len(p)>5 else p.lower() for p in palabras]


print("Array original: ",palabras)
print("Array con elementos invertidos:",invertido)
print("Palabras con más de 5 dígitos convertidos a mayúscula:",mayusculas)

