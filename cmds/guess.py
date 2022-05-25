import discord
from discord.ext import commands
from core.classes import Cog_EX
import json
import random
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
        highernumber = 100
    
        number = random.randint(lowernumber, highernumber)
        print(number)
    # print(number)
    
        embed=discord.Embed(title="`1` ~ `100` 任意選一個數字", color=0xff0000, timestamp = datetime.datetime.now())
        embed.set_author(name="🕹️ 娛樂中心 🕹️")
        embed.set_thumbnail(url="https://cdn.dribbble.com/users/648258/screenshots/9070602/media/20cef9101ef2a1f1617b6b020ec97157.gif")
        await ctx.message.delete()
        await ctx.send(ctx.author.mention,embed=embed)


        for i in range(10):    
            response = await self.bot.wait_for('message', check = check)
        
            try : 
                guess = int(response.content) 

        
            except:
                embed=discord.Embed(title="🤔 ‖ 請輸入數字", color=0xff0000, timestamp = datetime.datetime.now())
                embed.set_author(name="🕹️ 娛樂中心 🕹️")
                embed.set_thumbnail(url="https://cdn.dribbble.com/users/648258/screenshots/9070602/media/20cef9101ef2a1f1617b6b020ec97157.gif")
                await ctx.send(ctx.author.mention,embed=embed)
            
            if guess == number : 
                embed=discord.Embed(title="✅ ‖ 答對了!!", color=0xff0000, timestamp = datetime.datetime.now())
                embed.set_author(name="🕹️ 娛樂中心 🕹️")
                embed.set_thumbnail(url="https://c.tenor.com/uCPMfBXrypUAAAAC/win-minions.gif")
                await ctx.send(ctx.author.mention,embed=embed)
                break
            
            if guess > 100 :
                embed=discord.Embed(title="❎ ‖ 超過 `100` ，格式錯誤", color=0xff0000, timestamp = datetime.datetime.now())
                embed.set_author(name="🕹️ 娛樂中心 🕹️")
                embed.set_thumbnail(url="https://cdn.dribbble.com/users/648258/screenshots/9070602/media/20cef9101ef2a1f1617b6b020ec97157.gif")
                await ctx.send(embed=embed)

            if guess < 1 :
                embed=discord.Embed(title="❎ ‖ 低於 `1` ，格式錯誤", color=0xff0000, timestamp = datetime.datetime.now())
                embed.set_author(name="🕹️ 娛樂中心 🕹️")
                embed.set_thumbnail(url="https://cdn.dribbble.com/users/648258/screenshots/9070602/media/20cef9101ef2a1f1617b6b020ec97157.gif")
                await ctx.send(embed=embed)
            
            if 0 < guess < number:
                lowernumber = guess
                em1=discord.Embed(title=f"🤔 ‖ 比 `{lowernumber}` 大，比 `{highernumber}` 小", color=0xff0000, timestamp = datetime.datetime.now())
                em1.set_author(name="🎮 終極密碼 🎮")
                await ctx.send(embed=em1)

            if 101 > guess > number :
                highernumber = guess
                em2=discord.Embed(title=f"🤔 ‖ 比 `{lowernumber}` 大，比 `{highernumber}` 小", color=0xff0000, timestamp = datetime.datetime.now())
                em2.set_author(name="🎮 終極密碼 🎮")
                await ctx.send(embed=em2)
        else:
            embed=discord.Embed(title=f"GAME OVER\n答案為: `{number}`", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="🕹️ 娛樂中心 🕹️")
            embed.set_thumbnail(url="https://i.gifer.com/QeMS.gif")
            await ctx.send(embed=embed)

    @commands.command()
    async def abb(self, ctx):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.message.channel
        await ctx.message.delete()
        embed=discord.Embed(title="請輸入不重複四位數(1-9)", color=0xff0000, timestamp = datetime.datetime.now())
        embed.set_author(name="🕹️ 娛樂中心 🕹️")
        await ctx.send(embed=embed)
        A = [1,2,3,4,5,6,7,8,9]
        ans = random.sample(A,4)
        print(ans)
        guess = await self.bot.wait_for("message",check = check)
        guess = guess.content
        g_n = [int(i) for i in guess]
        a = 0
        b = 0
        times = 1
        while 1 == 1:
            
            for i in range(4):
                for j in range(4):
                    if ans[i] == g_n[j] and i == j:
                            a += 1
                    if ans[i] == g_n[j] and i != j:
                            b += 1
            if a != 4:
                embed=discord.Embed(title=f"`{a}` A`{b}` B, 已猜`{times}`次", color=0xff0000, timestamp = datetime.datetime.now())
                embed.set_author(name="🕹️ 娛樂中心 🕹️")
                await ctx.send(embed=embed)
            if a == 4:
                em2=discord.Embed(title=f"恭喜答對了!!\n答案為`{ans}`，花了`{times}`次", color=0xff0000, timestamp = datetime.datetime.now())
                em2.set_author(name="🎮 1A2B 🎮")
                await ctx.send(ctx.author.mention,embed=em2)
                break

            guess = await self.bot.wait_for("message",check = check)
            guess = guess.content
            g_n = [int(i) for i in guess]
            a = 0
            b = 0
            times += 1
            if a!=4 and times == 2:
                embed=discord.Embed(title=f"GAME OVER\n答案為`{ans}`", color=0xff0000, timestamp = datetime.datetime.now())
                embed.set_author(name="🕹️ 娛樂中心 🕹️")
                embed.set_thumbnail(url="https://i.gifer.com/QeMS.gif")
                await ctx.send(embed=embed)
                break


def setup(bot):
    bot.add_cog(Guess(bot))