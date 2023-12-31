# ==============================================================================
# AutoTube Script
# Creado por: Domingo Caballero
# Canal de YouTube: https://www.youtube.com/@emprendedomingo?=sub_confirmation=1
# Lista de Correo: https://emprendecondomingo.substack.com/
# ==============================================================================

import json
from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser

from utils.information.name_extractor import get_brand, get_model
from utils.information.description_extractor import get_description, get_video_url
from utils.information.video_extractor import download_video

def get_html(asin):
    pw = sync_playwright().start()
    browser = pw.chromium.launch()
    page = browser.new_page()
    
    url = f"https://www.amazon.es/dp/{asin}"
    
    page.goto(url)
    html = HTMLParser(page.content())

    browser.close()
    pw.stop()

    return html

def extractor(asin, video_path):
    with open('../AutoTube/args.json', 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)

    print("Getting html...")
    html = get_html(asin)
    print("Getting brand and model...")
    product = get_brand(html) + get_model(html)
    print("Getting description...")
    data, description = get_description(html, asin)

    full_description = product + ', ' + description

    print("Downloading video...")
    try:
        download_video(data['video_url'], video_path)
    except:
        print("Retrying to download video...")
        url = get_video_url(html, asin)
        download_video(url, video_path)

    return (product,full_description)
    