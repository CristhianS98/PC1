"""
Agrupación por primera letra:
Dado un array de nombres, agrupa los nombres por su primera letra en un objeto. Por
ejemplo: { A: [Ana, Alberto], B: [Bruno, Brenda] }.

"""

nombres = ["Leonardo", "Cristhian", "Yael", "Eduardo", "Milner", "Valeria", "Monica", "Helen"]

agrupados = {}
for n in nombres:
    letra = n[0].upper()
    if letra not in agrupados:
        agrupados[letra] = []
    agrupados[letra].append(n)

print(agrupados)