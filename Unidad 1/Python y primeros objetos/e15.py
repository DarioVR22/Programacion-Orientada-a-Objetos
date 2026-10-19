"""Ejercicio 15 — Buscar entre objetos

Crea una lista con L1 Dune y L2 1984. Define buscar(libros, codigo): devuelve el objeto cuyo código coincide o None si no existe. 
Prueba L1 y L9. Solo llama a prestar cuando el resultado no sea None.

Comprueba: Buscar L1 devuelve el propio objeto almacenado. Buscar L9 devuelve None. 
Prestar el resultado de L1 modifica el objeto de la lista.

Ampliación: Define disponibles(libros) que construya y devuelva una lista con los libros disponibles.
"""

# Copia aquí tus clases de los ejercicios anteriores que se necesitan.
# Escribe tu solución debajo.
from modelos_inicio import Libro


def buscar(libros, codigo):
    for libro in libros:
        if libro.codigo == codigo:
            return libro
    return None

def disponibles(libros):
    resultado = []
    for libro in libros:
        if libro.disponible:
            resultado.append(libro)
    return resultado


L1 = Libro("L1", "Dune")
L2 = Libro("L2", "1984")

libros = [L1, L2]

resultado = buscar(libros, "L1")

if resultado is not None:
    resultado.prestar()

resultado = buscar(libros, "L9")

if resultado is not None:
    resultado.prestar()
else:
    print("El libro L9 no existe")

for libro in disponibles(libros):
    print(libro.resumen())