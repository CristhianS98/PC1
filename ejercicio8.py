"""
Números primos dentro de un rango definido:
Pide al usuario un número inicial y uno final. Luego, muestra todos los números
primos dentro de ese rango usando una función que los verifique.

"""
I=int(input("Ingresa el número inicial: "))
F=int(input("Ingresa el número final: "))

primos=[]

for i in range(I+1,F):
    if i >=2:
        es_primo=True
        for j in range(2,i):
            if i%j==0:
                es_primo=False
        if es_primo:
            primos.append(i)
print(primos)

