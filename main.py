import discord
from Conf.config import Token

client = discord.Client()

@client.event
async def on_ready():
    #the 0 in {0.user} is replaced by value of client variable
    print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


