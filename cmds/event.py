import discord
from discord.ext import commands
from core.classes import Cog_EX
from cmds.bank import Bank
from cmds.money import Money
import json
import asyncio
import datetime

with open('setting.json', mode='r', encoding='utf8') as jfile:
   jdata = json.load(jfile)
class Event(Cog_EX):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['CHANNEL']))
        embed=discord.Embed(title=f'✨ ‖ **{member}** 加入!', color=0xff8800, timestamp = datetime.datetime.now())
        embed.set_author(name="🛑 成員加入通知 🛑")
        await channel.send(member.mention , embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['CHANNEL']))
        embed=discord.Embed(title=f'😢 ‖ **{member}** 離開了...', color=0xff8800, timestamp = datetime.datetime.now())
        embed.set_author(name="🛑 成員離開通知 🛑")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == '安安' :
            await msg.channel.send('嗨')
        elif msg.content == 'test':
            await msg.channel.send('<@&801115250165940244>') # @USER ==> '<@使用者ID>' #@ROLE ==> '<@&身分組ID>'
        elif msg.content == '早上好' :
            await msg.channel.send('中國\n我現在有冰淇淋')
        elif msg.content == '晚安' :
            await msg.channel.send('寶，晚安!')
        elif msg.content == '兩個禮拜以後' :
            await msg.channel.send('速度與激情9 ~')
        elif msg.content == '早安' :
            await msg.channel.send('拿鐵\n呼拉!')
        elif msg.content == '我好帥喔':
            await msg.delete()
            await msg.channel.send('不好意思，不要騙人啦')
        elif msg.content == '我好帥':
            await msg.delete()
            await msg.channel.send('不好意思，不要騙人啦')
        elif msg.content == '木瓜好漂亮':
            await msg.delete()
            await msg.channel.send('噓!，你太誠實了啦😎')
        elif msg.content == '木瓜好美':
            await msg.delete()
            await msg.channel.send('噓!，你太誠實了啦😎')
    

    #ERROR HANDLER
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        #https://youtu.be/ojSb06_jm9Y?list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN&t=2727
        if hasattr(ctx.command,'on_error'):
            return

        if isinstance(error,commands.errors.MissingRequiredArgument):
            embed=discord.Embed(title=" ❓‖ 指令不完整或錯誤，請重新輸入\n輸入 `>command` 查詢現有指令", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 發生錯誤 ⚠️")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.CommandNotFound):
            embed=discord.Embed(title=" ❓‖ 無此指令\n輸入 `>command` 查詢現有指令", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 發生錯誤 ⚠️")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=" 😕 ‖ 請通報 **管理員** 修復",color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 發生未知錯誤 ⚠️")
            await ctx.send(embed=embed)
    
    # https://youtu.be/ojSb06_jm9Y?list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN&t=1748
    #個別錯誤處理
    @Bank.lm.error
    async def lm_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            msg = await ctx.send("誰?")
            await asyncio.sleep(3)
            await ctx.message.delete()
            await msg.delete()
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            embed=discord.Embed(title=" ❓‖ 指令不完整或錯誤，請重新輸入\n輸入 `>command` 查詢現有指令", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 發生錯誤 ⚠️")
            await ctx.send(embed = embed)

    @Money.daily.error
    async def daily_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            cd = int(error.retry_after)
            H = int(cd / 3600)
            M = (int(cd / 60)- H*60)
            S = int(cd % 60)
            em = discord.Embed(title=f"✅ ‖ 已簽到\n冷卻時間 `{H}` H `{int(M)}` M `{int(S)}`S .", color=0xff0000, timestamp = datetime.datetime.now())
            em.set_author(name="⚠️ 冷卻時間 ⚠️")
            await ctx.send(embed=em)
        else:
            pass

    #新增反應獲得身分組
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id ==974926070451150899:
            if str(payload.emoji) == '<:emoji_1:801114598408192044>':
                guild = self.bot.get_guild(payload.guild_id)
                role = guild.get_role(974906252079550505)
                await payload.member.add_roles(role)
                embed=discord.Embed(title=f"✅ ‖ 已新增 {role} 身分組",color=0xff0000, timestamp = datetime.datetime.now())
                embed.set_author(name="💫 身分組領取通知 💫")
                await payload.member.send(embed = embed)

    #移除反應獲得身分組
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id ==974926070451150899:
            if str(payload.emoji) == '<:emoji_1:801114598408192044>':
                guild = self.bot.get_guild(payload.guild_id)
                user = guild.get_member(payload.user_id)
                role = guild.get_role(974906252079550505)
                await user.remove_roles(role)
                embed=discord.Embed(title=f"✅ ‖ 已移除 {role} 身分組",color=0xff0000, timestamp = datetime.datetime.now())
                embed.set_author(name="💫 身分組移除通知 💫")
                await user.send(embed = embed)
    
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