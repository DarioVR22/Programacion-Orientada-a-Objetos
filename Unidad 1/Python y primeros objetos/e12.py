"""Ejercicio 12 — Nuestra primera clase

Crea tu propia clase Libro. Su inicializador recibe codigo y titulo, guarda ambos en self y establece disponible = True. 
Crea L1 con Dune y L2 con 1984. Muestra sus títulos. 
En esta versión añadimos un código para distinguir ejemplares incluso si comparten título.

Comprueba: L1 y L2 tienen códigos y títulos independientes. Ambos empiezan disponibles. Cambiar el título del primero no cambia el segundo.

Ampliación: Añade autor al inicializador y crea dos objetos con autores diferentes.
"""

# Escribe tu solución debajo.

from modelos_inicio import Libro

# Creamos los libros
if __name__ == "__main__":
    L1 = Libro(1, "Dune", autor="Frank Herbert")
    L2 = Libro(2, "1984", autor="George Orwell")

    # Mostramos los títulos
    print(L1.titulo)
    print(L2.titulo)

    # Comprobamos que tienen códigos y títulos independientes
    print(L1.codigo, L1.titulo, L1.disponible)
    print(L2.codigo, L2.titulo, L2.disponible)

    # Cambiamos el título del primero
    L1.titulo = "Dune: Edición especial"

    # Comprobamos que el segundo no cambia
    print(L1.titulo)
    print(L2.titulo)

    # Mostramos los autores
    print(L1.autor)
    print(L2.autor)