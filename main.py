# ==============================================================================
# AutoTube Script
# Creado por: Domingo Caballero
# Canal de YouTube: https://www.youtube.com/@emprendedomingo?=sub_confirmation=1
# Lista de Correo: https://emprendecondomingo.substack.com/
# ==============================================================================

from utils.gpt.chatgpt import chatgpt
from utils.information.extractor import extractor
from utils.voice.voice import voice
from utils.edition.edit import edit
import json
import os
from datetime import datetime

def set_up_folders(video_name):
    current_date_time = datetime.now().strftime("%Y_%m_%d_%H_%M")

    main_folder_name = f"../AutoTube/data/{current_date_time}_{video_name}"

    os.makedirs(main_folder_name, exist_ok=True)

    subfolders = ["1. Scripts", "2. Videos", "3. Miniatures", "4. Audio", "5. Edition"]

    for subfolder in subfolders:
        os.makedirs(os.path.join(main_folder_name, subfolder), exist_ok=True)

    return main_folder_name


def main(folder_path, datos):
    list_asins = ['ASIN_TOP5','ASIN_TOP4','ASIN_TOP3','ASIN_TOP2','ASIN_TOP1']

    data_extracted = {}
    
    #################### EXTRACTION ####################
    print("###########################################################")
    print("Extraction start.")
    print("###########################################################")
    for i, asin in enumerate(list_asins):
        video_path = os.path.join(folder_path, "2. Videos", f"{i+1}. video.mp4")
        try:
            data_extracted[asin] = extractor(datos[asin], video_path)
        except:
            print("Retraying...")
            data_extracted[asin] = extractor(datos[asin], video_path)

    #################### CHATGPT ####################
    print("###########################################################")
    print("ChatGPT start.")
    print("###########################################################")
    chatgpt(data_extracted, folder_path)

    #################### AUDIO ####################
    print("###########################################################")
    print("Audio start.")
    print("###########################################################")
    voice(folder_path)

    #################### EDITION ####################
    print("###########################################################")
    print("Edition start.")
    print("###########################################################")
    edit(folder_path)

if __name__ == "__main__":
    with open('../AutoTube/argss.json', 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)

    folder_path = set_up_folders(datos['video_name'])
    main(folder_path, datos)