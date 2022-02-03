from conftest import *

oposicion = importar_oposicion('test/oposiciones.txt')
preguntas = importar_preguntas('test/preguntas.txt')
examen = Examen(1, oposicion, preguntas)

print("INFORMACION DE LA OPOSICION")
print("Titulo Oposicion: " + examen.oposicion.titulo)
print("Grupo: " + str(examen.oposicion.grupo))
print("Temas:")
for tema in examen.oposicion.temas:
    print("\t- " + tema.titulo)

print()
print("CONTENIDO DEL EXAMEN")
print("Preguntas examen:")
for p in examen.preguntas:
    print("\t- " + "[" + p.tema.titulo + "] " + p.enunciado)
    for c in p.respuestas:
        print("\t\t " + str(c) + ". " + p.respuestas[c])
    print()
