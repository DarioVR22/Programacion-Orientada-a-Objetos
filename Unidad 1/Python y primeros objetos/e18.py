"""Ejercicio 18 — La biblioteca de consola

Prepara una Biblioteca con L1 Dune y L2 1984. Implementa un menú: 1 listar, 2 prestar, 3 devolver y 0 salir. Reutiliza pedir_entero. 
Para préstamo o devolución solicita un código y distingue libro inexistente de operación rechazada. 
La interfaz muestra mensajes, pero cambia el estado llamando a métodos. Puedes copiar tus clases y funciones en el mismo archivo.

Comprueba: No debe fallar al introducir abc como opción. Rechaza prestar dos veces L1 y devolver dos veces L1. 
L9 se informa como inexistente. Al salir termina el bucle. Los datos se pierden al reiniciar: todavía no hay persistencia.

Ampliación: Añade la opción 4 para listar solo los disponibles.
"""

# Copia aquí tus clases de los ejercicios anteriores que se necesitan.
# Escribe tu solución debajo.

from modelos_inicio import Biblioteca, Libro


def pedir_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero < 0:
                print("No puede ser negativo")
            else:
                return numero

        except ValueError:
            print("Escribe un entero")


def listar_libros(libros):
    if not libros:
        print("No hay libros para mostrar.")
    else:
        for libro in libros:
            print(f"{libro.codigo} - {libro.resumen()}")


# Creamos la biblioteca y añadimos los libros
biblioteca = Biblioteca()

biblioteca.agregar(Libro("L1", "Dune", autor="Frank Herbert"))
biblioteca.agregar(Libro("L2", "1984", autor="George Orwell"))


# Menú principal
while True:
    print("\n" + "=" * 35)
    print("       BIBLIOTECA DE CONSOLA")
    print("=" * 35)
    print("  1. Listar libros")
    print("  2. Prestar libro")
    print("  3. Devolver libro")
    print("  4. Listar libros disponibles")
    print("  0. Salir")
    print("=" * 35)

    opcion = pedir_entero("Selecciona una opción: ")
    print()

    if opcion == 1:
        listar_libros(biblioteca.libros)

    elif opcion == 2:
        codigo = input("Introduce el código del libro: ").strip()
        libro = biblioteca.buscar(codigo)

        if libro is None:
            print("\n" + "-" * 35)
            print("El libro no existe.")
            print("-" * 35 + "\n")

        elif biblioteca.prestar(codigo):
            print("\n" + "-" * 35)
            print("Libro prestado correctamente.")
            print("-" * 35 + "\n")

        else:
            print("\n" + "-" * 35)
            print("Operación rechazada: el libro ya está prestado.")
            print("-" * 35 + "\n")

    elif opcion == 3:
        codigo = input("Introduce el código del libro: ").strip()
        libro = biblioteca.buscar(codigo)

        if libro is None:
            print("\n" + "-" * 35)
            print("El libro no existe.")
            print("-" * 35 + "\n")

        elif biblioteca.devolver(codigo):
            print("\n" + "-" * 35)
            print("Libro devuelto correctamente.")
            print("-" * 35 + "\n")

        else:
            print("\n" + "-" * 35)
            print("Operación rechazada: el libro ya estaba disponible.")
            print("-" * 35 + "\n")

    elif opcion == 4:
        libros_disponibles = [
            libro for libro in biblioteca.libros
            if libro.disponible
        ]
        listar_libros(libros_disponibles)

    elif opcion == 0:
        print("\n" + "=" * 35)
        print("Saliendo de la biblioteca...")
        print("=" * 35)
        break

    else:
        print("\n" + "-" * 35)
        print("Opción inválida. Elige una opción del menú.")
        print("-" * 35 + "\n")
