import random
from opotests.oposicion import Oposicion

class Examen:
    """
    Clase utilizada para representar un Examen
    
    ...

    Attributes
    ----------
    id : int
        identificador del examen
    oposicion : Oposicion
        oposicion a la que corresponde el examen
    preguntas : list
        lista que contiene las preguntas del examen
    """

    def __init__(self, id, oposicion, preguntas):
        self.__id = id

        if type(oposicion) is Oposicion:
            self.__oposicion = oposicion
        else:
            raise TypeError ("El atributo 'oposicion' debe ser del tipo Oposicion")

        self.__preguntas = []

        # Obtenemos una lista con solo preguntas del temario de la oposicion
        preguntas_candidatas = []
        for pregunta in preguntas:
            if pregunta.tema in oposicion.temas:
                preguntas_candidatas.append(pregunta)
        
        # Desordenamos las preguntas para obtener aleatoriedad en la generacion
        random.shuffle(preguntas_candidatas)

        # Generamos las preguntas del examen con preguntas de todo el temario
        numero_preguntas = oposicion.numero_preguntas

        while numero_preguntas > 0:
            for tema in oposicion.temas:
                if numero_preguntas <= 0:
                    break
                for pregunta in preguntas_candidatas:
                    if pregunta.tema == tema:
                        self.__preguntas.append(pregunta)
                        preguntas_candidatas.remove(pregunta)
                        numero_preguntas -= 1
                        break
                
        # Desordenamos las preguntas
        random.shuffle(self.__preguntas)

    @property
    def id(self):
        """Devuelve el identificador del examen"""
        return self.__id

    @property
    def oposicion(self):
        """Devuelve la oposición correspondiente al examen"""
        return self.__oposicion

    @property
    def preguntas(self):
        """Devuelve la lista de preguntas del examen"""
        return self.__preguntas
