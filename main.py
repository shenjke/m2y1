import discord
from discord.ext import commands
import random, os
 
 
intents = discord.Intents.default()
intents.message_content = True
 
bot = commands.Bot(command_prefix='$', intents=intents)
 
image = [{'mem1.jpg': 3}, {'mem2.jpg' : 2}, {'mem3.jpg' : 1}] 

 
@bot.command()
async def mem(ctx):

    chance = []
    for name, weight in image.items():
        chance.extend([name]*weight)


    image_name = random.choice(os.listdir('images', chance))
    with open(f'images/{image_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
 
bot.run('MTA5MzIwNDUwMDAzMTk5NTkyNg.Gri1mf.KkhK7bQmm4vlGecVS2Zvrl6lhc3KMjmY8zs8C4')