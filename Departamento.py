class Departamento:
  def __init__ (self, id, nombre):
    self.id=id
    self.nombre=nombre

  def show(self):
    print(f"Id: {self.id}")
    print(f"Nombre del departamento: {self.nombre}")

