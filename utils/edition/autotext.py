# ==============================================================================
# AutoTube Script
# Creado por: Domingo Caballero
# Canal de YouTube: https://www.youtube.com/@emprendedomingo?=sub_confirmation=1
# Lista de Correo: https://emprendecondomingo.substack.com/
# ==============================================================================

from moviepy.editor import TextClip, ColorClip, CompositeVideoClip
from random import choice, randint
import os
import textwrap


def title_intro(title:str, video):
    
    texto = TextClip(title, fontsize=40, color='white', font='Bebas Neue Bold')
    texto = texto.set_position('center').set_duration(6)

    color_clip = ColorClip(video.size, color=(0, 0, 0), duration=texto.duration)
    color_clip = color_clip.set_opacity(0.9)  # Ajusta la opacidad

    color_clip = color_clip.set_start(4)

    texto = texto.set_start(4).crossfadein(1)

    video_opaco = CompositeVideoClip([video, color_clip])

    video_final = CompositeVideoClip([video_opaco, texto])

    return video_final

def generate_line_effect(vid):
    raya = ColorClip(size=(350, 3), color=(255, 255, 255), duration=6)

    raya = raya.set_position(('center', ((vid.size[1]/2)+25))).set_start(4).crossfadein(1)

    return raya
