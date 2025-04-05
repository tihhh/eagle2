import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from main import Client
from os import getenv

from functions.apidata import *
from functions.news import NewsHandler
from functions.func import progressBar, timeConvert
from functions.pagination import Pagination

load_dotenv(".env")

class NewsCog(commands.Cog):
    def __init__(self, bot : Client):
        self.bot = bot
        self.data = bot.getData().news
        self.handler = NewsHandler()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online")

    @discord.app_commands.command(name="news", description="Returns galactic news broadcasts.")
    @discord.app_commands.guilds(discord.Object(id=getenv('GUILD_ID')))
    async def news(self, interaction: discord.Interaction):
        try:
            async def get_page(page: int):
                L = 1 #Amount of news per page
                embed=discord.Embed(title="GALACTIC BROADCAST", color=0xff0000)
                offset = (page-1)*L
                for i in self.handler.getNews(self.data)[offset:offset+L]:
                    embed.add_field(name="", value=i, inline=False) 
                n = Pagination.compute_total_pages(len(self.handler.getNews(self.data)), L)
                embed.set_footer(text=f"Page {page} from {n}")
                embed.set_thumbnail(url="https://static.wikia.nocookie.net/helldivers_gamepedia/images/2/22/Ministry_of_Truth_Insignia.png")
                return embed, n
                   
            await Pagination(interaction, get_page).navegate()
        except Exception as e:
            await interaction.response.send_message(e)
    


async def setup(bot):
    await bot.add_cog(NewsCog(bot))