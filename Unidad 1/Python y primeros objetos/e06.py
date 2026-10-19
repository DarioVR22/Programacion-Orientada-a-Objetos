"""Ejercicio 06 — Una decisión sobre el plazo

Usa dias = 3 como número de días que faltan para devolver un libro. Si dias es mayor que 0, muestra "En plazo". Si es 0, "Vence hoy". Si es negativo, "Con retraso". 
Prueba también 0 y -2 cambiando la variable.

Comprueba: 3 produce En plazo, 0 produce Vence hoy y -2 produce Con retraso. Solo se ejecuta una rama.

Ampliación: Para un retraso, muestra además cuántos días han pasado desde el vencimiento.
"""

# Escribe tu solución debajo.
dias = -2

if dias > 0:
    print("En plazo")
elif dias == 0:
    print("Vence hoy")
else:
    print(f"Con retraso de {abs(dias)} días.")
    