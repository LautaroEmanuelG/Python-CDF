class Libro:
    def __init__(self, titulo, autor, año_publicacion, unidades, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.unidades = unidades
        self.disponible = disponible