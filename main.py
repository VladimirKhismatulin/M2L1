import discord
import random
import requests
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
images = os.listdir('images')
rares = os.listdir('rares')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def mem(ctx):
    if random.randint(1, 5) != 5:
        img = random.choice(images)
        with open(f'images/{img}', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file = picture)
    else:
        img = random.choice(rares)
        with open(f'rares/{img}', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file = picture)

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('fox')
async def fox(ctx):
    image_url = get_fox_image_url()
    await ctx.send(image_url)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("")
