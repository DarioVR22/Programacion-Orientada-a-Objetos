from testigo import Testigo

testigo = Testigo("L20")
caja = [testigo]

copia = caja[0]

del testigo

print("A: la caja conserva", caja[0].codigo)

caja.clear()

print("B: la caja está vacía")

print(copia.codigo)

del copia
