import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from main import Client
from os import getenv

from functions.apidata import *
from functions.planet import *
from functions.func import progressBar, timeConvert

load_dotenv(".env")

class PlanetsCog(commands.Cog):
    def __init__(self, bot : Client):
        self.bot = bot
        self.handler = PlanetHandler()
        self.data = bot.getData().getPlanets()
        self.status = bot.getData().planetStatus

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online")
    
    @discord.app_commands.command(name="planet", description="Returns info on an active planet.")
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
            await interaction.response.send_message("Planet name is incorrect or is not active (use /planetinfo to grab info on inactive planets)")
    
    @discord.app_commands.command(name="planetinfo", description="Returns info on a certain planet.")
    @discord.app_commands.guilds(discord.Object(id=getenv('GUILD_ID')))
    async def detailedPlanetInfo(self, interaction: discord.Interaction, planet : str):
        try:
            currentPlanetId = self.handler.returnId(planet)
            planetDetailedInformation = self.handler.returnPlanetDetailed(currentPlanetId)
            currentPlanetStatus = self.handler.getPlanetStatus(self.status, planet_id=currentPlanetId)
            if currentPlanetId != None:
                embed=discord.Embed(title=f"**[{currentPlanetId}] {planetDetailedInformation[1]}**", description=self.handler.returnBiomeInfoFromBiome(planetDetailedInformation[3])[0], color=0x7c2727)
                embed.set_image(url=self.handler.returnBiomeInfoFromBiome(planetDetailedInformation[3])[1])
                embed.set_thumbnail(url=self.handler.returnOwnerLogoByID(currentPlanetStatus['owner']))
                embed.add_field(name="Sector", value=planetDetailedInformation[2], inline=False)
                embed.add_field(name="Players", value=currentPlanetStatus['players'], inline=False)
                for key, value in self.handler.returnGalacticEffects(self.status, currentPlanetId).items():
                    if key != 'UNKNOWN':
                        embed.add_field(name=key, value=value, inline=False)
                embed.set_footer(text=f"PLANET CONDITIONS: {planetDetailedInformation[4]}")
                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message("Planet not found!")
        except Exception as e:
            await interaction.response.send_message(f"{e}")


    @discord.app_commands.command(name="debugcodeplanet", description="Returns debug info for planet")
    @discord.app_commands.guilds(discord.Object(id=getenv('GUILD_ID')))
    async def planetDebugCode(self, interaction: discord.Interaction, planet : str):
        try:
            currentPlanetId = self.handler.returnId(planet)
            planetDetailedInformation = self.handler.returnPlanetDetailed(currentPlanetId)
            currentPlanetStatus = self.handler.getPlanetStatus(self.status, planet_id=currentPlanetId)
            await interaction.response.send_message(f"{currentPlanetId} \\ {planetDetailedInformation} \\ {currentPlanetStatus} \\{self.handler.returnGalacticEffects(self.status, currentPlanetId)}")
        except Exception as e:
            await interaction.response.send_message(f"{e}")
async def setup(bot):
    await bot.add_cog(PlanetsCog(bot))
