import discord
import os
import requests
import json
import random
#from Conf.config import Token


tk = os.environ['BOT_TOKEN']
client = discord.Client(intents=discord.Intents.default())

sad_words = ['sad', 'depressed', 'unhappy', 'angry',
             'miserable', 'depressing']


starter_encouragements = [
    'You are valid.',
    'Thing will get better.',
    'You are a good person/Bot.'
    ]

def get_quote():
    # This function accesses a rest api 
    response = requests.get('https://zenquotes.io/api/random')
    # retrieves a record in json format 
    json_data = json.loads(response.text)
     # parses the content, in this case 
    # there is quote data and author data
    # concatinates them as a single string 
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    # and returns the string thusly:
    # "Quote text -Authors name"
    return(quote)

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
    if message.content.startswith('$inspire'):
        await message.channel.send(get_quote())

client.run(tk)
