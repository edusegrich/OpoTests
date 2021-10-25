class Tema:
    """
    Clase utilizada para representar un Tema de una Oposicion

    ...

    Attributes
    ----------
    id : int
        identificador del tema
    titulo : str
        titulo del tema
    descripcion : str
        descripcion del contenido del tema
    """

    def __init__(self, id, titulo, descripcion):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
