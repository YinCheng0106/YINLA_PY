import discord
from discord.ui import Button, View
from discord.ext import commands
from core.classes import Cog_EX
import asyncio

class Main(Cog_EX):

    @commands.command()
    async def ping(self, ctx):
        # 按鈕 # https://youtu.be/kNUuYEWGOxA
#        button1 = Button(label = "更新", style = discord.ButtonStyle.green, emoji = "🔁")

        msg = f'延遲 `{round(self.bot.latency*1000)}` ms'
        embed=discord.Embed(title = msg, color = 0x1eff00)
        embed.set_author(name = "🤖 機器人狀態 🤖")

        

#        async def button_callback(interaction):
#            await interaction.response.edit_message(embed = embed, view = view)

#        button1.callback = button_callback

#        view = View()
#        view.add_item(button1)
        
        await ctx.reply(mention_author = False ,embed = embed) #view = view


    @commands.command()
    async def say(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)
        embed=discord.Embed(title=f"已刪除 `{num}` 則訊息", color=0xff0000)
        embed.set_author(name="🛑 系統通知 🛑")
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(3)
        await msg.delete()

    @commands.command()
    async def command(self, ctx):
        embed=discord.Embed(title="📍 ‖ 指令專區", color=0xfbff00)
        embed.add_field(name=">say [內容]", value="讓機器人說話", inline=True)
        embed.add_field(name=">clean [數量]", value="清除訊息", inline=True)
        embed.add_field(name=">ping", value="檢視機器人延遲", inline=False)
        embed.add_field(name=">into", value="檢視機器人資訊", inline=False)
        embed.add_field(name=">yin", value="檢視機器人創作者資訊", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def into(self, ctx):
        embed=discord.Embed(title="機器人資訊", color=0x16a5fe)
        embed.set_author(name="YINLA", url="https://discord.gg/We6enK7wb3", icon_url="https://pbs.twimg.com/media/FOJUUgpVgAIwig9?format=jpg&name=4096x4096")
        embed.add_field(name="🎂 ‖ 誕生日期", value="`2022/02/09`", inline=True)
        embed.add_field(name="🛑 ‖ 正式啟用", value="`????/??/??`", inline=True)
        embed.add_field(name="🖥️ ‖ 程式", value="`PYTHON`", inline=True)
        embed.add_field(name="📍 ‖ 指令", value="`>`", inline=True)
        embed.set_footer(text="YinCheng#8104 製")
        await ctx.send(embed=embed)

    @commands.command()
    async def yin(self, ctx):
        embed=discord.Embed(title="機器人創作者資訊", color=0xffffff)
        embed.set_author(name="Yin Cheng", url="https://allmy.bio/yincheng", icon_url="https://i.imgur.com/TzmL9UQ.png" )
        embed.add_field(name="IG", value="\_yincheng\_", inline=False)
        embed.add_field(name="Discord", value="YinCheng#8104", inline=True)
        embed.add_field(name="Twitter", value="@Yin_Cheng0106", inline=False)
        embed.add_field(name="Twitch", value="胤啦(yincheng0106)", inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Main(bot))