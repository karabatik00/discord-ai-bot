import discord
from discord import app_commands

@app_commands.command(name="join", description="Botu ses kanalına katılmaya davet eder.")
async def join(interaction: discord.Interaction):
    if interaction.user.voice:
        channel = interaction.user.voice.channel
        await channel.connect()

        embed = discord.Embed(
            title="🔊 Ses Kanalına Katılındı!",
            description=f"{interaction.user.display_name} tarafından katılmam istendi!",
            color=0x00ff00
        )
        embed.set_thumbnail(url=interaction.user.avatar.url)
        embed.set_footer(text="Sesli komutları dinlemeye başladım.", icon_url=interaction.client.user.avatar.url)
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(
            title="❌ Katılma Başarısız",
            description="Bir ses kanalında değilsiniz!",
            color=0xff0000
        )
        embed.set_thumbnail(url=interaction.client.user.avatar.url)
        await interaction.response.send_message(embed=embed)
