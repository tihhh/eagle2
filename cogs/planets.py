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
            embed.set_image(url=self.handler.returnBiome(currentPlanet)[2])
            embed.add_field(name="Players", value=currentPlanet['players'], inline=True)
            embed.add_field(name="Progress", value=progressBar(currentPlanet['percentage']), inline=False)
            if currentPlanet['expireDateTime'] != None:
                embed.set_footer(text="Time until planet falls: "+ timeConvert(int(self.handler.getDefense(currentPlanet))))
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Planet name is incorrect or is not active (no war is happening)")


async def setup(bot):
    await bot.add_cog(PlanetsCog(bot))
