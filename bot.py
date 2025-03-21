import os
import discord
from discord.ext import commands

token = os.environ['TOKEN']

client = commands.Bot(command_prefix = 'e!', help_command=commands.MinimalHelpCommand())
