"""
Gestión de tareas:
Crea una lista de tareas como objetos (nombre, completado: true/false). Permite
añadir, marcar como completado y eliminar tareas usando métodos de array.

"""
tareas = [
    {"nombre": "Limpiar", "completado": False},
    {"nombre": "Cocinar", "completado": False},
    {"nombre": "Lavar", "completado": False},
    {"nombre": "Bañarse", "completado": False}
]

print("Tareas actuales:")
for t in tareas:
    print(t["nombre"], "-", t["completado"])

tareas.append({"nombre": "Jugar", "completado": False})
print("\nSe añadió la tarea 'Jugar'.")


tarea_completada = input("\nIngrese la tarea completada: ")
for t in tareas:
    if t["nombre"].lower() == tarea_completada.lower():
        t["completado"] = True


print("\nTareas finales:")
for t in tareas:
    print(t["nombre"], "-", t["completado"])
