"""
Tablas cruzadas:
Genera la tabla de multiplicar del 1 al 12 para los números del 1 al 10. Imprime cada
tabla en bloques separados.

"""

for i in range(1, 11):  
    print(f"\nTabla del {i}:")
    for j in range(1, 13):  
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
        