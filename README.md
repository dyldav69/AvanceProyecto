# Avance proyecto
Integrantes: Dylan Dávila - 506231047 y Julieta Lozano - 506241123

Para poder ejecutar el codigo debera seguir los siguientes pasos.

Primero ejecute el comando: Python -m venv env
Luego ejecute el comando:.\env\Scripts\activate
Y finalmente ejecute el comando: pip install -r .\requirements.txt
Al ejecutarse deberá verse así cada punto del ejercicio:

## Descripción

Este proyecto consiste en el desarrollo de un asistente inteligente basado en inteligencia artificial que funciona utilizando la técnica **RAG (Retrieval Augmented Generation)**.  

El sistema permite consultar una base de conocimientos compuesta por documentos específicos y generar respuestas basadas en esa información. El objetivo es que el asistente pueda leer documentos, comprender el contenido y responder preguntas relacionadas con ellos.

El asistente funciona de manera local, lo que permite mantener la privacidad de los datos y evitar el uso de servicios externos.

---

## Tipo de Asistente

El asistente desarrollado en este proyecto es un **Tutor Académico Personalizado**.  

Está basado en material académico como guías de estudio, documentos o libros de una asignatura. Su función es ayudar a los estudiantes a comprender los temas del curso, responder preguntas y explicar conceptos utilizando la información disponible en los documentos.

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
