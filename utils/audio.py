import os
import discord
from gtts import gTTS
import speech_recognition as sr

def process_audio_file(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language="tr-TR")
    return text

def play_text_as_audio(vc, text):
    tts = gTTS(text, lang="tr")
    tts.save("response.mp3")
    if vc:
        vc.play(discord.FFmpegPCMAudio(executable="ffmpeg", source="response.mp3"))
    if os.path.exists("response.mp3"):
        os.remove("response.mp3")
