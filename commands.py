import asyncio
import json
import random

import aiohttp
import discord
from discord import Game
from discord.ext.commands import Bot

BP = (".","!")

client = Bot(command_prefix=BP)

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context, message):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await message.channel.send(random.choice(possible_responses) + ", " + context.message.author.mention)
