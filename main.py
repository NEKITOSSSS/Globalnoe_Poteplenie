import discord
import random
from discord.ext import commands
import requests


import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)




@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')





@bot.command('fact')
async def python(ctx):
    response = random.choice(facts)
    await ctx.send(response)



@bot.command('util')
async def python(ctx):
    response = random.choice(utilization)
    await ctx.send(response)





facts = [
    'Вода — источник жизни на земле и требует особого отношения. Старайтесь экономить воду при каждой возможности и не допускайте загрязнения воды бытовым стоком.',
    'Мусор является одной из основных причин загрязнения окружающей среды, как в городах, так и в сельской местности. Ежедневно выбрасывается большое количество мусора, как бытового, так и промышленного характера. Старайтесь всегда бросать мусор только в специальные урны и научите своих детей этому.',
    'Одним из основных загрязнителей природы считаются пластиковые бутылки и различные полиэтиленовые изделия и пакеты. Всем известно, что пластиковые изделия почти не разлагаются в природе и при сжигании образуют ядовитые вещества загрязняя воздух.',
    'Энергия является неотъемлемой частью нашей жизни и невозможно представить жизнь без современных приборов и гаджетов. Однако, если использовать энергосберегающие и энергоэффективные приборы, то это заметно уменьшит спрос на электроэнергию и снизит нагрузку на окружающую среду.'
 
]
    

utilization = [
    'Стелянные тары и пластик нельзя выбрасывать не в специализированные контейнеры. ',
    'Сортируйте мусор! Отделяйте перерабатываемые отходы от неперерабатываемых',
 
]
    


bot.run("")    




