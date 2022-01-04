from opotests.dificultad import Dificultad

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
    dificultad : Dificultad
        dificultad de la pregunta
    """

    def __init__(self, id, tema, enunciado, respuestas, resp_correcta, dificultad):
        self.__id = id
        self.__tema = tema
        self.__enunciado = enunciado
        self.__respuestas = respuestas
        self.__resp_correcta = resp_correcta

        if type(dificultad) is Dificultad:
            self.__dificultad = dificultad
        else:
            raise TypeError("El atributo 'dificultad' debe ser de tipo Dificultad")

    @property
    def id(self):
        """Devuelve el identificador de la Pregunta"""
        return self.__id

    @property
    def tema(self):
        """Devuelve el tema de la Pregunta"""
        return self.__tema

    @property
    def respuestas(self):
        """Devuelve las respuestas de la Pregunta"""
        return self.__respuestas

    @property
    def resp_correcta(self):
        """Devuelve la respuesta correcta de la Pregunta"""
        return self.__resp_correcta

    @property
    def dificultad(self):
        """Devuelve la dificultad de la Pregunta"""
        return self.__dificultad
    
    def add_respuesta(self, respuesta):
        """Añade una opción de respuesta a la Pregunta"""
        pass
