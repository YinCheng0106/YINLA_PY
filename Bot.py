from re import T
import discord
from discord.ext import commands
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='yin',intents=intents)

@bot.event
async def on_ready():
    print(">>bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(940826399227400222)
    await channel.send(f'**{member}** join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(940826399227400222)
    await channel.send(f'**{member}** leave...')

@bot.command()
async def ping(ctx): 
    await ctx.send(f'{round(bot.latency*1000)} (ms)')


bot.run('OTQwNzc4NzQzNjM3NjA2NDUx.YgMWew._UGW_Ub2Xve4l3ctstkRJMRUJLo')