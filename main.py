import asyncio
import json
import random
import logging


import aiohttp
import discord
from discord import Game
from discord.ext import commands
logging.basicConfig(level=logging.INFO)

f = open('Token.txt')

token = f.read()

client = commands.Bot(command_prefix = '!')




async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
@client.event
async def on_ready():
        
        print('Logged on as', client.user.name)
        print(client.user.id)
        game = discord.Game('With broken code')
        await client.change_presence(status=discord.Status.idle,activity=game)

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))
@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))
    await message.channel.send('{}: {}'.format(author, content))


@client.event
async def on_member_join(member):
    server = member.guild
    channel = client.get_channel(562124177671192600)
    await channel.send('Welcome {} to {}'.format(member, server))
    await channel.send(file=discord.File('welc.jpg'))
    
    

client.run(token)

#commands

