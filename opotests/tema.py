class Tema:
    """
    Clase utilizada para representar un Tema de una Oposicion

    ...

    Attributes
    ----------
    titulo : str
        titulo del tema que servirá como identificador
    """

    def __init__(self, titulo):
        self.__titulo = titulo
    
    @property
    def titulo(self):
        """Devuelve el titulo del Tema"""
        return self.__titulo

    def __eq__(self, otro) -> bool:
        """
        Sobrecarga del operador == 
        Dos objetos de tipo Tema son iguales si su atributo 'titulo' es igual

        ...

        Parameters
        ----------
        otro : Tema / list
            objeto a comparar
        """
        if type(otro) is Tema:
            return self.__titulo == otro.titulo
        else:
            for o in otro:
                if self.__titulo == o.titulo:
                    return True
            return False

    def __ne__(self, otro) -> bool:
        return self.__titulo != otro.titulo
