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
    

    @app_commands.command(name="embed", description="embed demo", guild=discord.Object(id=getenv('GUILD_ID')))
    async def majorOrder(interaction: discord.Interaction)->None:
        print("say hi")
    