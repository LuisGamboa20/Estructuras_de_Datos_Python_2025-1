import requests
import os

clave_api = os.getenv("MIMO_OPENAI_API_KEY")
url = "https://ai.mimo.org/v1/openai/message"
encabezados = {"api-key": clave_api}

def enviar_mensaje(mensaje_usuario, id_hilo):
    cuerpo = {"message": mensaje_usuario}
    if id_hilo:
        cuerpo["threadId"] = id_hilo
    respuesta = requests.post(url, headers=encabezados, json=cuerpo)
    return respuesta.json()

id_hilo_actual = None

print("¡Bienvenido! Escribe tu mensaje y presiona Enter para enviarlo.")
print("Escribe 'salir' para terminar el programa.")
print("Escribe 'nuevo' para cambiar de hilo de conversación.")
print("Iniciando un nuevo hilo para ti.\n")

while True:
    mensaje_usuario = input("Tú: ")
    if mensaje_usuario.lower() == "salir":
        break
    elif mensaje_usuario.lower() == "nuevo":
        id_hilo_actual = None
        print("Se ha iniciado un nuevo hilo.")
        continue

    datos_respuesta = enviar_mensaje(mensaje_usuario, id_hilo_actual)
    ultimo_mensaje = datos_respuesta.get("response")
    id_hilo_actual = datos_respuesta.get("threadId")
    print(f"GPT: {ultimo_mensaje}")