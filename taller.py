import os
from google import genai
from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

# -------- CONFIG --------
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

# -------- EMBEDDINGS + VECTOR DB --------
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=API_KEY
)

vector_store = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

retriever = vector_store.as_retriever(search_kwargs={"k": 4})

# -------- HISTORIAL --------
historial = []

# -------- FILTRO DE DOMINIO --------
def es_pregunta_bd(texto):
    palabras_clave = [
        "sql", "base de datos", "tabla", "select",
        "where", "join", "clave", "primary",
        "foreign", "insert", "update", "delete"
    ]
    texto = texto.lower()
    return any(p in texto for p in palabras_clave)

# -------- PROMPT --------
prompt_base = """
<SYSTEM_PROMPT>

Eres un Tutor Académico especializado en Bases de Datos.

REGLAS:

1. Explica de forma clara.
2. Usa ejemplos simples.
3. Analiza errores en SQL si aparecen.
4. Usa SOLO la información del CONTEXTO RAG.
5. No inventes información.
6. Si no hay suficiente información di:
   "No encontré información en los documentos".

FORMATO OBLIGATORIO:

### Explicación
### Ejemplo
### Pregunta de Reflexión

</SYSTEM_PROMPT>
"""

# -------- FUNCIÓN PRINCIPAL --------
def tutor():

    print("📚 Tutor Académico con RAG (Bases de Datos)")
    print("Escribe 'salir' para terminar.\n")

    while True:

        pregunta = input("👨‍🎓 Estudiante: ")

        if pregunta.lower() == "salir":
            break

        # -------- FILTRO --------
        if not es_pregunta_bd(pregunta):
            print("\n👨‍🏫 Tutor:\n")
            print("La pregunta está fuera del dominio del asistente")
            print("\n" + "-" * 40)
            continue

        # -------- RAG --------
        docs = retriever.invoke(pregunta)
        contexto_rag = "\n\n".join([doc.page_content for doc in docs])

        # -------- DEBUG OPCIONAL --------
        print("\n🔎 Fragmentos recuperados:")
        for i, doc in enumerate(docs, 1):
            print(f"[{i}] {doc.page_content[:120]}...")

        # -------- HISTORIAL --------
        historial.append(f"Estudiante: {pregunta}")
        historial_reciente = historial[-6:]

        # -------- PROMPT FINAL --------
        prompt = (
            prompt_base
            + "\n<CONTEXTO>\n"
            + contexto_rag
            + "\n</CONTEXTO>\n"
            + "\n<CONVERSACION>\n"
            + "\n".join(historial_reciente)
            + "\nTutor:"
        )

        try:
            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )

            respuesta = response.text

            print("\n👨‍🏫 Tutor:\n")
            print(respuesta)
            print("\n" + "-" * 40)

            historial.append(f"Tutor: {respuesta}")

        except Exception as e:
            print(f"\n❌ Error: {e}")

# -------- EJECUTAR --------
tutor()