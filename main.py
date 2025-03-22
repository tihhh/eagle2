import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from os import getenv

from functions import apidata, mo

load_dotenv(".env")

class Client(commands.Bot):
    def __init__(self):
        self.data = apidata.APIData()

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
            guild = discord.Object(id=getenv('GUILD_ID'))
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print(f'Error syncing commands: {e}')
    async def on_message(self, message):
        if (message.author == self.user):
            return
        
        if (message.content.startswith('hello')):
            await message.channel.send(f'Hi there {message.author}')
    
    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted')


intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!!", intents=intents)

@client.tree.command(name="hello", description="Say hello!", guild=discord.Object(id=getenv('GUILD_ID')))
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there!")

@client.tree.command(name="printer", description="print whatever", guild=discord.Object(id=getenv('GUILD_ID')))
async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

@client.tree.command(name="embed", description="embed demo", guild=discord.Object(id=getenv('GUILD_ID')))
async def embed(interaction: discord.Interaction):
    embed=discord.Embed(title="MAJOR ORDER", description="Defend against the Automaton offensive, led by the newly-built Incineration Corps, or collect enough E-710 to activate the Penrose Energy Siphon and reduce Dark Energy Accumulation.", color=0xff0000)
    embed.set_thumbnail(url="https://helldivers.wiki.gg/images/thumb/8/84/Locations_Icon.svg/96px-Locations_Icon.svg.png?7f3375")
    embed.add_field(name="Defend 8 attacks from the Automatons", value="[====      ] 37.5%", inline=False)
    embed.add_field(name="Eradicate 1,250,000,000 Terminids", value="[======] 60%", inline=False)
    embed.add_field(name="Reward:", value="55 Medals", inline=False)
    embed.set_footer(text="Major order ends in 66h")
    await interaction.response.send_message(embed=embed)

client.run(getenv('TOKEN'))