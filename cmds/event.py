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
        embed=discord.Embed(title=f'**{member}**加入!', color=0xff8800)
        embed.set_author(name="✨ 歡迎 ✨")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['CHANNEL']))
        embed=discord.Embed(title=f'**{member}**離開了...', color=0xff8800)
        embed.set_author(name="😢 喔不 😢")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, msg1):
        keyword = ['hi','早安','早安咖啡','安安']
        if msg1.content in keyword and msg1.author !=self.bot.user:
            await msg1.channel.send('拿鐵\n**呼拉!**')

    @commands.Cog.listener()
    async def on_message(self, msg2):
        keyword = ['早上好']
        if msg2.content in keyword and msg2.author !=self.bot.user:
            await msg2.channel.send('中國\n我現在有冰淇淋')

    @commands.Cog.listener()
    async def on_message(self, msg3):
        keyword = ['晚安','晚上好']
        if msg3.content in keyword and msg3.author !=self.bot.user:
            await msg3.channel.send('寶，晚安!')

    @commands.Cog.listener()
    async def on_message(self, msg4):
        keyword = ['兩個禮拜以後']
        if msg4.content in keyword and msg4.author !=self.bot.user:
            await msg4.channel.send('速度與激情9 ~')

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
            embed=discord.Embed(title="⚠️ 發生未知錯誤 ⚠️",color=0xff0000)
            await ctx.send(embed=embed)
    
    # https://youtu.be/ojSb06_jm9Y?list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN&t=1748
    #個別錯誤處理
    #@指令名稱.error
    #async def 指令名稱_error(self, ctx, error):
    #    if isinstance(error, commands.errors.MissingRequiredArgument):
    #        await ctx.send("錯誤訊息")
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        print(payload.emoji)
        print(payload.member)


def setup(bot):
    bot.add_cog(Event(bot))