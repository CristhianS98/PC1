""""
Clasificación de productos:
Pide nombre, precio y categoría (tecnología, alimentos, ropa). Dependiendo de la
categoría y precio, aplica diferentes tipos de impuestos y clasificaciones (lujo, básico,
etc.).

"""
comprobar=True

categorias={
    "tecnología":{"impuesto": 0.15, "precio_lujo":2000},
    "alimentos":{"impuesto": 0.05, "precio_lujo":500},
    "ropa":{"impuesto": 0.10, "precio_lujo":1000}  
}

while comprobar == True:
    
    nombre=input("Ingrese el nombre del producto: ")
    precio=float(input("Ingrese el precio del producto: "))
    categoria=input("Ingrese la categoria del producto: ").lower()


    
    if categoria in categorias:
        
        comprobar=False
        
        impuesto=precio*categorias[categoria]["impuesto"]
        total=precio+impuesto
        
        if precio >= categorias[categoria]["precio_lujo"]:
            clasificacion="Lujo"
        else:
            clasificacion= "Básico"
            
        print(f"Producto: {nombre}")
        print(f"La categoría del producto es: {categoria}")
        
        if clasificacion == "Lujo":
            print("Clasificación: LUJO")
            print(f"Impuesto a pagar: S/. {impuesto:.2f}")
            print(f"El total a pagar es: S/.{total:.2f}")
        else:
            print("Clasificación: BÁSICO")
            print(f"Impuesto a pagar: S/. {impuesto:.2f}")
            print(f"El total a pagar es: S/. {total:.2f}")
    else:
        print("La categoría del producto ingresado no existe, por favor, inténtalo nuevamente.")