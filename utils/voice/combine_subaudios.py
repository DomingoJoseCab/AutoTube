# ==============================================================================
# AutoTube Script
# Creado por: Domingo Caballero
# Canal de YouTube: https://www.youtube.com/@emprendedomingo?=sub_confirmation=1
# Lista de Correo: https://emprendecondomingo.substack.com/
# ==============================================================================

from pydub import AudioSegment
import os

def combine_subaudios(folder_path, output_path):
    
    archivos_audio = [archivo for archivo in os.listdir(folder_path) if archivo.endswith('.wav')]

    audio_combinado = None

    for archivo in archivos_audio:
        ruta_completa = os.path.join(folder_path, archivo)
        audio_actual = AudioSegment.from_file(ruta_completa, format="wav")

        if audio_combinado is None:
            audio_combinado = audio_actual
        else:
            audio_combinado += audio_actual

    if audio_combinado is not None:
        audio_combinado.export(output_path, format="wav")

