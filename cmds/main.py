from re import purge
import discord
from discord.ext import commands
from core.classes import Cog_EX
import datetime

class Main(Cog_EX):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx): 
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def sayd(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)

    

    @commands.command()
    async def into(self, ctx):
        embed=discord.Embed(title="機器人資訊", color=0x16a5fe)
        embed.set_author(name="YINLA", url="https://discord.gg/We6enK7wb3", icon_url="https://pbs.twimg.com/media/FOJUUgpVgAIwig9?format=jpg&name=4096x4096")
        embed.add_field(name="誕生日期", value="2022/02/09", inline=True)
        embed.add_field(name="正式啟用", value="????/??/??", inline=True)
        embed.add_field(name="程式", value="PYTHON", inline=True)
        embed.add_field(name="指令", value="yin", inline=True)
        embed.set_footer(text="YinCheng#8104 製")
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Main(bot))