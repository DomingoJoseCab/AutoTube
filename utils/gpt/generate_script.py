# ==============================================================================
# AutoTube Script
# Creado por: Domingo Caballero
# Canal de YouTube: https://www.youtube.com/@emprendedomingo?=sub_confirmation=1
# Lista de Correo: https://emprendecondomingo.substack.com/
# ==============================================================================

from openai import OpenAI
import os

CLIENT = None
MODELO_GPT4 = None
FOLDER_PATH = None

def set_up_generate_script(client, modelo, folder_path):
    global CLIENT, MODELO_GPT4, FOLDER_PATH
    CLIENT = client
    MODELO_GPT4 = modelo
    FOLDER_PATH = folder_path

def guardar_respuesta(respuesta, output_guion):
    texto_respuesta = respuesta.choices[0].message.content
    
    with open(output_guion, 'w', encoding='utf-8') as file:
        file.write(texto_respuesta)

def get_product_replace(data, video_name, i):
    
    with open(f'../AutoTube/utils/scripts/products.txt', 'r', encoding='utf-8') as file:
        plantilla = file.read()

    texto_final = plantilla.replace('{INFO PRODUCTO}', f'{data}')

    if i==1:
        texto_final = texto_final.replace('{INICIO}',"Terminando")
    elif i==5:
        texto_final = texto_final.replace('{INICIO}',"Empezando")
    else:
        texto_final = texto_final.replace('{INICIO}',"Continuando")

    texto_final = texto_final.replace('{i}',f'{i}')

    texto_final = texto_final.replace('{PRODUCTO}',video_name)
    
    return texto_final

def get_product_script(data_extracted, video_name, i):

    prompt = get_product_replace(data_extracted, video_name, i)
    
    messages = [
        {"role": "system", "content": "Genera un guion en ESPAÑOL para un narrador de voz en off para un video de YouTube, el video habla de varios productos de Amazon, PERO en este caso deberas generar el guion para un ÚNICO PRODUCTO. El guion del ÚNICO producto debe contener exclusivamente el texto del narrador, solo el texto del narrador sin comillas. Concéntrate en las características únicas, el precio y los beneficios del producto. El guion debe adherirse al sistema de medidas habitual utilizado en España. La narración debe ser coherente y continua para un único capítulo del video, estrictamente limitada a lo que dirá el narrador. Excluye cualquier descripción visual, notas de transición o interacciones con la audiencia. El objetivo es crear una narración informativa y atractiva, adecuada para un video profesional de YouTube."},
        {"role": "user", "content": prompt}
    ]

    respuesta = CLIENT.chat.completions.create(
        model=MODELO_GPT4,
        messages=messages,
        max_tokens=500
    )
    n = 6-i
    product_save_path = os.path.join(FOLDER_PATH, "1. Scripts", f"{n}. product_{n}.txt")
    return guardar_respuesta(respuesta, product_save_path)

def get_intro_replace(path_intro,name):
    with open(path_intro, 'r', encoding='utf-8') as intro:
        prompt = intro.read()
    
    return prompt.replace('{PRODUCTO}',name)

def get_better_intro(path_intro,name):
    prompt = get_intro_replace(path_intro,name)
    
    messages = [
        {"role": "system", "content": "Dada una introducción base únicamente quiero que adecues correctamente el genero de los artículos. Únicamente devuelve la introducción en CASTELLANO, nada más. Solo la introducción."},
        {"role": "user", "content": prompt}
    ]
    

    respuesta = CLIENT.chat.completions.create(
        model=MODELO_GPT4,
        messages=messages,
        max_tokens=150
    )
    intro_save_path = os.path.join(FOLDER_PATH, "1. Scripts", "0. intro.txt")
    return guardar_respuesta(respuesta,intro_save_path)

def get_better_outro(path_outro, name):
    prompt = get_intro_replace(path_outro,name)

    messages = [
        {"role": "system", "content": "Dada una despedida base únicamente quiero que adecues correctamente el genero de los artículos. Únicamente devuelve la despedida en CASTELLANO, nada más. Solo la despedida."},
        {"role": "user", "content": prompt}
    ]
    

    respuesta = CLIENT.chat.completions.create(
        model=MODELO_GPT4,
        messages=messages,
        max_tokens=150
    )

    outro_save_path = os.path.join(FOLDER_PATH, "1. Scripts", "7. outro.txt")
    return guardar_respuesta(respuesta,outro_save_path)