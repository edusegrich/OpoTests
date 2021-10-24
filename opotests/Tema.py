class Tema:
    """
    Clase utilizada para representar un Tema de una Oposicion

    ...

    Attributes
    ----------
    id : int
        identificador del tema
    idOposicion : int
        identificador de la oposicion a la que pertenece el tema
    titulo : str
        titulo del tema
    descripcion : str
        descripcion del contenido del tema
    """

    def __init__(self, id, idOposicion, titulo, descripcion):
        self.id = id
        self.idOposicion = idOposicion
        self.titulo = titulo
        self.descripcion = descripcion
