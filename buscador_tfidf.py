import numpy as np

# Dataset del reglamento
documents = [
    "la asistencia minima requerida es del 80 por ciento",
    "las faltas disciplinarias se clasifican en leves graves y gravisimas",
    "la perdida de cupo ocurre por promedio inferior a 3 0",
    "el estudiante puede cancelar materias hasta la semana 8",
    "se pueden solicitar examenes supletorios dentro de tres dias",
    "el plagio es considerado una falta grave",
    "las matriculas deben pagarse antes de la fecha limite",
    "los estudiantes tienen derecho a tutorias academicas",
    "las becas se asignan al mejor promedio",
    "la cancelacion de semestre debe hacerse antes de la semana 10"
]

#consulta = "becas promedio"
#consulta = "faltas graves"
consulta = "cancelacion semestre"

N = len(documents)

terminos = consulta.split()

scores = []

for i, doc in enumerate(documents):
    tf_idf_total = 0

    for termino in terminos:
        df = sum(1 for d in documents if termino in d)

        if df == 0:
            continue
        idf = np.log(N / df)
        tf = doc.split().count(termino) / len(doc.split())
        tf_idf_total += tf * idf

    scores.append((i+1, tf_idf_total, doc))

scores.sort(key=lambda x: x[1], reverse=True)

print(f"\nConsulta: {consulta}\n")

for i, (doc_id, score, doc) in enumerate(scores[:3], 1):
    print(f"{i}. Documento {doc_id}: {doc}")
    print(f"   Score: {score:.4f}\n")
palabras = set(" ".join(documents).split())

idf_lista = []

for palabra in palabras:
    df = sum(1 for doc in documents if palabra in doc)

    if df > 0:
        idf = np.log(N / df)
        idf_lista.append((palabra, idf))

idf_lista.sort(key=lambda x: x[1], reverse=True)

top_5_altos = idf_lista[:5]
top_5_bajos = idf_lista[-5:]

print("5 PALABRAS CON IDF MÁS ALTO")

for palabra, valor in top_5_altos:
    print(f"{palabra} -> {valor:.4f}")

print("\n5 PALABRAS CON IDF MÁS BAJO")

for palabra, valor in top_5_bajos:
    print(f"{palabra} -> {valor:.4f}")