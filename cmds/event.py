from configparser import MissingSectionHeaderError
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
    #ERROR HANDLER
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        #https://youtu.be/ojSb06_jm9Y?list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN&t=2727
        if hasattr(ctx.command,'on_error'):
            return

        if isinstance(error,commands.errors.MissingRequiredArgument):
            embed=discord.Embed(title="指令不完整，請重新輸入", color=0xff0000)
            embed.set_author(name="⚠️ 發生錯誤 ⚠️")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.CommandNotFound):
            embed=discord.Embed(title="無此指令", color=0xff0000)
            embed.set_author(name="⚠️ 發生錯誤 ⚠️")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(color=0xff0000)
            embed.set_author(name="⚠️ 發生未知錯誤 ⚠️")
            await ctx.send(embed=embed)
    
    # https://youtu.be/ojSb06_jm9Y?list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN&t=1748
    #個別錯誤處理
    #@指令名稱.error
    #async def 指令名稱_error(self, ctx, error):
    #    if isinstance(error, commands.errors.MissingRequiredArgument):
    #        await ctx.send("錯誤訊息")
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction)


def setup(bot):
    bot.add_cog(Event(bot))