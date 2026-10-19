"""Ejercicio 14 — Dos nombres o dos objetos

Crea a = Libro("L1", "Dune"), b = a y c = Libro("L2", "Dune"). 
Antes de ejecutar b.prestar(), predice qué ocurrirá con a.disponible y c.disponible. 
Ejecuta y muestra a is b y a is c. is comprueba si dos referencias apuntan al mismo objeto.

Comprueba: a y b nombran el mismo objeto, que queda prestado. c es otro y sigue disponible. a is b es True y a is c es False.

Ampliación: Crea dos listas, copia = lista y separada = lista.copy(). 
Añade un elemento a copia y explica cuál de las dos listas cambia. La copia es superficial.
"""

from modelos_inicio import Libro

# Creamos los objetos y las referencias
a = Libro("L1", "Dune")
b = a
c = Libro("L2", "Dune")

# Comprobamos los estados antes de prestar
print("Antes de prestar:")
print("a:", a.disponible)
print("b:", b.disponible)
print("c:", c.disponible)

# Prestamos mediante b
b.prestar()

print("\nDespués de prestar mediante b:")
print("a:", a.disponible)
print("b:", b.disponible)
print("c:", c.disponible)

# Comprobamos si apuntan al mismo objeto
print("\na is b:", a is b)
print("a is c:", a is c)

# ampliación
lista = [1, 2, 3]

copia = lista
separada = lista.copy()

copia.append(4)

print("Lista original:", lista)
print("Copia:", copia)
print("Separada:", separada)