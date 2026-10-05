"""Ejercicio 03 — Datos que escribe una persona

Pide un título y un número de páginas con input. Convierte las páginas con int y muestra cuántas tendría el libro si se añadieran 10.
En esta primera versión la entrada numérica será un entero válido. 
Anota qué ocurre al introducir "muchas" y conserva esa duda para el ejercicio 17.

Comprueba: Con Dune y 412, la nueva cantidad es 422. input devuelve texto incluso cuando escribes dígitos.
"muchas" produce ValueError en esta versión.

Ampliación: Muestra cuánto ocuparían dos ejemplares si sumamos sus páginas.
"""
# Escribe tu solución debajo.

titulo1 = input("Introduce un título: ")
paginas1 = input("Introduce un número de páginas: ")
paginas1 = int(paginas1)
paginas10=paginas1 + 10
print(f"Tu número de páginas +10 sería: {paginas10}.")

titulo2 = input("Introduce otro título: ")
paginas2 = input("Introduce otro número de páginas: ")
paginas2 = int(paginas2)

paginas_totales= paginas1 + paginas2
print(f"El número de páginas totales de los 2 libros sería {paginas_totales}.")

