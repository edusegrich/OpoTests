class Oposicion:
    """
    Clase utilizada para representar una Oposicion

    ...

    Attributes
    ----------
    id : int
        identificador de la oposicion
    idsTemas : list
        lista que contiene los ids de los temas que componen la oposicion
    titulo : str
        titulo de la oposicion
    descripcion : str
        descripcion  de la oposicion
    """

    def __init__(self, id, idsTemas, titulo, descripcion):
        self.id = id
        self.idsTemas = idsTemas
        self.titulo = titulo
        self.descripcion = descripcion
