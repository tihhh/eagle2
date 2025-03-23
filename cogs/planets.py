import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

from functions.apidata import *
from functions.planet import *
from functions.func import progressBar, timeConvert

load_dotenv(".env")

class PlanetsCog(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        self.handler = PlanetHandler()
        self.data = bot.getData().getPlanets()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online")
    
    @discord.app_commands.command(name="planet", description="Returns info on a certain planet.")
    @discord.app_commands.guilds(discord.Object(id=getenv('GUILD_ID')))
    async def planetInfo(self, interaction: discord.Interaction, planet : str):
        currentPlanet = self.handler.getPlanet(self.data, planet)
        if currentPlanet != None:
            embed=discord.Embed(title=currentPlanet['name'], description=self.handler.returnBiome(currentPlanet)[1])
            embed.set_thumbnail(url=self.handler.returnOwnerLogo(currentPlanet))
            embed.set_image(url="https://static.wikia.nocookie.net/helldivers_gamepedia/images/9/9d/Arctic_Landscape.png")
            embed.add_field(name="Players", value=currentPlanet['players'], inline=True)
            embed.add_field(name="Progress", value=progressBar(currentPlanet['percentage']), inline=False)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Planet not found")


async def setup(bot):
    await bot.add_cog(PlanetsCog(bot))
