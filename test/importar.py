from opotests.dificultad import Dificultad

def importar_pregunta(ruta):
    """
    Funcion para obtene una pregunta de un fichero .txt
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
    Funcion para pasar un string a objeto de tipo dificultad
    """
    dificultades = { 'Alto': Dificultad.Alto, 
                     'Medio': Dificultad.Medio, 
                     'Bajo': Dificultad.Bajo}
    return dificultades[str]