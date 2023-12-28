# ==============================================================================
# AutoTube Script
# Creado por: Domingo Caballero
# Canal de YouTube: https://www.youtube.com/@emprendedomingo?=sub_confirmation=1
# Lista de Correo: https://emprendecondomingo.substack.com/
# ==============================================================================

import os
import json
from moviepy.editor import CompositeVideoClip
from utils.edition.autoediting import load_videos, load_audio, generate_product, generate_intro, generate_outro
from utils.edition.autotext import title_intro


def main(videos_path, audios_path, output_path, names, base_path):
    videos = load_videos(videos_path)
    audios = load_audio(audios_path)

    audio_intro = audios.pop(0)
    audio_outro = audios.pop(-1)
    
    intro = generate_intro(videos, audio_intro)
    intro = title_intro(str.upper(names['titulo']),intro)
    outro = generate_outro(videos, audio_outro)

    top_clips = {}
    top_names = ['top5','top4','top3','top2','top1']

    for vid, aud, top in zip(videos, audios, top_names):
        top_clips[top] = generate_product(vid, aud)
        top_clips[top] = title_intro(str.upper(names[top]),top_clips[top])

    final_video = CompositeVideoClip([intro, 
                                      top_clips['top5'].set_start(intro.duration), 
                                      top_clips['top4'].set_start(intro.duration+top_clips['top5'].duration), 
                                      top_clips['top3'].set_start(intro.duration+top_clips['top5'].duration+top_clips['top4'].duration), 
                                      top_clips['top2'].set_start(intro.duration+top_clips['top5'].duration+top_clips['top4'].duration+top_clips['top3'].duration), 
                                      top_clips['top1'].set_start(intro.duration+top_clips['top5'].duration+top_clips['top4'].duration+top_clips['top3'].duration+top_clips['top2'].duration), 
                                      outro.set_start(intro.duration+top_clips['top5'].duration+top_clips['top4'].duration+top_clips['top3'].duration+top_clips['top2'].duration+top_clips['top1'].duration)])

    final_video.resize(newsize=(1920,1080))

    final_video.write_videofile(os.path.join(output_path,"video.mp4"))
    
def edit(base_path):
    videos_path = os.path.join(base_path,"2. Videos")
    audios_path = os.path.join(base_path,"4. Audio")
    output_path = os.path.join(base_path,"5. Edition")

    with open(os.path.join(base_path,'datos.json'), 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)

    names = {}
    names['titulo'] = datos['video_name']
    for top in ['top5','top4','top3','top2','top1']:
        names[top] = datos[top] 
    
    from moviepy.config import change_settings
    change_settings({"IMAGEMAGICK_BINARY": "C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

    main(videos_path, audios_path, output_path, names, base_path)