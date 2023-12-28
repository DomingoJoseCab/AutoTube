# ==============================================================================
# AutoTube Script
# Creado por: Domingo Caballero
# Canal de YouTube: https://www.youtube.com/@emprendedomingo?=sub_confirmation=1
# Lista de Correo: https://emprendecondomingo.substack.com/
# ==============================================================================

import json
import os
import requests
from utils.voice.generate_audio import get_intro_voice, get_outro_voice, get_product_voice

def voice(folder_path):
    print("Generating audio intro...")
    intro_path = os.path.join(folder_path,'1. Scripts','0. intro.txt')
    get_intro_voice(intro_path, folder_path)

    for i in range(1,6):
        print(f"Generating audio product {i}...")
        product_path = os.path.join(folder_path,'1. Scripts',f'{i}. product_{i}.txt')
        get_product_voice(product_path, folder_path, i)
    
    print("Generating audio outro...")
    outro_path = os.path.join(folder_path,'1. Scripts','7. outro.txt')
    get_outro_voice(outro_path, folder_path)

