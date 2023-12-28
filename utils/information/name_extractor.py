# ==============================================================================
# AutoTube Script
# Creado por: Domingo Caballero
# Canal de YouTube: https://www.youtube.com/@emprendedomingo?=sub_confirmation=1
# Lista de Correo: https://emprendecondomingo.substack.com/
# ==============================================================================

import requests
from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser

def get_brand(html):
    brand = html.css_first(".a-section.a-spacing-none a#bylineInfo").text(strip=True)
    brand = brand.replace("Visita la tienda de ","")
    brand = brand.replace("Marca: ","")
    
    return brand

def get_model(html):
    rows = html.css('tr')

    for row in rows:
        header = row.css_first('th')
        value = row.css_first('td')
        if header and value and "Número de modelo" in header.text(strip=True):
            return value.text(strip=True)

    return ""