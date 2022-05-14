from configparser import MissingSectionHeaderError
from lib2to3.pgen2.token import AWAIT
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
    async def on_message(self, msg):
        if msg.content == '安安' :
            await msg.channel.send('嗨')
        elif msg.content == 'test' :
            await msg.channel.send('ok')
        elif msg.content == '早上好' :
            await msg.channel.send('中國\n我現在有冰淇淋')
        elif msg.content == '晚安' :
            await msg.channel.send('寶，晚安!')
        elif msg.content == '兩個禮拜以後' :
            await msg.channel.send('速度與激情9 ~')
        elif msg.content == '早安' :
            await msg.channel.send('拿鐵\n呼拉!')

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

    #新增反應獲得身分組
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id ==974926070451150899:
            if str(payload.emoji) == '<:emoji_1:801114598408192044>':
                guild = self.bot.get_guild(payload.guild_id)
                role = guild.get_role(974906252079550505)
                await payload.member.add_roles(role)
                await payload.member.send(f"已取得 **{role}** 身分組")

    #移除反應獲得身分組
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id ==974926070451150899:
            if str(payload.emoji) == '<:emoji_1:801114598408192044>':
                guild = self.bot.get_guild(payload.guild_id)
                user = guild.get_member(payload.user_id)
                role = guild.get_role(974906252079550505)
                await user.remove_roles(role)
                await user.send(f"已移除 **{role}** 身分組")
    
    #審核日誌 訊息刪除紀錄
#    @commands.Cog.listener()
#    async def on_message_delete(self, msg):
#        counter = 1
#        async for audilog in msg.guild.audit_logs(action = discord.AuditLogAction.message_delete):
#            if counter == 1:
#                await msg.channel.send("刪除訊息者:" + audilog.user.name)
#                counter += 1
#        await msg.channel.send("已刪除訊息：" + str(msg.content))
#        await msg.channel.send("訊息刪除者：" + str(msg.author))


def setup(bot):
    bot.add_cog(Event(bot))