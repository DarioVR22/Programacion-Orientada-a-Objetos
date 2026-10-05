"""Ejercicio 04 — Los textos tienen métodos

Parte de titulo = "  dune  ". Predice y ejecuta titulo.strip() y titulo.upper(). 
Guarda el resultado de strip en limpio y el de upper aplicado a limpio en mayusculas. 
Muestra los tres nombres con repr para ver sus espacios. No encadenes todavía las llamadas.

Comprueba: titulo mantiene sus espacios y minúsculas. limpio vale "dune" y mayusculas vale "DUNE".

Ampliación: Compara los títulos " Dune " y "dune" ignorando espacios exteriores y mayúsculas.
"""

# Escribe tu solución debajo.
titulo = "  dune  "
limpio = titulo.strip()
mayusculas = limpio.upper()

print(repr(titulo))
print(repr(limpio))
print(repr(mayusculas))

titulo2= " Dune "
titulo = titulo.strip().lower()
titulo2 = titulo2.strip().lower()
if titulo == titulo2:
    print("Los títulos son iguales")