class Pregunta:
    """
    Clase utilizada para representar una Pregunta de un Tema

    ...

    Attributes
    ----------
    id : int
        identificador de la pregunta
    tema : int
        tema al que pertenece la pregunta
    enunciado : str
        enunciado de la pregunta
    respuestas : dict
        diferentes opciones de respuesta de la pregunta
    resp_correcta : int
        indice de la respuesta correcta en el diccionario de respuestas
    dificultad : str
        dificultad de la pregunta
    """

    def __init__(self, id, tema, enunciado, respuestas, resp_correcta, dificultad):
        self.__id = id
        self.__tema = tema
        self.__enunciado = enunciado
        self.__respuestas = respuestas
        self.__resp_correcta = resp_correcta
        self.__dificultad = dificultad

    @property
    def id(self):
        """Devuelve el identificador de la Pregunta"""
        return self.__id
    
    def add_respuesta(self, respuesta):
        """Añade una opción de respuesta a la Pregunta"""
        pass