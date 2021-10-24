class Pregunta:
    """
    Clase utilizada para representar una Pregunta de un Tema

    ...

    Attributes
    ----------
    id : int
        identificador de la pregunta
    idTema : int
        identificador del tema al que pertenece la pregunta
    enunciado : str
        enunciado de la pregunta
    respuestas : dict
        diferentes opciones de respuesta de la pregunta
    resp_correcta : int
        indice de la respuesta correcta en el diccionario de respuestas
    dificultad : str
        dificultad de la pregunta
    """

    def __init__(self, id, idTema, enunciado, respuestas, resp_correcta, dificultad):
        self.id = id
        self.idTema = idTema
        self.enunciado = enunciado
        self.respuestas = respuestas
        self.resp_correcta = resp_correcta
        self.dificultad = dificultad
