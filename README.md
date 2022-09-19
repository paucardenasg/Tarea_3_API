# Tarea_3_API
Este repositorio contiene la tarea 3 de la materia Proyecto de Ciencia de Datos. Además de este archivo README.md, el repositorio contiene un archivo de Python con el código para la API y un archivo de texto con los requisitos necesarios para ejecutar el código correctamente.

Se siguieron las instrucciones a continuación:
+ Crear una nueva API, la cual contenga cuatro *endpoints* con las siguientes consideraciones:
  1. Un endpoint para crear un diccionario en donde las llaves de dicho diccionario sea un ID de tipo entero como identificador único para una lista de usuarios. El valor de dicha llave será otro diccionario con la siguiente estructura:
    {"user_name": "name",
     "user_id": id,
     "usar_email": "email",
     "age": age,
     "recommendations": list[str],
     "ZIP" (optional): ZIP
    }
  Cada vez que se haga un request a ese endpoint, se debe actualizar el diccionario. La respuesta de este endpoint debe enviar el ID del usuario creado y una descripción de 'usuario creado exitosamente'.
  2. Si se envía datos con un ID ya existente, se debe regresar un mensaje de error que mencione este hecho.
  3. Un endpoint para actualizar la información de un usuario específico buscándolo por ID. Si el ID no existe, debe regresar un mensaje de error que mencione este hecho.
  4. Un endpoint para obtener la información de un usuario específico buscándolo por ID. Si el ID no existe, debe regresar un mensaje de error que mencione este hecho.
  5. Un endpoint para eliminar la información de un usuario específico buscándolo por ID. Si el ID no existe, debe regresar un mensaje de error que mencione este hecho.
