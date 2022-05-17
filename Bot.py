import discord
from discord.ext import commands
import json
import os
import asyncio
import random

with open('setting.json', mode='r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='>',intents = intents)

@bot.event
async def on_ready():

    print(">>bot is online<<")
#    game = discord.Activity(type = discord.ActivityType.watching, name = "如何建構 內臟", url = "https://www.twitch.tv/yincheng0106" ) #機器人狀態
#    await bot.change_presence(status = discord.Status.dnd, activity = game)

async def ch_pr():
    await bot.wait_until_ready()

    statuses = [f"管理 {len(bot.guilds)} 個伺服器" , "查詢指令 >command", "discord.py"]

    while not bot.is_closed():

        status = random.choice(statuses)

        await bot.change_presence(activity = discord.Game(name = status))

        await asyncio.sleep(5)

bot.loop.create_task(ch_pr())

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    embed=discord.Embed(title=f'✅ ‖ **{extension}** 載入成功',color=0x00ff62)
    embed.set_author(name="🛑 系統通知 🛑")
    await ctx.send(embed=embed)

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    embed=discord.Embed(title=f'✅ ‖ **{extension}** 移除成功',color=0x00ff62)
    embed.set_author(name="🛑 系統通知 🛑")
    await ctx.send(embed=embed)
    
@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    embed=discord.Embed(title=f'✅ ‖ 重載 **{extension}** 成功!',color=0x00ff62)
    embed.set_author(name="🛑 系統通知 🛑")
    await ctx.send(embed=embed)


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN']) 