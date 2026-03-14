# Tutor Académico con Prompt Engineering + Few Shot + Delimitadores

import os
from google import genai
from dotenv import load_dotenv


# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")


# 2. Inicializar el Cliente
client = genai.Client(api_key=clave_api)


# 3. Historial de conversación
historial = []


# 4. Base de conocimiento (simulación RAG)
base_conocimiento = """
Conceptos básicos de Bases de Datos

- Una base de datos es un sistema que permite almacenar información organizada.
- SQL es el lenguaje para consultar y manipular bases de datos.
- Una clave primaria identifica de manera única cada registro.
- Una clave foránea permite relacionar dos tablas.
- SELECT se usa para consultar datos.
- FROM indica la tabla origen.
- WHERE permite filtrar resultados.
"""


# 5. Prompt base con reglas + Few-Shot + delimitadores
prompt_base = f"""
<SYSTEM_PROMPT>

Eres un Tutor Académico especializado en Bases de Datos.

REGLAS:

1. Explica conceptos de forma clara.
2. Usa ejemplos sencillos.
3. Si el estudiante muestra SQL, analiza posibles errores.
4. No inventes información fuera del contexto.
5. Si la pregunta no es de bases de datos responde:
   "La pregunta está fuera del dominio del asistente".

FORMATO DE RESPUESTA (usar siempre):

### Explicación
### Ejemplo
### Pregunta de Reflexión

</SYSTEM_PROMPT>

<CONTEXTO>
{base_conocimiento}
</CONTEXTO>

<FEW_SHOT>

Estudiante: ¿Qué es una clave primaria?

Tutor:

### Explicación
Una clave primaria es un campo que identifica de forma única cada registro en una tabla.

### Ejemplo
En una tabla de estudiantes, el número de identificación puede ser la clave primaria.

### Pregunta de Reflexión
¿Qué problema ocurriría si dos registros tuvieran la misma clave primaria?

---

Estudiante: SELECT nombre estudiantes

Tutor:

### Explicación
La consulta parece intentar obtener nombres, pero puede faltar una cláusula importante.

### Ejemplo
En SQL normalmente se indica la tabla usando una cláusula específica.

### Pregunta de Reflexión
¿Qué cláusula se usa para indicar la tabla de donde se obtienen los datos?

</FEW_SHOT>
"""


# 6. Función principal del tutor
def tutor():

    print("📚 Tutor Académico de Bases de Datos")
    print("Escribe 'salir' para terminar.\n")

    while True:

        entrada_usuario = input("👨‍🎓 Estudiante: ")

        if entrada_usuario.lower() == "salir":
            break

        historial.append(f"Estudiante: {entrada_usuario}")

        # limitar historial para no gastar demasiados tokens
        historial_reciente = historial[-6:]

        # construir contexto
        contexto = (
            prompt_base
            + "\n\n<CONVERSACION>\n"
            + "\n".join(historial_reciente)
            + "\nTutor:"
        )

        try:

            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=contexto
            )

            respuesta = response.text

            print("\n👨‍🏫 Tutor:\n")
            print(respuesta)
            print("\n" + "-" * 40)

            historial.append(f"Tutor: {respuesta}")

        except Exception as e:
            print(f"\n❌ Error en la conexión: {e}")


# 7. Ejecutar tutor
tutor()
