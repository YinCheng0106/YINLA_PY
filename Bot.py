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
    await bot.change_presence(status = discord.Status.idle,activity = discord.Game(name = "啟動中..."))
    print(">>機器人啟動完成<<")

async def ch_pr():
    await bot.wait_until_ready()

    statuses = [f" {len(bot.guilds)} 個伺服器 ‖ YINLA" , "查指令 ‖ >command", "discord.py ‖ YINLA"]

    while not bot.is_closed():

        status = random.choice(statuses)

        await bot.change_presence(status = discord.Status.dnd,activity = discord.Game(name = status))

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