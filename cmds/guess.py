import discord
from discord.ext import commands
from core.classes import Cog_EX
import json
import random
import asyncio
import datetime

with open('setting.json', mode='r', encoding='utf8') as jfile:
   jdata = json.load(jfile)


class Guess(Cog_EX):
    @commands.command()
    async def guess(self, ctx):
    
    # 檢查回傳的是否是同一個人(已及是否在同一個頻道)
        def check(number):
            return number.author == ctx.author and number.channel == ctx.message.channel
        global lowernumber
        global highernumber
    
        lowernumber = 1
        highernumber = 50
    
        number = random.randint(lowernumber, highernumber)
    # print(number)
    
        embed=discord.Embed(title="`1` ~ `50` 任意選一個數字", color=0xff0000, timestamp = datetime.datetime.now())
        embed.set_author(name="🕹️ 娛樂中心 🕹️")
        embed.set_thumbnail(url="https://cdn.dribbble.com/users/648258/screenshots/9070602/media/20cef9101ef2a1f1617b6b020ec97157.gif")
        await ctx.message.delete()
        await ctx.send(embed=embed)

    
        for i in range(0, 5):    
            response = await self.bot.wait_for('message', check = check)
        
            try : 
                guess = int(response.content) 
        
            except:
                embed=discord.Embed(title="請輸入數字", color=0xff0000, timestamp = datetime.datetime.now())
                embed.set_author(name="🕹️ 娛樂中心 🕹️")
                embed.set_thumbnail(url="https://cdn.dribbble.com/users/648258/screenshots/9070602/media/20cef9101ef2a1f1617b6b020ec97157.gif")
                await ctx.send(ctx.author.mention,embed=embed)
            
            if guess == number : 
                embed=discord.Embed(title="答對了!!", color=0xff0000, timestamp = datetime.datetime.now())
                embed.set_author(name="🕹️ 娛樂中心 🕹️")
                embed.set_thumbnail(url="https://cdn.dribbble.com/users/648258/screenshots/9070602/media/20cef9101ef2a1f1617b6b020ec97157.gif")
                await ctx.send(ctx.author.mention,embed=embed)
                break
            
            if guess > 50 :
                embed=discord.Embed(title="超過 `50` ，格式錯誤", color=0xff0000, timestamp = datetime.datetime.now())
                embed.set_author(name="🕹️ 娛樂中心 🕹️")
                embed.set_thumbnail(url="https://cdn.dribbble.com/users/648258/screenshots/9070602/media/20cef9101ef2a1f1617b6b020ec97157.gif")
                await ctx.send(embed=embed)

            if guess < 0 :
                embed=discord.Embed(title="低於 `1` ，格式錯誤", color=0xff0000, timestamp = datetime.datetime.now())
                embed.set_author(name="🕹️ 娛樂中心 🕹️")
                embed.set_thumbnail(url="https://cdn.dribbble.com/users/648258/screenshots/9070602/media/20cef9101ef2a1f1617b6b020ec97157.gif")
                await ctx.send(embed=embed)
            
            if 0 < guess < number:
                lowernumber = guess
                em=discord.Embed(title=f"比 `{lowernumber}` 大，比 `{highernumber}` 小", color=0xff0000, timestamp = datetime.datetime.now())
                em.set_author(name="🎰 終極密碼 🎰")
                await ctx.send(embed=em)

            
            if 50 > guess > number :
                highernumber = guess
                em_1=discord.Embed(title=f"比 `{lowernumber}` 大，比 `{highernumber}` 小", color=0xff0000, timestamp = datetime.datetime.now())
                em_1.set_author(name="🎰 終極密碼 🎰")
                await ctx.send(embed=em)
        else:
            embed=discord.Embed(title="GAME OVER", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="🕹️ 娛樂中心 🕹️")
            embed.set_thumbnail(url="https://i.gifer.com/QeMS.gif")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Guess(bot))