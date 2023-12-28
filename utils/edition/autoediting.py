# ==============================================================================
# AutoTube Script
# Creado por: Domingo Caballero
# Canal de YouTube: https://www.youtube.com/@emprendedomingo?=sub_confirmation=1
# Lista de Correo: https://emprendecondomingo.substack.com/
# ==============================================================================

from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeAudioClip, AudioFileClip, CompositeVideoClip
from random import choice, randint
from math import ceil
import os

def load_videos(videos_path):
    video_list = []
    videos = os.listdir(videos_path)
    for vid in videos:
        video = VideoFileClip(os.path.join(videos_path,vid))
        video_list.append(video)

    return video_list

def load_audio(audio_path):
    audio_list = []
    audios = os.listdir(audio_path)
    for au in audios:
        audio = AudioFileClip(os.path.join(audio_path,au))
        audio_list.append(audio)

    return audio_list

def generate_intro(videos, audio):
    selected_video = choice(videos)
    audio_duration = audio.duration

    total_video_duration = audio_duration + 1 

    start_time = choice(range(int(selected_video.duration - total_video_duration)))
    video_clip = selected_video.subclip(start_time, start_time + total_video_duration)

    adjusted_audio = CompositeAudioClip([audio.set_start(0.5)])

    video_clip = video_clip.set_audio(adjusted_audio)

    return video_clip

def generate_subclip(video):
    cut_point_1 = randint(0, int(video.duration) - 10)
    cut_point_2 = randint(cut_point_1 + 3, int(video.duration) - 3)

    cut_point_1, cut_point_2 = sorted([cut_point_1, cut_point_2])

    clip1 = video.subclip(0, cut_point_1)
    clip2 = video.subclip(cut_point_1, cut_point_2)
    clip3 = video.subclip(cut_point_2, video.duration-1)

    subclips = [clip2, clip1, clip3]
    return subclips

def generate_outro(videos, audio):
    selected_video = choice(videos)
    audio_duration = audio.duration

    clips = generate_subclip(selected_video)

    total_video_duration = audio_duration + 25

    repetitions = ceil(total_video_duration / sum(clip.duration for clip in clips))

    final_clips = clips * repetitions

    final_clips = concatenate_videoclips(final_clips).subclip(0, total_video_duration)

    adjusted_audio = CompositeAudioClip([audio.set_start(0.5)])

    video_clip = final_clips.set_audio(adjusted_audio)

    return video_clip

def generate_product(video, audio):
    ordered_clips = generate_subclip(video)

    repetitions = ceil(audio.duration / sum(clip.duration for clip in ordered_clips))

    final_clips_sequence = ordered_clips * repetitions

    final_clips_sequence = concatenate_videoclips(final_clips_sequence).subclip(0, audio.duration+1)

    final_video = final_clips_sequence.set_audio(CompositeAudioClip([audio.set_start(0.5)]))

    return final_video

