"""Ejercicio 13 — Métodos que cumplen una regla

Añade prestar y devolver a tu clase. prestar devuelve True y cambia disponible a False solo si estaba disponible. 
En caso contrario devuelve False y conserva el estado. devolver hace la operación inversa y también informa con un booleano. 
Usa la clase en cuatro llamadas: prestar, prestar, devolver, devolver.

Comprueba: Las llamadas devuelven True, False, True, False. El estado final es disponible. 
Un intento rechazado no altera el objeto.

Ampliación: Añade resumen, equivalente a etiqueta del ejercicio 11 pero sin parámetro libro: usa self.
"""

# Escribe tu solución debajo.
from modelos_inicio import Libro

# Creamos un libro
L1 = Libro(1, "Dune", autor="Frank Herbert")

# Probamos las cuatro llamadas
print(L1.prestar())   # True
print(L1.prestar())   # False
print(L1.devolver())  # True
print(L1.devolver())  # False

# Comprobamos el estado final
print(L1.resumen())