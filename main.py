import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
from os import getenv
import asyncio

from functions import apidata, mo

load_dotenv(".env")

intents = discord.Intents.default()
intents.message_content = True
class Client(commands.Bot):
    def __init__(self):
        super().__init__(
            intents=intents,
            command_prefix="!"
        )
        self.data = apidata.APIData()
        self.data.callMajorOrderAPI()

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        try:
            guild = discord.Object(id=getenv('GUILD_ID'))
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print(f'Error syncing commands: {e}')
    
    
    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted')

    def getData(self):
        return self.data

client = Client()

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

@client.tree.command(name="embed", description="embed demo", guild=discord.Object(id=getenv('GUILD_ID')))
async def embed(interaction: discord.Interaction):
    embed=discord.Embed(title="MAJOR ORDER", description="Defend against the Automaton offensive, led by the newly-built Incineration Corps, or collect enough E-710 to activate the Penrose Energy Siphon and reduce Dark Energy Accumulation.", color=0xff0000)
    embed.set_thumbnail(url="https://helldivers.wiki.gg/images/thumb/8/84/Locations_Icon.svg/96px-Locations_Icon.svg.png?7f3375")
    embed.add_field(name="Defend 8 attacks from the Automatons", value="[====      ] 37.5%", inline=False)
    embed.add_field(name="Eradicate 1,250,000,000 Terminids", value="[======] 60%", inline=False)
    embed.add_field(name="Reward:", value="55 Medals", inline=False)
    embed.set_footer(text="Major order ends in 66h")
    await interaction.response.send_message(embed=embed)

async def main():
    await load()
    await client.start(getenv('TOKEN'))

if __name__ == "__main__":
    asyncio.run(main())
