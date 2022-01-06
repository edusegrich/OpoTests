import pytest
from opotests.dificultad import Dificultad
from opotests.grupo import Grupo
from opotests.tema import Tema
from opotests.pregunta import Pregunta
from opotests.oposicion import Oposicion
from datetime import date, datetime
from assertpy import add_extension

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
        lista_temas = eval(salida[2])
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
    
@pytest.fixture
def pregunta():
    datos_pregunta = importar_pregunta('test/preguntas.txt')
    return Pregunta(datos_pregunta[0], datos_pregunta[1], datos_pregunta[2], datos_pregunta[3], datos_pregunta[4], datos_pregunta[5])

@pytest.fixture
def oposicion():
    datos_oposicion= importar_oposicion('test/oposiciones.txt')
    return Oposicion(datos_oposicion[0], datos_oposicion[1], datos_oposicion[2], datos_oposicion[3])

def esta_entre_los_temas(self, lista):
    """
    Extension de assertpy para verificar si un tema (titulo) esta entre los temas de una lista
    """
    esta = False
    for tema in lista:
        if self.val == tema.titulo:
            esta = True
            break
    if esta == False:
        self.error(f'{self.val} no esta')

    return self

# Añadimos la extension
add_extension(esta_entre_los_temas)

def esta_entre_las_claves(self, diccionario):
    """
    Extension de assertpy para verificar si un valor esta entre las claves de un diccionario
    """
    esta = False
    for key in diccionario.keys():
        if self.val == key:
            esta = True
            break
    if esta == False:
        self.error(f'{self.val} no esta')

    return self

# Añadimos la extension
add_extension(esta_entre_las_claves)
