import discord
import os
import requests
import json
import random
from replit import db
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

def update_encouragements(encouraging_message):
    if 'encouragements'  in db.key():
        encouragements = db['encouragements']
        encouragements.append(encouraging_message)
        db['encouragements'] = encouragements
    else:
        db['encouragements'] = [encouraging_message]

def delete_encouragements(index):
    encouragements = db['encouragements']
    if len(encouragements) > index:
        del encouragements[index]
        db['encouragements'] = encouragements

@client.event
async def on_ready():
    #the 0 in {0.user} is replaced by value of client variable
    print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content

    quote = get_quote()

    if msg.startswith('$hello'):
        await message.channel.send('Hello!')

    if msg.startswith('$inspire'):
        await message.channel.send(quote)

    options = starter_encouragements
    if 'encouragements' in db.keys():
        options = options = db['encouragements']
        
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

client.run(tk)
