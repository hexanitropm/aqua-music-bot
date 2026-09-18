import asyncio
import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # @discord.app_commands.command(name="anya")
    # async def anya(self, interaction: discord.Interaction):
    #     embed = discord.Embed(
    #         title="🎵 AquaMusic",
    #         description="Информация о треке"
    #     )

    #     embed.add_field(
    #         name="Трек",
    #         value="Лабубу",
    #         inline=True
    #     )

    #     embed.add_field(
    #         name="Громкость",
    #         value="88%",
    #         inline=True
    #     )

    #     embed.add_field(
    #         name="Длительность",
    #         value="14:48",
    #         inline=True
    #     )

    #     embed.set_footer(
    #         text="AquaMusic • Music Bot"
    #     )

    #     await interaction.response.send_message(embed=embed)

    @discord.app_commands.command(name="join")
    async def join(self, interaction: discord.Interaction):
        if interaction.user.voice is None:
            await interaction.response.send_message(
                "❌ you are not in the voice channel"
            )
            return

        if interaction.guild.voice_client is not None:
            await interaction.response.send_message(
                "❌ bot is already on the voice channel"
            )
            return

        voice_channel = interaction.user.voice.channel

        await voice_channel.connect()

        await interaction.response.send_message(
            f"🎧Aqua connected to voice channel: {voice_channel.name}"
        )

    @discord.app_commands.command(name="leave")
    async def leave(self, interaction: discord.Interaction):

        if interaction.guild.voice_client is None:
            await interaction.response.send_message(
                "❌ bot is not in the voice channel"
            )
            return

        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message(
            "👋 Aqua left the voice channel!"
        )
        
async def setup(bot):
    await bot.add_cog(General(bot))