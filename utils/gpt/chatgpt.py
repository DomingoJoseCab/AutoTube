# ==============================================================================
# AutoTube Script
# Creado por: Domingo Caballero
# Canal de YouTube: https://www.youtube.com/@emprendedomingo?=sub_confirmation=1
# Lista de Correo: https://emprendecondomingo.substack.com/
# ==============================================================================

from openai import OpenAI
import os
import json
from utils.gpt.generate_script import get_product_script, get_better_intro, get_better_outro, set_up_generate_script
from utils.gpt.generate_description import get_description, set_up_generate_description
from utils.gpt.generate_miniature import get_miniature, set_up_generate_miniature

with open('../AutoTube/argss.json', 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)

OPENAI_API_KEY = datos['OPENAI_API_KEY']
CLIENT = OpenAI(api_key=OPENAI_API_KEY)
MODELO_GPT4 = "gpt-4"
MODELO_IMG = "dall-e-3"

def set_up(folder_path):
    set_up_generate_script(CLIENT, MODELO_GPT4, folder_path)
    set_up_generate_description(CLIENT, MODELO_GPT4, folder_path)
    set_up_generate_miniature(CLIENT, MODELO_IMG, folder_path)

def chatgpt(data, folder_path):
    set_up(folder_path)
    list_asins = ['ASIN_TOP5','ASIN_TOP4','ASIN_TOP3','ASIN_TOP2','ASIN_TOP1']
    
    #################### GENERATING INTRO ####################
    print("Generating intro...")
    intro_path = os.path.join(datos['scripts_path'],'intro.txt')
    get_better_intro(intro_path, datos['video_name'])
    print("Intro generated.")
    print("-----------------------------")

    #################### GENERATING PRODUCTS ####################
    for i, product in enumerate(list_asins):
        print(f"Generating product {5-i}...")
        get_product_script(data[product],datos['video_name'],5-i)
    print("Products generated.")
    print("-----------------------------")
    
    #################### GENERATING OUTRO ####################
    print("Generating outro...")
    outro_path = os.path.join(datos['scripts_path'],'outro.txt')
    get_better_outro(outro_path, datos['video_name'])
    print("Outro generated.")
    print("-----------------------------")

    #################### GENERATING DESCRIPTION ####################
    print("Generating description...")
    

    description_data = {
        'video_name': datos['video_name'],
        'top5': data['ASIN_TOP5'][0],
        'top4': data['ASIN_TOP4'][0],
        'top3': data['ASIN_TOP3'][0],
        'top2': data['ASIN_TOP2'][0],
        'top1': data['ASIN_TOP1'][0],
        
    }

    with open(os.path.join(folder_path,'datos.json'), 'w', encoding='utf-8') as products:
        json.dump(description_data, products, indent=4)

    description_path = os.path.join(datos['scripts_path'],'description.txt')
    get_description(description_path, description_data)
    print("Description generated.")
    print("-----------------------------")

    #################### GENERATING MINIATURE ####################
    print("Generating miniature...")
    with open("../AutoTube/utils/scripts/miniature.txt", 'r', encoding='utf-8') as mini:
        prompt_miniature = mini.read()
    get_miniature(prompt_miniature, description_data['video_name'])
    print("Miniature generated.")
    print("-----------------------------")
    
