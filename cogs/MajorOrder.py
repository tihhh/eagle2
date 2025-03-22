import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from main import Client
from os import getenv

load_dotenv(".env")

class MajorOrder(commands.Cog):
    def __init__(self, bot : Client):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online")
    

    @discord.app_commands.command(name="majororder", description="Returns the current major order")
    @discord.app_commands.guilds(discord.Object(id=getenv('GUILD_ID')))
    async def majorOrder(self, interaction: discord.Interaction):
        await interaction.response.send_message("PUT MO HERE PLEASE")
    

async def setup(bot):
    await bot.add_cog(MajorOrder(bot))