class Obra: 
    def __init__ (self, id_obra, titulo, artista, departamento, tipo, anio, imagen_url):
        self.id_obra=id_obra
        self.titulo=titulo
        self.artista=artista
        self.departamento=departamento
        self.tipo=tipo
        self.anio=anio
        self.imagen_url=imagen_url

    def show(self):
        print(f"Id obra: {self.id_obra}")
        print(f"Titulo de obra: {self.titulo}")
        print(f"Artista de la obra: {self.artista}")
        print(f"Departamento: {self.departamento}")
        print(f"Tipo de obra: {self.tipo}")
        print(f"Anio de publicacion: {self.anio}")
        print(f"Imagen: {self.imagen_url}")
