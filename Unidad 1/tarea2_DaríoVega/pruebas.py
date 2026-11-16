from modelos_inicio import Libro

libro = Libro("L14", "Atlas")
inventario = [libro]
mostrador = libro

del libro

mostrador.prestar()
print(inventario[0].disponible)

del mostrador

print(inventario[0].titulo)

inventario.clear()