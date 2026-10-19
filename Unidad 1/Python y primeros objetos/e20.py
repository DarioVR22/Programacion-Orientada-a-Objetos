"""Ejercicio 20 — La misma llamada con respuestas distintas

Extensión opcional de RA2. Crea Material con titulo y descripcion(), que devuelve el título. 
LibroPapel y Revista heredan de Material y redefinen descripcion para anteponer "Libro: " y "Revista: ". 
Recorre una lista con un objeto de cada tipo y llama a descripcion sin comprobar su tipo.

Comprueba: La misma llamada produce "Libro: Dune" y "Revista: Ciencia". El bucle no conoce los detalles de cada clase.

Ampliación: Añade AudioLibro y comprueba que funciona en el mismo bucle sin modificarlo.
"""
# Escribe tu solución debajo.

class Material:
    def __init__(self, titulo):
        self.titulo = titulo

    def descripcion(self):
        return self.titulo


class LibroPapel(Material):
    def descripcion(self):
        return f"Libro: {self.titulo}"


class Revista(Material):
    def descripcion(self):
        return f"Revista: {self.titulo}"


class AudioLibro(Material):
    def descripcion(self):
        return f"AudioLibro: {self.titulo}"


# Creamos una lista con diferentes tipos de materiales
materiales = [
    LibroPapel("Dune"),
    Revista("Ciencia"),
    AudioLibro("El principito")
]

# Polimorfismo: misma llamada, diferentes respuestas
for material in materiales:
    print(material.descripcion())