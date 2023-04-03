import discord
import os
import requests
import json
#from Conf.config import Token


tk = os.environ['BOT_TOKEN']
client = discord.Client(intents=discord.Intents.default())


# This function accesses a rest api 
# retrieves a record in json format 
# parses the content in this case 
# there is quote data and author data
# concatinates them as a single string 
# and returns the string thusly:
# "Quote text -Authors name"
def get_quote():
    response = requests.get
    ('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
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

client.run(tk)
