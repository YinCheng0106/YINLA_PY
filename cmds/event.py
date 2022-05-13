import discord
from discord.ext import commands
from core.classes import Cog_EX
import json

with open('setting.json', mode='r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

class Event(Cog_EX):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['CHANNEL']))
        await channel.send(f'**{member}** join!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['CHANNEL']))
        await channel.send(f'**{member}** leave...')

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ['hi','早安','早安咖啡','安安']
        if msg.content in keyword and msg.author !=self.bot.user:
            await msg.channel.send('拿鐵\n**呼拉!**')



def setup(bot):
    bot.add_cog(Event(bot))