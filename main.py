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

async def on_ready(self):
        print('Logged on as', self.user)

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
async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))
            await channel.send.file('welc.jpg')

client.run(token)



