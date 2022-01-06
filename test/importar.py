from opotests.dificultad import Dificultad
from opotests.grupo import Grupo
from opotests.tema import Tema
from datetime import date, datetime

def importar_pregunta(ruta):
    """
    Funcion para obtener una pregunta de un fichero .txt

    Formato:
    id|tema|enunciado|respuestas|respuesta correcta|dificultad
    """
    with open(ruta, 'r') as fichero:
        pregunta = fichero.readline()
        salida = pregunta.split(sep='|')

        # Pasamos el 'id' a int
        salida[0] = int(salida[0])

        # Pasamos las 'respuestas' a diccionario
        salida[3] = eval(salida[3])

        # Pasamos la 'resp_correcta' a int
        salida[4] = int(salida[4])

        # Pasamos la 'dificultad' a un objeto de tipo Dificultad
        salida[-1] = dificultad(salida[-1])
    
    return salida

def importar_oposicion(ruta):
    """
    Funcion para obtener una pregunta de un fichero .txt

    Formato:
    titulo|grupo|lista temas|fecha
    """
    with open(ruta, 'r') as fichero:
        pregunta = fichero.readline()
        salida = pregunta.split(sep='|')

        # Pasamos el 'grupo' a un objeto de tipo Grupo
        salida[1] = grupo(salida[1])

        # Obtenemos los titulos de los temas y construimos una lista de objetos de tipo Tema
        lista_temas = list(salida[2])
        salida[2] = []
        for titulo_tema in lista_temas:
            salida[2].append(Tema(titulo_tema))

        # Pasamos la fecha a un objeto de tipo Date
        salida[3] = datetime.strptime(salida[3], "%Y-%m-%d")
    
    return salida

def importar_preguntas(ruta):
    """
    Funcion para obtener las preguntas de un fichero .txt (una pregunta en cada linea)
    """
    with open(ruta, 'r') as fichero:
        preguntas = fichero.readlines()
        salida = []

        for p in preguntas:
            pregunta = p.split(sep='|')
            salida.append(pregunta)
    
    return salida

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
    