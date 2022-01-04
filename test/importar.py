import os

def importar_pregunta(ruta):
    """
    Funcion para obtene una pregunta de un fichero .txt
    """
    with open(ruta, 'r') as fichero:
        pregunta = fichero.readline()
        salida = pregunta.split(sep=',')
    
    return salida

def importar_preguntas(ruta):
    """
    Funcion para obtener las preguntas de un fichero .txt (una pregunta en cada linea)
    """
    with open(ruta, 'r') as fichero:
        preguntas = fichero.readlines()
        salida = []

        for p in preguntas:
            pregunta = p.split(sep=',')
            salida.append(pregunta)
    
    return salida