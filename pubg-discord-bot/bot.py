import discord  # Discord API wrapper
import pubg_python  # PUBG API weapper
import os

import json

os.system("ls -alt")
os.system("cd ..")
os.system("ls -alt")

# Load secrets from config/secrets.json
#secrets = json.loads(open('/usr/src/pubg-discord-bot/config', 'r').read())
#discordBotToken = secrets['discord-bot-token']
#pubgApiKey = secrets['pubg-api-key']

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ping'):
        await message.channel.send('Hello, you pinged me!')

    if message.content.startswith('!report'):
        await message.channel.send('Information about last PUBG MATCH')

    if message.content.startswith('!stats'):
        await message.channel.send('Information about my stats')

# client.run(discordBotToken)
