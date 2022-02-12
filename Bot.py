import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json', mode='r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='yin',intents=intents)

@bot.event
async def on_ready():
    print(">>bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['CHANNEL']))
    await channel.send(f'**{member}** join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['CHANNEL']))
    await channel.send(f'**{member}** leave...')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])