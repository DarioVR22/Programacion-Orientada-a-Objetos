class Testigo:
    def __init__(self, codigo):
        self.codigo = codigo
        if self.codigo == "L20":
            print("Alta L20")

    def __del__(self):
        print(f"Fin {self.codigo}")
