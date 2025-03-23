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

async def main():
    await load()
    await client.start(getenv('TOKEN'))

if __name__ == "__main__":
    asyncio.run(main())
