"""Ejercicio 02 — Un cálculo de existencias

Una biblioteca tiene 12 ejemplares y ha prestado 5. Calcula cuántos quedan y qué porcentaje representan. 
Guarda ambos resultados y muéstralos con un texto. Usa una cadena f para incluir valores, por ejemplo f"Quedan {restantes}". 
Supón que el total es positivo.

Comprueba: Quedan 7 ejemplares. El porcentaje es aproximadamente 58,33. Si prestados vale 0, quedan 12 y el porcentaje es 100.

Ampliación: Calcula cuántas cajas de 5 ejemplares se llenan con los 12 y cuántos sobran.
"""

# Escribe tu solución debajo.

ejemplares = 12
prestados = 5
capacidad = 5

restantes = ejemplares - prestados
porcentaje = (restantes / ejemplares)*100

if restantes > 0:  
    print(f"Me quedan {restantes} ejemplares")
    print(f"El porcentaje de los ejemplares que quedan es aproximadamente el {round(porcentaje, 3)}%.")
else:
    print("Error: el resultado es menor a 0.")
    
cajas_totales = ejemplares // capacidad
resto = ejemplares % capacidad
print(f"Con {ejemplares} se llenarían {cajas_totales} cajas y sobrarían {resto} libros.")
    