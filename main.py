import discord
import discord.ext
from discord.ext import commands
import random

token = 'OTI2OTA3NDYwNzc2NzU5Mzg3.YdCf1w.3eNiroFxuTkaRXjS-H-nBsu0dAs'

client = discord.Client()

bot = commands.Bot(command_prefix='$')

bad_words = ["sus", "vent", "balls", "amogus", "among", "impostor", "obama"]

curse_respone = [
    "That's a bit sussy.",
    "hmmm you're a sussy baka",
    "when the imposter is sus",
    "You vented."
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if any(word in msg for word in bad_words):
        await message.channel.send(random.choice(curse_respone))
        print('"' + msg + '" was deemed sussy.')

client.run(token)

@bot.command()
async def ping(ctx):
	await ctx.channel.send("pong")

bot.run(token)