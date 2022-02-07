from opotests.dificultad import Dificultad
from opotests.grupo import Grupo
from opotests.tema import Tema
from opotests.pregunta import Pregunta
from opotests.oposicion import Oposicion
from datetime import datetime

def importar_pregunta(ruta):
    """
    Funcion para obtener una pregunta de un fichero .txt

    Formato:
    id|tema|enunciado|respuestas|respuesta correcta|dificultad
    """
    with open(ruta, 'r') as fichero:
        pregunta = fichero.readline()
        pregunta = formatear_pregunta(pregunta)
    
    return Pregunta(pregunta[0], pregunta[1], pregunta[2], pregunta[3], pregunta[4], pregunta[5])

def importar_oposicion(ruta):
    """
    Funcion para obtener una pregunta de un fichero .txt

    Formato:
    titulo|grupo|lista temas|numero preguntas|fecha
    """
    with open(ruta, 'r') as fichero:
        oposicion = fichero.readline()
        oposicion = formatear_oposicion(oposicion)
    
    return Oposicion(oposicion[0], oposicion[1], oposicion[2], oposicion[3], oposicion[4])

def importar_preguntas(ruta):
    """
    Funcion para obtener las preguntas de un fichero .txt (una pregunta en cada linea) en una lista
    """
    with open(ruta, 'r') as fichero:
        preguntas = fichero.readlines()
        salida = []

        for p in preguntas:
            pregunta = formatear_pregunta(p)
            salida.append(Pregunta(pregunta[0], pregunta[1], pregunta[2], pregunta[3], pregunta[4], pregunta[5]))
    
    return salida

def formatear_pregunta(linea):
    """
    Funcion para ajustar los atributos de una pregunta
    """
    # Separamos los atributos
    pregunta = linea.split(sep='|')

    # Pasamos el 'id' a int
    pregunta[0] = int(pregunta[0])

    # Pasamos el 'tema' a un objeto de tipo Tema
    pregunta[1] = Tema(pregunta[1])

    # Pasamos las 'respuestas' a diccionario
    pregunta[3] = eval(pregunta[3])

    # Pasamos la 'resp_correcta' a int
    pregunta[4] = int(pregunta[4])

    # Pasamos la 'dificultad' a un objeto de tipo Dificultad
    pregunta[-1] = pregunta[-1].replace('\n', '')
    pregunta[-1] = dificultad(pregunta[-1])

    return pregunta

def formatear_oposicion(linea):
    """
    Funcion para ajustar los atributos de una oposicion
    """
    oposicion = linea.split(sep='|')

    # Pasamos el 'grupo' a un objeto de tipo Grupo
    oposicion[1] = grupo(oposicion[1])

    # Obtenemos los titulos de los temas y construimos una lista de objetos de tipo Tema
    lista_temas = eval(oposicion[2])
    oposicion[2] = []
    for titulo_tema in lista_temas:
        oposicion[2].append(Tema(titulo_tema))

    # Pasamos el 'numero_preguntas' a int
    oposicion[3] = int(oposicion[3])

    # Pasamos la fecha a un objeto de tipo Date
    oposicion[4] = datetime.strptime(oposicion[4], "%Y-%m-%d")

    return oposicion

def dificultad(str):
    """
    Funcion para pasar un string a objeto de tipo Dificultad
    """
    dificultades = { 'Alto': Dificultad.Alto, 
                     'Medio': Dificultad.Medio, 
                     'Bajo': Dificultad.Bajo}
    return dificultades[str]

def grupo(str):
    """
    Funcion para pasar un string a objeto de tipo Grupo
    """
    grupos = { 'A1': Grupo.A1, 
               'A2': Grupo.A2, 
               'B': Grupo.B,
               'C1': Grupo.C1, 
               'C2': Grupo.C2, 
               'E': Grupo.E}
    return grupos[str]
