"""
Búsqueda avanzada de elementos:
Crea un array de objetos con productos (nombre, categoría, precio). Solicita una
categoría y muestra todos los productos de esa categoría ordenados por precio.

"""


productos=[
        {"nombre":"PS5","categoria":"Electrónicos","precio":1500},
        {"nombre":"Mousepad","categoria":"Electrónicos","precio":50},
        {"nombre":"Monitor","categoria":"Electrónicos","precio":1200},
        {"nombre":"Polo","categoria":"Ropa","precio":20},
        {"nombre":"Short","categoria":"Ropa","precio":100},
        {"nombre":"Zapatillas","categoria":"Calzado","precio":1000},
    ]

categoria= input("Por favor, ingresa la categoría: ")
filtrados= [p for p in productos if p["categoria"].lower()==categoria.lower()]
filtrado_ordenado= sorted(filtrados, key=lambda x:x["precio"])
print(filtrado_ordenado)
for p in filtrado_ordenado:
    print(f"{p['nombre']}: {p['precio']}")


