# ==============================================================================
# AutoTube Script
# Creado por: Domingo Caballero
# Canal de YouTube: https://www.youtube.com/@emprendedomingo?=sub_confirmation=1
# Lista de Correo: https://emprendecondomingo.substack.com/
# ==============================================================================

from openai import OpenAI
import json
import os

CLIENT = None
MODELO_GPT4 = None
FOLDER_PATH = None

def set_up_generate_description(client, modelo, folder_path):
    global CLIENT, MODELO_GPT4, FOLDER_PATH
    CLIENT = client
    MODELO_GPT4 = modelo
    FOLDER_PATH = folder_path

def guardar_respuesta(respuesta, output_guion):
    texto_respuesta = respuesta.choices[0].message.content
    
    with open(output_guion, 'w', encoding='utf-8') as file:
        file.write(texto_respuesta)

def get_prompt_replaced(description_path, data):
    with open('../AutoTube/argss.json', 'r', encoding='utf-8') as d:
        datos = json.load(d)

    with open(description_path, 'r', encoding='utf-8') as desc:
        prompt = desc.read()

    prompt_replace = prompt.replace('{PRODUCTO}',data['video_name'])
    for i in range(1,6):
        name = data[f'top{i}']
        name_replace = '{'+f'PRODUCTO TOP {i}'+'}'
        asin_replace = f'ASIN_TOP{i}'
        asin = datos[asin_replace]
        asin_replace = '{'+asin_replace+'}'
        prompt_replace = prompt_replace.replace(name_replace,name)
        prompt_replace = prompt_replace.replace(asin_replace,asin)

    return prompt_replace

def get_description(description_path, data):
    prompt_replace = get_prompt_replaced(description_path, data)
    
    messages = [
        {"role": "system", "content": "Dada una descripcción quiero que dejes bien escrito todo, asegúrate de que del genero y la coherencia gramátical. Únicamente quiero que me devuelvas la descripción, nada más. Es decir, yo te paso la descripción, la revisas y me la devuelves sin añadir ningún mensaje más, SOLO LA DESCRIPCIÓN."},
        {"role": "user", "content": prompt_replace}
    ]
    

    respuesta = CLIENT.chat.completions.create(
        model=MODELO_GPT4,
        messages=messages,
        max_tokens=300
    )
    
    description_save_path = os.path.join(FOLDER_PATH, "1. Scripts", "description.txt")
    return guardar_respuesta(respuesta, description_save_path)