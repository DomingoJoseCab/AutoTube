# ==============================================================================
# AutoTube Script
# Creado por: Domingo Caballero
# Canal de YouTube: https://www.youtube.com/@emprendedomingo?=sub_confirmation=1
# Lista de Correo: https://emprendecondomingo.substack.com/
# ==============================================================================

import json
import os
import requests
from utils.voice.combine_subaudios import combine_subaudios

def get_api_key():
    with open('../AutoTube/argss.json', 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    return datos['LOVOAI_API_KEY']

def download_audio(url, output_path):
    respuesta = requests.get(url, stream=True)

    if respuesta.status_code == 200:
        
        with open(output_path, 'wb') as archivo:
            for chunk in respuesta.iter_content(chunk_size=1024):
                
                archivo.write(chunk)
        print(f"Descarga completada: {output_path}")
    else:
        print(f"Error al descargar el audio. Código de estado: {respuesta.status_code}")

def get_audio(text, output_path):
    url = "https://api.genny.lovo.ai/api/v1/tts/sync"

    payload = {
        "speed": 1.05,
        "text": text,
        "speaker": "64e2f76036fe21ca612f166f"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": get_api_key()
    }

    response = requests.post(url, json=payload, headers=headers)
    res = json.loads(response.content)
    dict_response = dict(res)
    try:
        download_audio(dict_response['data'][0]['urls'][0],output_path)
    except:
        print("Error downloading audio...")
        print(dict_response)

def check_line(linea):
    
    if linea[-1]=='.' or linea[-1]=='!' or linea[-1]=='?':
        return linea
    else:
        ultimo_punto = linea.rfind('.')
        ultima_exclamacion = linea.rfind('!')
        ultima_interrogacion = linea.rfind('?')

        ultimo = max([ultimo_punto, ultima_exclamacion, ultima_interrogacion])

        return linea[:ultimo + 1]

def dividir_linea(line):
    linea = check_line(line)
    if len(linea) > 500:
        ultimo_punto = linea.rfind('.', 0, 500)
        if ultimo_punto != -1:
            return [linea[:ultimo_punto + 1], linea[ultimo_punto + 1:]]
        else:
            return [linea[:500], linea[500:]] 
    else:
        return [linea]

def get_intro_voice(intro_path, folder_path):
    with open(intro_path, 'r', encoding='utf-8') as intro:
        text = intro.read()

    intro_output_path = os.path.join(folder_path, "4. Audio", "0.wav")
    get_audio(text, intro_output_path)

def get_product_voice(product_path, folder_path, i):
    os.makedirs(os.path.join(folder_path,"4.1. Subaudio", f"{i}"), exist_ok=True)
    subaudio_path = os.path.join(folder_path, "4.1. Subaudio",f"{i}")
    with open(product_path, 'r', encoding='utf-8') as product:
        for j, line in enumerate(product):
            if line.strip():
                lineas_divididas = dividir_linea(line.strip())
                for k, sublinea in enumerate(lineas_divididas):
                    subaudio_output_path = os.path.join(subaudio_path, f"{j}.{k}.wav")
                    get_audio(sublinea, subaudio_output_path)
    audio_output_path = os.path.join(folder_path, "4. Audio", f"{i}.wav")
    combine_subaudios(subaudio_path,audio_output_path)

def get_outro_voice(outro_path, folder_path):
    with open(outro_path, 'r', encoding='utf-8') as outro:
        text = outro.read()

    outro_output_path = os.path.join(folder_path, "4. Audio", "7.wav")
    get_audio(text, outro_output_path)