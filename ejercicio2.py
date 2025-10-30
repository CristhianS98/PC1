"""
Validación de acceso:
Solicita usuario, contraseña y rol (admin, editor, visitante). Verifica si las credenciales
son válidas y muestra los permisos disponibles según el rol. Usa múltiples condicionales
y lógica anidada.
"""

comprobar = True

usuarios = {
    "admin": {"contraseña": "admin123", "rol": "admin"},
    "editor": {"contraseña": "editor123", "rol": "editor"},
    "visitante": {"contraseña": "visit123", "rol": "visitante"}
}

while comprobar == True:
    usuario = input("Ingresa el usuario: ")
    contraseña = input("Ingresa la contraseña: ")

    if usuario in usuarios and contraseña == usuarios[usuario]["contraseña"]:
        comprobar = False 
        
        rol = usuarios[usuario]["rol"]
        print(f"\n Acceso concedido ({rol.upper()})")

        if rol == "admin":
            print("Permisos: Control total")
        elif rol == "editor":
            print("Permisos: Puede editar.")
        else:
            print("Permisos: Solo lectura (visitante).")

    else:
        print("Usuario o contraseña incorrectos. Intente nuevamente.\n")
