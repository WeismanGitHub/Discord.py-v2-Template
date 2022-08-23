from discord.utils import get
import discord

blurple = 0x7289da
red = 0xe74c3c

def embed(title, message, color=blurple):
    return discord.Embed(title = title, description = message, color=color)

def error_embed(error, title="There's been an error!", color=red):
    return discord.Embed(title=title, description=error, color=color)