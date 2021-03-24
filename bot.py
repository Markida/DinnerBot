import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    print(f'{member}join!')
    channel = bot.get_channel(557849735785086978)
    await channel.send(f'{member}join!')

@bot.event
async def on_member_remove(member):
    print(f'{member}leave!')
    channel = bot.get_channel(557849735785086978)
    await channel.send(f'{member}leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}ms')
    


bot.run('ODIzOTEzNzkzNDI2ODE3MDc1.YFnvgw.f0vs0OomSq9iyCpHhkouIEMAqmc')


