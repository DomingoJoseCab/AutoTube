# ==============================================================================
# AutoTube Script
# Creado por: Domingo Caballero
# Canal de YouTube: https://www.youtube.com/@emprendedomingo?=sub_confirmation=1
# Lista de Correo: https://emprendecondomingo.substack.com/
# ==============================================================================

from openai import OpenAI
import requests
import os

CLIENT = None
MODELO_IMG = None
FOLDER_PATH = None

def set_up_generate_miniature(client, modelo, folder_path):
    global CLIENT, MODELO_IMG, FOLDER_PATH
    CLIENT = client
    MODELO_IMG = modelo
    FOLDER_PATH = folder_path

def guardar_imagen(url, path):
    respuesta = requests.get(url)
    respuesta.raise_for_status()

    with open(path, 'wb') as file:
        file.write(respuesta.content)

def get_prompt_miniature(prompt, data):
    return prompt.replace('{PRODUCTO}',data)

def get_miniature(prompt, name):

    prompt_img = get_prompt_miniature(prompt, name)

    response = CLIENT.images.generate(
        model=MODELO_IMG,
        prompt=prompt_img,
        size="1792x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url

    img_save_path = os.path.join(FOLDER_PATH, "3. Miniatures", "miniatura.png")
    guardar_imagen(image_url, img_save_path)