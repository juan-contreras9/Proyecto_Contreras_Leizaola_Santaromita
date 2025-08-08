class Artista:
    def __init__ (self, nombre, nacionalidad, fecha_de_nacimiento, fecha_de_muerte):
        self.nombre=nombre
        self.nacionalidad=nacionalidad
        self.fecha_de_nacimiento=fecha_de_nacimiento
        self.fecha_de_muerte=fecha_de_muerte

    def show(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Fecha de nacimiento: {self.fecha_de_nacimiento}")
        print(f"Fecha de muerte: {self.fecha_de_muerte}")

