from opotests.grupo import Grupo
from datetime import datetime

class Oposicion:
    """
    Clase utilizada para representar una Oposicion

    ...

    Attributes
    ----------
    titulo : str
        titulo de la oposición que servirá como identificador
    grupo : Grupo
        grupo de la oposición
    temas : list
        lista que contiene los temas que componen la oposición
    numero_preguntas : int
        numero de preguntas con las que se evalua en los examenes de la oposicion
    fecha : datetime
        fecha en la que tendrá lugar el examen de la oposición
    """

    def __init__(self, titulo, grupo, temas, numero_preguntas, fecha):
        self.__titulo = titulo

        if type(grupo) is Grupo:
            self.__grupo = grupo
        else:
            raise TypeError ("El atributo 'grupo' debe ser del tipo Grupo")
        
        self.__temas = temas

        self.__numero_preguntas = numero_preguntas

        if type(fecha) is datetime:
            self.__fecha = fecha
        else:
            raise TypeError ("El atributo 'fecha' debe ser del tipo datetime")
    
    @property
    def titulo(self):
        """Devuelve el titulo de la Oposición"""
        return self.__titulo

    @property
    def grupo(self):
        """Devuelve el grupo de la Oposición"""
        return self.__grupo

    @property
    def temas(self):
        """Devuelve los temas de la Oposición"""
        return self.__temas

    @property
    def numero_preguntas(self):
        """Devuelve el numero de preguntas con las que se evalua en la Oposición"""
        return self.__numero_preguntas

    @property
    def fecha(self):
        """Devuelve la fecha de la Oposición"""
        return self.__fecha

    def add_tema(self, tema):
        """Añade un tema al temario de la Oposición"""
        pass
