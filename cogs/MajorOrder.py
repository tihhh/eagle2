import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from main import Client
from os import getenv

from functions.apidata import *
from functions.mo import *
from functions.func import progressBar, timeConvert

load_dotenv(".env")

class MajorOrder(commands.Cog):
    def __init__(self, bot : Client):
        self.bot = bot
        self.MOHandler = MajorOrderHandler()
        self.data = bot.getData().mo
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online")
    

    @discord.app_commands.command(name="majororder", description="Returns the current major order")
    @discord.app_commands.guilds(discord.Object(id=getenv('GUILD_ID')))
    async def majorOrder(self, interaction: discord.Interaction):
        embed=discord.Embed(title="MAJOR ORDER", description=str(self.MOHandler.returnBrief(self.data)), color=0xff0000)
        embed.set_thumbnail(url="https://helldivers.wiki.gg/images/thumb/8/84/Locations_Icon.svg/96px-Locations_Icon.svg.png?7f3375")
        for task in self.MOHandler.returnTasks(self.data):
            embed.add_field(name=task[0], value=progressBar(task[2]/task[1]*100), inline=False)
        embed.set_footer(text="Major order ends in "+timeConvert(self.MOHandler.returnSeconds(self.data)))
            #embed.add_field(name="No Major Order currently", value="Wait for High Command", inline=False)
        await interaction.response.send_message(embed=embed)
    

async def setup(bot):
    await bot.add_cog(MajorOrder(bot))