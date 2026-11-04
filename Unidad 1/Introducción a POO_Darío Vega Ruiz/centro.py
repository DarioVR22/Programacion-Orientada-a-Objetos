
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "talleres.json")


# Clase Taller
class Taller:

    def __init__(self, codigo, nombre, capacidad):
        self.codigo = codigo
        self.nombre = nombre
        self.capacidad = capacidad
        self.inscritos = 0

    def inscribir(self):
        if self.inscritos < self.capacidad:
            self.inscritos += 1
            return True

        return False

    def cancelar(self):
        if self.inscritos > 0:
            self.inscritos -= 1
            return True

        return False

    def plazas_libres(self):
        return self.capacidad - self.inscritos


# Clase Centro
class Centro:

    def __init__(self):
        self.talleres = []

    def buscar(self, codigo):
        for taller in self.talleres:
            if taller.codigo == codigo:
                return taller

        return None

    def agregar(self, taller):
        if self.buscar(taller.codigo) is None:
            self.talleres.append(taller)
            return True

        return False

    def inscribir(self, codigo):
        taller = self.buscar(codigo)

        if taller is None:
            return False

        return taller.inscribir()

    def cancelar(self, codigo):
        taller = self.buscar(codigo)

        if taller is None:
            return False

        return taller.cancelar()

    def total_inscritos(self):
        total = 0

        for taller in self.talleres:
            total += taller.inscritos

        return total


# Función para guardar el centro
def guardar_centro(centro, ruta):
    datos = []

    for taller in centro.talleres:
        datos.append({
            "codigo": taller.codigo,
            "nombre": taller.nombre,
            "capacidad": taller.capacidad,
            "inscritos": taller.inscritos
        })

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)


# Función para cargar el centro
def cargar_centro(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        centro = Centro()

        for dato in datos:
            taller = Taller(
                dato["codigo"],
                dato["nombre"],
                dato["capacidad"]
            )

            centro.agregar(taller)

            for i in range(dato["inscritos"]):
                taller.inscribir()

        return centro

    except FileNotFoundError:
        centro = Centro()

        taller1 = Taller("T1", "Fotografía", 3)
        taller2 = Taller("T2", "Cerámica", 2)

        centro.agregar(taller1)
        centro.agregar(taller2)

        return centro


# Menú principal
def menu():
    centro = cargar_centro(RUTA)

    opcion = -1

    while opcion != 0:
        print("\n--- MENÚ CENTRO DE TALLERES ---")
        print("1. Listar talleres")
        print("2. Inscribir a una persona")
        print("3. Cancelar una inscripción")
        print("4. Consultar total de inscripciones")
        print("0. Guardar y salir")

        try:
            opcion = int(input("Elige una opción: "))

            if opcion == 1:
                print("\n--- TALLERES ---")

                for taller in centro.talleres:
                    print(
                        f"Código: {taller.codigo} | "
                        f"Nombre: {taller.nombre} | "
                        f"Inscritos: {taller.inscritos} | "
                        f"Plazas libres: {taller.plazas_libres()}"
                    )

            elif opcion == 2:
                codigo = input("Introduce el código del taller: ")

                taller = centro.buscar(codigo)

                if taller is None:
                    print("El taller no existe.")

                elif centro.inscribir(codigo):
                    print("Inscripción realizada correctamente.")

                else:
                    print("Operación rechazada. El taller está completo.")

            elif opcion == 3:
                codigo = input("Introduce el código del taller: ")

                taller = centro.buscar(codigo)

                if taller is None:
                    print("El taller no existe.")

                elif centro.cancelar(codigo):
                    print("Cancelación realizada correctamente.")

                else:
                    print("Operación rechazada. No hay inscripciones.")

            elif opcion == 4:
                print(
                    f"Total de inscripciones: "
                    f"{centro.total_inscritos()}"
                )

            elif opcion == 0:
                guardar_centro(centro, RUTA)
                print("Centro guardado. Hasta pronto.")

            else:
                print("Opción no válida.")

        except ValueError:
            print("Aviso: debes introducir una opción numérica.")


# Ejecutar el programa
if __name__ == "__main__":
    menu()


# Prueba realizada:
# Las tres primeras inscripciones en Fotografía se aceptan.
# La cuarta inscripción se rechaza porque el taller está completo.
# Cancelar una inscripción deja dos inscritos y una plaza libre.
# Cancelar sin inscripciones se rechaza.
# Buscar un código inexistente informa de que el taller no existe.
# El total de inscritos coincide con la suma de ambos talleres.
# Al guardar y volver a ejecutar, se conservan las inscripciones.
