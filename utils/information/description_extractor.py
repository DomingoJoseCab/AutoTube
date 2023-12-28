# ==============================================================================
# AutoTube Script
# Creado por: Domingo Caballero
# Canal de YouTube: https://www.youtube.com/@emprendedomingo?=sub_confirmation=1
# Lista de Correo: https://emprendecondomingo.substack.com/
# ==============================================================================

import requests
from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser

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

def get_stars(html):
    return html.css_first("span#acrPopover").attributes.get('title')

def get_price(html):
    return html.css_first("span.a-offscreen").text(strip=True)

def get_about(html):
    return html.css_first("div#feature-bullets").text(strip=True)

def get_show_more(html):
    return html.css_first("ul.a-unordered-list").text(strip=True)

def get_video_url(html, asin, language):
    try:
        url = html.css_first("video.vjs-tech").attributes.get('src')
        return url
    except:
        return get_video_url(get_html(asin), asin)

def get_description(html, asin):
    data = {
        'stars': get_stars(html),
        'price': get_price(html),
        'about': get_about(html),
        'show_more': get_show_more(html),
        'video_url': get_video_url(html, asin)
    }

    return data, f'{get_stars(html)},{get_price(html)},{get_about(html)},{get_show_more(html)}'