"""
Sistema de clasificación de rendimiento:
Solicita al usuario su nota (0-20) y su asistencia (%). Si la nota es mayor o igual a 11 y
la asistencia es mayor o igual al 70%, se aprueba. De lo contrario, se desaprueba.
Además, otorga menciones especiales para notas mayores a 17 con asistencia completa.
"""

comprobar = True

while comprobar == True:
    nota = int(input("Ingrese su nota (0-20): "))
    asistencia = float(input("Ingrese su asistencia (%): "))

    if nota < 0 or asistencia < 0:
        print("⚠️ Error: la nota o la asistencia no pueden ser negativas. Intente nuevamente.\n")
    else:
        comprobar = False  

if 11 <= nota <= 20 and 70 <= asistencia <= 100:
    if nota > 17 and asistencia == 100:
        print(f"Usted aprobó con mérito y asistencia perfecta.")
    else:
        print(f"Usted aprobó.")
else:
    print(f"Usted no aprobó.")
