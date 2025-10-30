"""
Contador de dígitos pares e impares:
Solicita un número entero largo, y con un bucle determina cuántos dígitos son pares y
cuántos impares.

"""
n=input("Ingresa un número de varios dígitos: ")

par=[]
impar=[]

for i in n:
    
    if int(i)%2==0:
        par.append(int(i))
    else:
        impar.append(int(i))
print(f"En el número ingresado, estos son los dígitos:\n Pares: {par}\n Impares: {impar}")
print("la cantidad de números pares son:",len(par),"y la cantidad de número impares son: ",len(impar))