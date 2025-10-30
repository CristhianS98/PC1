"""
Verificación de año bisiesto y edad legal:
Pide el año de nacimiento y determina si es bisiesto. Luego calcula la edad del usuario
y verifica si es mayor de edad (18+).
"""
comprobar=True

while comprobar==True:
    
    año_nacimiento=int(input("Ingrese su año de nacimiento: "))
    año_actual=2025
    edad=año_actual-año_nacimiento 
     
    if año_nacimiento >=0:

        comprobar=False
    
        if edad >= 18:
                print(f"Su edad es {edad} y usted es mayor de edad")
        else:
                print(f"Su edad es {edad} y usted es menor de edad")
                
        if (año_nacimiento%4==0 and año_nacimiento%100!=0) or (año_nacimiento%400==0):
                print(f"Su año de nacimiento {año_nacimiento} es un año bisiesto")
        else:
                print("Su año de nacimiento",año_nacimiento, "no es bisiesto")
    else:
        print("Número inválido, por favor, inténtalo nuevamente.")
    