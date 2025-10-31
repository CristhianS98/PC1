"""
El programa debe pedir al usuario que ingrese un número entero positivo y, 
en caso de que el valor ingresado no sea válido, debe volver a solicitarlo. 
Una vez validado el número, el programa recorrerá todos los números desde 
1 hasta N, identificando aquellos que sean pares o múltiplos de 5 para guardarlos 
en una lista. Finalmente, mostrará en pantalla la lista completa de números que 
cumplen la condición junto con la suma total de dichos valores.

"""
comprobar= True
while comprobar == True:
    n= int(input("Ingresa un número positivo: "))

    if n>0:
        comprobar=False
        lista=[]
        for i in range(1,n+1):
            if i%2==0 or i%5==0:
                lista.append(i)
        print(f"Los números que cumplen la condición son: {lista}\nLa suma de todos los elementos de la lista es: {sum(lista)}")    
    else:
        print("El número ingresado no es correcto, por favor inténtelo nuevamente.")
    
    