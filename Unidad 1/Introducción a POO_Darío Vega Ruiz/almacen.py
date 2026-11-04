
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "almacen.json")


# Clase Producto
class Producto:

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = 0

    def reponer(self, cantidad):
        if type(cantidad) is int and cantidad > 0:
            self.stock += cantidad
            return True

        return False

    def vender(self, cantidad):
        if type(cantidad) is int and cantidad > 0 and cantidad <= self.stock:
            self.stock -= cantidad
            return True

        return False


# Clase Almacen
class Almacen:

    def __init__(self):
        self.productos = []

    def buscar(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None

    def agregar(self, producto):
        if self.buscar(producto.codigo) is None:
            self.productos.append(producto)
            return True

        return False

    def reponer(self, codigo, cantidad):
        producto = self.buscar(codigo)

        if producto is None:
            return False

        return producto.reponer(cantidad)

    def vender(self, codigo, cantidad):
        producto = self.buscar(codigo)

        if producto is None:
            return False

        return producto.vender(cantidad)


# Función para guardar el almacén
def guardar_almacen(almacen, ruta):
    datos = []

    for producto in almacen.productos:
        datos.append({
            "codigo": producto.codigo,
            "nombre": producto.nombre,
            "stock": producto.stock
        })

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)


# Función para cargar el almacén
def cargar_almacen(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        almacen = Almacen()

        for dato in datos:
            producto = Producto(dato["codigo"], dato["nombre"])
            almacen.agregar(producto)

            if dato["stock"] > 0:
                producto.reponer(dato["stock"])

        return almacen

    except FileNotFoundError:
        almacen = Almacen()

        producto1 = Producto("P1", "Cuaderno")
        producto2 = Producto("P2", "Bolígrafo")

        almacen.agregar(producto1)
        almacen.agregar(producto2)

        producto1.reponer(10)
        producto2.reponer(20)

        return almacen


# Menú principal
def menu():
    almacen = cargar_almacen(RUTA)

    opcion = -1

    while opcion != 0:
        print("\n--- MENÚ ALMACÉN ---")
        print("1. Listar productos y existencias")
        print("2. Reponer unidades")
        print("3. Vender unidades")
        print("0. Guardar y salir")

        try:
            opcion = int(input("Elige una opción: "))

            if opcion == 1:
                print("\n--- PRODUCTOS ---")

                for producto in almacen.productos:
                    print(
                        f"Código: {producto.codigo} | "
                        f"Nombre: {producto.nombre} | "
                        f"Stock: {producto.stock}"
                    )

            elif opcion == 2:
                codigo = input("Introduce el código del producto: ")

                try:
                    cantidad = int(input("Introduce la cantidad a reponer: "))

                    producto = almacen.buscar(codigo)

                    if producto is None:
                        print("El producto no existe.")

                    elif almacen.reponer(codigo, cantidad):
                        print("Reposición realizada correctamente.")

                    else:
                        print("Operación rechazada.")

                except ValueError:
                    print("Aviso: debes introducir un número entero.")

            elif opcion == 3:
                codigo = input("Introduce el código del producto: ")

                try:
                    cantidad = int(input("Introduce la cantidad a vender: "))

                    producto = almacen.buscar(codigo)

                    if producto is None:
                        print("El producto no existe.")

                    elif almacen.vender(codigo, cantidad):
                        print("Venta realizada correctamente.")

                    else:
                        print("Operación rechazada.")

                except ValueError:
                    print("Aviso: debes introducir un número entero.")

            elif opcion == 0:
                guardar_almacen(almacen, RUTA)
                print("Almacén guardado. Hasta pronto.")

            else:
                print("Opción no válida.")

        except ValueError:
            print("Aviso: debes introducir una opción numérica.")


# Ejecutar el programa
if __name__ == "__main__":
    menu()


# Prueba realizada:
# Partiendo de 10 cuadernos, vender 3 deja 7.
# Intentar vender 8 se rechaza y siguen quedando 7.
# Reponer 5 deja 12.
# Vender 0 o una cantidad negativa se rechaza.
# Buscar P9 informa de que no existe.
# Al guardar y volver a ejecutar, se conservan las 12 unidades.
