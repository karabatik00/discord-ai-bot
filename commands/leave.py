import discord
from discord import app_commands

@app_commands.command(name="leave", description="Botun ses kanalından ayrılmasını sağlar.")
async def leave(interaction: discord.Interaction):
    if interaction.guild.voice_client:
        await interaction.guild.voice_client.disconnect()
        embed = discord.Embed(
            title="🔇 Ses Kanalından Ayrıldım",
            description=f"{interaction.user.display_name}, istek üzerine ses kanalından ayrıldım.",
            color=0x00ff00
        )
        embed.set_thumbnail(url=interaction.user.avatar.url)
        embed.set_footer(text="Her zaman hizmetinizdeyim!", icon_url=interaction.client.user.avatar.url)
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(
            title="❌ Hata",
            description="Bir ses kanalında değilim!",
            color=0xff0000
        )
        embed.set_thumbnail(url=interaction.client.user.avatar.url)
        await interaction.response.send_message(embed=embed)
