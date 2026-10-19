"""Ejercicio 19 — Guardar y recuperar el catálogo

Extensión opcional hacia RA3. Define guardar(biblioteca, ruta) y cargar(ruta). Guarda una lista de diccionarios con codigo, titulo y disponible. 
Al cargar, crea una nueva Biblioteca y nuevos Libro, recuperando el estado mediante prestar si corresponde.
En este ejercicio el JSON tiene el formato esperado y códigos únicos. Préstale L1, guarda, carga y comprueba su estado.

Comprueba: La nueva biblioteca conserva títulos, códigos y disponibilidad, pero contiene instancias nuevas. Un título con tildes se conserva. 
JSON almacena datos, no los métodos del objeto.

Ampliación: Si el fichero no existe, devuelve una biblioteca vacía. Un JSON dañado debe seguir mostrando su error, sin ocultarlo.
"""

# Reutiliza tus clases Libro y Biblioteca del ejercicio 16.
# Escribe tu solución debajo.
import json
from pathlib import Path
from modelos_inicio import Biblioteca, Libro


def guardar(biblioteca, ruta):
    datos = []

    for libro in biblioteca.libros:
        datos.append({
            "codigo": libro.codigo,
            "titulo": libro.titulo,
            "disponible": libro.disponible
        })

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)
        
def cargar(ruta):
    biblioteca = Biblioteca()

    if not Path(ruta).exists():
        return biblioteca

    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    for dato in datos:
        libro = Libro(
            dato["codigo"],
            dato["titulo"]
        )

        if not dato["disponible"]:
            libro.prestar()

        biblioteca.agregar(libro)

    return biblioteca

biblioteca = Biblioteca()

biblioteca.agregar(
    Libro("L1", "Cien años de soledad", autor="Gabriel García Márquez")
)
biblioteca.agregar(
    Libro("L2", "El principito", autor="Antoine de Saint-Exupéry")
)

# Prestamos el primer libro
biblioteca.prestar("L1")

# Guardamos la biblioteca
guardar(biblioteca, "biblioteca.json")

# Cargamos una nueva biblioteca
biblioteca_nueva = cargar("biblioteca.json")

# Comprobamos los estados
for libro in biblioteca_nueva.libros:
    print(libro.codigo, libro.titulo, libro.disponible)

# Comprobamos que son instancias diferentes
print(biblioteca.libros[0] is biblioteca_nueva.libros[0])