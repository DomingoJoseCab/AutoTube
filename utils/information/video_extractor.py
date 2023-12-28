# ==============================================================================
# AutoTube Script
# Creado por: Domingo Caballero
# Canal de YouTube: https://www.youtube.com/@emprendedomingo?=sub_confirmation=1
# Lista de Correo: https://emprendecondomingo.substack.com/
# ==============================================================================

import requests
from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser

def download_video(video_url, output_file):
    respuesta = requests.get(video_url, stream=True)

    if respuesta.status_code == 200:
        
        with open(output_file, 'wb') as archivo:
            for chunk in respuesta.iter_content(chunk_size=1024):
                
                archivo.write(chunk)
        print(f"Descarga completada: {output_file}")
    else:
        print(f"Error al descargar el video. Código de estado: {respuesta.status_code}")