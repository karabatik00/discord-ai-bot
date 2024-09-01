import discord
from discord import app_commands

@app_commands.command(name="help", description="Botun komutları hakkında bilgi verir.")
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🛠️ Yardım Menüsü",
        description="Botun mevcut komutlarının listesi:",
        color=0x00ff00
    )
    embed.add_field(
        name="/join",
        value="Botu ses kanalına katılmaya davet eder.",
        inline=False
    )
    embed.add_field(
        name="/leave",
        value="Botun ses kanalından ayrılmasını sağlar.",
        inline=False
    )
    embed.add_field(
        name="/listen",
        value="Belirtilen süre boyunca (saniye) ses kaydeder ve işler.",
        inline=False
    )
    embed.add_field(
        name="/help",
        value="Bu yardım mesajını gösterir.",
        inline=False
    )
    embed.set_footer(text="Komutları slash (/) ile başlatarak kullanabilirsiniz.", icon_url=interaction.client.user.avatar.url)
    embed.set_thumbnail(url=interaction.client.user.avatar.url)
    await interaction.response.send_message(embed=embed)
