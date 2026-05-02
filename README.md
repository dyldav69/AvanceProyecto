# Avance proyecto
Integrantes: Dylan Dávila - 506231047 y Julieta Lozano - 506241123

Para poder ejecutar el codigo debera seguir los siguientes pasos.

- Python -m venv env
- .\env\Scripts\activate
- pip install -r .\requirements.txt
- pip install langchain langchain-community langchain-text-splitters langchain-google-genai langchain-chroma chromadb python-dotenv unstructured pypdf
Y finalmente ejecute el rag.py y el taller.py.

## Descripción

Este proyecto consiste en el desarrollo de un asistente inteligente basado en inteligencia artificial que funciona utilizando la técnica **RAG (Retrieval Augmented Generation)**.  

El sistema permite consultar una base de conocimientos compuesta por documentos específicos y generar respuestas basadas en esa información. El objetivo es que el asistente pueda leer documentos, comprender el contenido y responder preguntas relacionadas con ellos.

El asistente funciona de manera local, lo que permite mantener la privacidad de los datos y evitar el uso de servicios externos.

---

## Tipo de Asistente

El asistente desarrollado en este proyecto es un **Tutor Académico Personalizado**.  

Está basado en material académico como guías de estudio, documentos o libros de una asignatura. Su función es ayudar a los estudiantes a comprender los temas del curso, responder preguntas y explicar conceptos utilizando la información disponible en los documentos.

Su objetivo es:

Explicar conceptos de bases de datos
Responder preguntas sobre SQL
Analizar consultas SQL
Limitar respuestas al dominio definido

---
# Flujo del sistema RAG

El sistema implementa las siguientes etapas:

1. Carga de documentos: Se carga un documento pdf desde archivos locales.

2. Fragmentación (Chunking): Los documentos se dividen en fragmentos para facilitar su procesamiento.

3. Vectorización (Embeddings): Cada fragmento se convierte en un vector numérico utilizando el modelo: gemini-embedding-001

4. Base de datos vectorial: Los vectores se almacenan en una base de datos local: ChromaDB.
Esto permite realizar búsquedas semánticas.

5. Recuperación de información (Retriever): Cuando el usuario realiza una pregunta:

- Se convierte en embedding
- Se buscan los fragmentos más similares
- Se recupera el contexto relevante

6. Generación de respuesta (LLM): El modelo genera la respuesta utilizando únicamente el contexto recuperado.


---

## Diseño de Prompts
Para mejorar el comportamiento del modelo se utilizaron diferentes técnicas de prompting.

### System Prompt
Se define un **system prompt** que establece el rol del asistente como tutor académico. Esto permite controlar la forma en la que el modelo responde a las preguntas del usuario.

### Few-Shot Prompting
Se incluyen ejemplos dentro del prompt para mostrar al modelo cómo debe responder. Esto ayuda a que las respuestas sigan un formato específico.

### Uso de Delimitadores
Se utilizan delimitadores como triple comillas (`"""`) para separar claramente el contexto, las instrucciones y la pregunta del usuario.

---

## Funcionamiento
El sistema funciona de la siguiente forma:

1. Se carga una base de documentos con información académica.
2. El usuario realiza una pregunta.
3. El sistema busca información relevante dentro de los documentos.
4. El modelo genera una respuesta utilizando el contexto encontrado.

---

## Tecnologías Utilizadas

- Python  
- Modelos de lenguaje (LLM)  
- Técnica RAG  
- Prompts estructurados  

---

## Autor
Proyecto desarrollado como parte de la asignatura de **Desarrollo de Aplicaciones con Inteligencia Artificial**.
