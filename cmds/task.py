from typing_extensions import Self
import discord
from discord.ext import commands
from core.classes import Cog_EX
import json, asyncio, datetime

class Task(Cog_EX):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(940826399227400222)
            while not self.bot.is_closed():
                await self.channel.send("Hi I'm running!")
                await asyncio.sleep(5)  #單位:秒       

        self.bg_task = self.bot.loop.create_task(interval())

    @commands.command()
    async def set_channel(self, ctx, ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'設定頻道為:{self.channel.mention}') #.mention-->標記

def setup(bot):
    bot.add_cog(Task(bot))