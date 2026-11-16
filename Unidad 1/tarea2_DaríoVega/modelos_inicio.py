class Libro:
    """Modelo preparado para aprender a usar objetos."""

    def __init__(self, codigo, titulo, fecha=2026, autor=None):
        if not self.codigo_valido(codigo):
            raise ValueError("Código inválido. Debe tener formato L01-L99.")

        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("El título no puede estar vacío.")

        self.codigo = codigo
        self.titulo = titulo.strip()
        self._disponible = True
        self.fecha = fecha
        self.autor = autor

    @staticmethod
    def codigo_valido(texto):
        if not isinstance(texto, str):
            return False

        if len(texto) != 3:
            return False

        if texto[0] != "L":
            return False

        if not all(c in "0123456789" for c in texto[1:]):
            return False

        return 1 <= int(texto[1:]) <= 99

    @classmethod
    def desde_linea(cls, linea):
        if not isinstance(linea, str) or ";" not in linea:
            raise ValueError("La línea debe contener un punto y coma.")

        codigo, titulo = linea.split(";", 1)

        return cls(codigo.strip(), titulo.strip())

    @property
    def disponible(self):
        return self._disponible

    def prestar(self):
        if not self.disponible:
            return False

        self._disponible = False
        return True

    def devolver(self):
        if self.disponible:
            return False

        self._disponible = True
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