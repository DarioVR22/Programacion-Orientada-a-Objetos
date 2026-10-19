"""Ejercicio 16 — Una biblioteca contiene libros

Define Biblioteca con self.libros = [] en __init__. Añade buscar(codigo), agregar(libro) y prestar(codigo).
agregar rechaza códigos repetidos y devuelve un booleano. prestar busca el objeto y delega en su método prestar. 
Si no lo encuentra, devuelve False. Un mismo título con códigos distintos sí se admite.

Comprueba: Agregar L1 funciona una vez. Agregar otro L1 falla sin reemplazar el anterior. 
Prestar L9 falla. Dos bibliotecas nuevas no comparten su lista.

Ampliación: Añade total_disponibles que devuelva cuántos libros disponibles tiene la biblioteca.
"""

# Copia aquí tus clases de los ejercicios anteriores que se necesitan.
# Escribe tu solución debajo.
from modelos_inicio import Biblioteca, Libro

# Creamos una biblioteca y varios libros
biblioteca = Biblioteca()

L1 = Libro("L1", "Dune")
L2 = Libro("L2", "Dune")
L3 = Libro("L1", "1984")
L9 = Libro("L9", "El Hobbit")

# Comprobamos agregar()
print(biblioteca.agregar(L1))  # True
print(biblioteca.agregar(L3))  # False: código repetido
print(biblioteca.agregar(L2))  # True: código diferente

# Comprobamos prestar()
print(biblioteca.prestar("L1"))  # True
print(biblioteca.prestar("L1"))  # False: ya está prestado
print(biblioteca.prestar("L9"))  # False: no existe

# Comprobamos la ampliación
print("Libros disponibles:", biblioteca.total_disponibles())

# Comprobamos que dos bibliotecas no comparten su lista
biblioteca2 = Biblioteca()
print(biblioteca.libros is biblioteca2.libros)  # False
