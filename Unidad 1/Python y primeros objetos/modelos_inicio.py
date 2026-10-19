class Libro:
    """Modelo preparado para aprender a usar objetos."""
    def __init__(self, codigo, titulo, fecha=2026, autor=None):
        self.codigo = codigo
        self.titulo = titulo
        self.disponible = True
        self.fecha = fecha
        self.autor = autor

    def prestar(self):
        if not self.disponible:
            return False
        self.disponible = False
        return True

    def devolver(self):
        if self.disponible:
            return False
        self.disponible = True
        return True

    def resumen(self):
        if self.disponible:
            estado = "disponible"
        else:
            estado = "prestado"
        return f"{self.titulo}: {estado}"
    
class Biblioteca:
    def __init__(self):
        self.libros = []

    def buscar(self, codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                return libro
        return None

    def agregar(self, libro):
        if self.buscar(libro.codigo) is not None:
            return False

        self.libros.append(libro)
        return True

    def prestar(self, codigo):
        libro = self.buscar(codigo)

        if libro is None:
            return False

        return libro.prestar()

    def devolver(self, codigo):
        libro = self.buscar(codigo)

        if libro is None:
            return False

        return libro.devolver()

    def total_disponibles(self):
        total = 0

        for libro in self.libros:
            if libro.disponible:
                total += 1

        return total