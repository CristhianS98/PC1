"""
Suma condicional de múltiplos:
Pide un número N y suma solo los múltiplos de 3 o 5 hasta N. Muestra la suma y los
múltiplos encontrados.

"""
comprobar=True
while comprobar ==True:
    n=int(input("ingrese un número entero positivo: "))
    
    if n > 0:
        comprobar=False
        suma = 0
        multiplos=[]
        for i in range(1,n+1):
            if i%3==0 or i%5==0:
             suma += i
             multiplos.append(i)
        print(f"Los números que cumplen la condición son:\n: {multiplos}")
        print("La suma de los múltiplos de 3 o 5 es:",suma)
    else:
        
        print("El número ingresado no es correcto, inténtelo nuevamente. ")
    
