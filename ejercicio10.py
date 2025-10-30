"""
Filtrado y estadística de temperaturas:
Dado un array de temperaturas de un mes, filtra los días con temperaturas mayores al
promedio y muestra estadísticas como el mínimo, máximo y promedio general.

"""

temperaturas=[10,8,15,20,15,29,30,39,43,45,14,21,17,19,25]

promedio=sum(temperaturas)/len(temperaturas)

filtrado= [t for t in temperaturas if t>promedio]

print(f"El promedio es: {promedio:.2f} \n Las temperaturas del mes son: {temperaturas}\n Las temperaturas mayores al promedio son {filtrado}\n la temparatura mínima es: {min(temperaturas)}\n La temparatura máxima es: {max(temperaturas)} ")
