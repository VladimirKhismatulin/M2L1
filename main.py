import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def mem(ctx):
    a = random.randint(1, 3)
    if a == 1:
        with open('images/mem1.jpg', 'rb') as f:
            await ctx.send(file = discord.File(f))
    elif a == 2:
        with open('images/mem2.jpg', 'rb') as f:
            await ctx.send(file = discord.File(f))
    elif a == 3:
        with open('images/mem3.jpg', 'rb') as f:
            await ctx.send(file = discord.File(f))

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("")
