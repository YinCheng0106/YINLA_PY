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
    async def em(self, ctx):
        embed=discord.Embed(title="About", description="YinCheng0106", color=0xfa0000, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="YinCheng", url="https://allmy.bio/yincheng", icon_url="https://media.giphy.com/media/sJWNLTclcvVmw/giphy.gif")
        embed.set_thumbnail(url="https://media.giphy.com/media/sJWNLTclcvVmw/giphy.gif")
        embed.add_field(name="1", value="123", inline=False)
        embed.add_field(name="2", value="123", inline=True)
        embed.set_footer(text="123456")
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Main(bot))