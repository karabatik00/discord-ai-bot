import discord
from discord import app_commands
from utils.microphone import get_microphone_device
from utils.audio import process_audio_file, play_text_as_audio
from utils.api import get_api_response
import subprocess
import os

@app_commands.command(name="listen", description="Belirtilen süre boyunca ses kaydeder.")
@app_commands.describe(duration="Dinleme süresini saniye cinsinden belirtin.")
async def listen(interaction: discord.Interaction, duration: int):
    await interaction.response.defer()
    if not interaction.guild.voice_client:
        embed = discord.Embed(
            title="❌ Bir Ses Kanalında Değilim!",
            description="Lütfen beni bir ses kanalına katılmam için davet edin.",
            color=0xff0000
        )
        embed.set_thumbnail(url=interaction.client.user.avatar.url)
        await interaction.followup.send(embed=embed)
        return

    vc = interaction.guild.voice_client

    device_name = get_microphone_device()
    if not device_name:
        embed = discord.Embed(
            title="🎙️ Mikrofon Bulunamadı",
            description="Bağlı bir mikrofon cihazı bulunamadı.",
            color=0xff0000
        )
        embed.set_thumbnail(url=interaction.client.user.avatar.url)
        await interaction.followup.send(embed=embed)
        return

    embed = discord.Embed(
        title="🎙️ Dinleme Başladı",
        description=f"{interaction.user.display_name} için {duration} saniye dinleniyor...",
        color=0x00ff00
    )
    embed.set_thumbnail(url=interaction.user.avatar.url)
    await interaction.followup.send(embed=embed)

    audio_file = "microphone_recording.wav"
    subprocess.run(["ffmpeg", "-y", "-f", "dshow", "-i", f"audio={device_name}", "-t", str(duration), audio_file])

    embed = discord.Embed(
        title="🎙️ Mikrofon Kaydedildi",
        description="Ses kaydedildi ve işleniyor...",
        color=0x00ff00
    )
    embed.set_thumbnail(url=interaction.user.avatar.url)
    await interaction.followup.send(embed=embed)

    try:
        text = process_audio_file(audio_file)
        embed = discord.Embed(
            title="📜 Anladım",
            description=f"Metin: **{text}**",
            color=0x00ff00
        )
        embed.set_thumbnail(url=interaction.client.user.avatar.url)
        await interaction.followup.send(embed=embed)

        answer = get_api_response(text)
        embed = discord.Embed(
            title="🗨️ Yanıt",
            description=f"{answer}",
            color=0x00ff00
        )
        embed.set_thumbnail(url=interaction.client.user.avatar.url)
        await interaction.followup.send(embed=embed)

        play_text_as_audio(vc, answer)

    except Exception as e:
        embed = discord.Embed(
            title="❌ Hata",
            description=f"Hata oluştu: {e}",
            color=0xff0000
        )
        embed.set_thumbnail(url=interaction.client.user.avatar.url)
        await interaction.followup.send(embed=embed)
    finally:
        if os.path.exists(audio_file):
            os.remove(audio_file)
