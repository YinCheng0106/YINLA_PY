import datetime
import discord
from discord.ui import Button, View
from discord.ext import commands
from core.classes import Cog_EX
import asyncio
import random

class Main(Cog_EX):

    @commands.command()
    async def ping(self, ctx):
        # 按鈕 # https://youtu.be/kNUuYEWGOxA
        button1 = Button(label = "更新", style = discord.ButtonStyle.green, emoji = "🔁")

        async def button_callback(interaction):
            embed2=discord.Embed(title =f'延遲 `{round(self.bot.latency*1000)}` ms', color = 0x1eff00, timestamp = datetime.datetime.now())
            embed2.set_author(name = "🤖 機器人狀態 🤖")
            msg = await interaction.response.edit_message(embed = embed2, view = view)

        button1.callback = button_callback
        

        view = View()
        view.add_item(button1)
        

        embed=discord.Embed(title =f'延遲 `{round(self.bot.latency*1000)}` ms', color = 0x1eff00, timestamp = datetime.datetime.now())
        embed.set_author(name = "🤖 機器人狀態 🤖")

        msg = await ctx.reply(mention_author = False, embed = embed, view = view)


    @commands.command()
    async def timer(self, ctx, seconds):

        secondint = int(seconds)
        await ctx.message.delete()
        if secondint > 600:
            embed=discord.Embed(title="我無法計時那麼久...(最多 600 秒)", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="🛑 系統通知 🛑")
            msg = await ctx.send(embed = embed)
            await ctx.message.delete()
            await asyncio.sleep(3)
            await msg.delete()

        if secondint <= 0:
            embed=discord.Embed(title="拜託...時間沒有負的", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="🛑 系統通知 🛑")
            msg = await ctx.send(embed = embed)
            await ctx.message.delete()
            await asyncio.sleep(3)
            await msg.delete()
        embed = discord.Embed(title=f"剩餘時間：`{seconds}`", color= 0xff0000, timestamp = datetime.datetime.now())
        embed.set_author(name="⏱️ 計時器 ⏱️")
        message = await ctx.send(embed = embed)
            
        while True:
            secondint -= 1
            
            embed2 = discord.Embed(title=f"剩餘時間：`{secondint}`", color=0xff0000, timestamp = datetime.datetime.now())
            embed2.set_author(name="⏱️ 計時器 ⏱️")
            msg = await message.edit(embed = embed2)

            if secondint == 0:
                break
            await asyncio.sleep(1)
        
        embed3 = discord.Embed(
            title = f"你時間到了!!\n 你所設定的時間為 `{seconds}`",
            color = 0xff0000,
            timestamp = datetime.datetime.now()
            )
        await ctx.send(ctx.author.mention, embed = embed3)
        
        await msg.delete()


    @commands.command()
    async def avatar(self, ctx, user : discord.Member):
        embed = discord.Embed(
            title = f"{user.name} 的頭像",
            color = user.color,
            timestamp = datetime.datetime.now()
        )
        embed.set_image(url = user.avatar)
        await ctx.reply(mention_author = False, embed = embed)


    @commands.command()
    async def profile(self, ctx, user : discord.Member):
        embed = discord.Embed(
            title = user.name,
            color = user.color,
            timestamp = datetime.datetime.now()
        )
        embed.set_thumbnail(url = user.avatar)
        embed.set_author(name = "個人檔案", icon_url = user.avatar)
        embed.add_field(name = "暱稱", value = user.nick)
        embed.add_field(name = "狀態", value = user.status, inline = False)
        embed.add_field(name = "建立帳號時間", value = f"<t:{int(user.created_at.timestamp())}:f>\n<t:{int(user.created_at.timestamp())}:R>",inline = False)
        embed.add_field(name = "加入伺服時間", value = f"<t:{int(user.joined_at.timestamp())}:f>\n<t:{int(user.joined_at.timestamp())}:R>")
        embed.set_footer(text = "YINLA", icon_url= "https://cdn.discordapp.com/avatars/940778743637606451/d8771ac9d0903242122e6bb89161f071.png")
        await ctx.reply(mention_author = False, embed = embed)
    
    @commands.command()
    async def sp(self, ctx):
        embed = discord.Embed(
            title = ctx.message.guild.name,
            color = 0x0000ff,
            timestamp = datetime.datetime.now()
        )
        embed.set_thumbnail(url = ctx.message.guild.icon )
        #embed.add_field(name = "建立伺服時間", value = f"<t:{int(ctx.message.guild.created_at.timestamp())}:f>\n<t:{int(ctx.message.guild.created_at.timestamp())}:R>")
        embed.add_field(name = "伺服器擁有者", value = f"<@{ctx.message.guild.owner_id}>")
        #embed.add_field(name = "伺服主要語言", value = " ")
        #embed.add_field(name = "文字頻道數量", value = f"`{len(ctx.message.guilds.text_channels)}` 個")
        #embed.add_field(name = "語音頻道數量", value = f"`{len(ctx.message.guilds.voice_channels)}` 個")
        embed.set_footer(text = "YINLA", icon_url= "https://cdn.discordapp.com/avatars/940778743637606451/d8771ac9d0903242122e6bb89161f071.png")
        await ctx.reply(mention_author = False, embed = embed)

    @commands.command()
    async def nt(self, ctx):
    
        today = datetime.datetime.now()
        dt = today.strftime(" ``%m`` / ``%d`` / ``%Y``"+" "+"``%H`` : ``%M`` : ``%S``")
        embed = discord.Embed(title= dt , color=0xff0000)
        embed.set_author(name="🕰️ 現在時間 🕰️")
        
        time = await ctx.send(embed = embed)
        await ctx.message.delete()
        await asyncio.sleep(10)
        await time.delete()
        
            


    @commands.command()
    async def 泡麵(self, ctx):
#        button2 = Button(label = "完成", style = discord.ButtonStyle.green, emoji = "🍽️")
        secondint = 180

#        async def button_callback(interaction):
#            await interaction.response.delete_message()

#        button2.callback = button_callback

#        view = View()
#        view.add_item(button2)

        embed = discord.Embed(title=f"剩餘時間 : `{secondint}`", color=0xff0000, timestamp = datetime.datetime.now())
        embed.set_author(name="⏱️ 泡麵計時器 ⏱️")
        message = await ctx.send(embed = embed)
            
        while True:
            secondint -= 1
            if secondint == 0:
                break

            embed2 = discord.Embed(title=f"剩餘時間 : `{secondint}`", color=0xff0000, timestamp = datetime.datetime.now())
            embed2.set_author(name="⏱️ 泡麵計時器 ⏱️")

            msg = await message.edit(embed = embed2)
            await asyncio.sleep(1)
        fin = await ctx.send(f"{ctx.author.mention} 你泡麵可以吃了!!" )
        await ctx.message.delete()
        await msg.delete()
        await asyncio.sleep(60)
        await fin.delete()
    

    @commands.command()
    async def say(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)


    @commands.command()
    async def clean(self, ctx, num:int):
        if num <= 1:
            embed=discord.Embed(title=" ❓‖ 訊息數量必須為 `正值`\n輸入 `>command` 查詢現有指令", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 發生錯誤 ⚠️")
            embed.set_footer(text = "YINLA", icon_url= "https://cdn.discordapp.com/avatars/940778743637606451/d8771ac9d0903242122e6bb89161f071.png")
            msg = await ctx.send(embed = embed)
            await asyncio.sleep(3)
            await ctx.message.delete()
            await asyncio.sleep(2)
            await msg.delete()
        else:
            await ctx.channel.purge(limit=num+1)
            embed=discord.Embed(title=f"已刪除 `{num}` 則訊息", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="🛑 系統通知 🛑")
            embed.set_footer(text = "YINLA", icon_url= "https://cdn.discordapp.com/avatars/940778743637606451/d8771ac9d0903242122e6bb89161f071.png")
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(3)
            await msg.delete()


    @commands.command()
    async def command(self, ctx):
        embed=discord.Embed(title="📍 ‖ 指令專區", color=0xfbff00, timestamp = datetime.datetime.now())
        
        embed.add_field(name=">泡麵", value="煮泡麵時幫你計時(180秒)", inline=True)
        embed.add_field(name=">timer [秒數]", value="計時器(秒)", inline=True)
        embed.add_field(name=">nt", value="現在時間", inline=True)
        embed.add_field(name=">say [內容]", value="讓機器人說話", inline=True)
        embed.add_field(name=">daily", value="簽到 (天)", inline=True)
        embed.add_field(name=">m", value="查詢錢包", inline=True)
        embed.add_field(name=">lm [@mention]", value="查詢其他用戶的錢包", inline=True)
        embed.add_field(name=">withdraw [金額]", value="提款", inline=True)
        embed.add_field(name=">deposit [金額]", value="存款", inline=True)
        embed.add_field(name=">send [@mention] [金額]", value="轉帳", inline=True)
        embed.add_field(name=">abb", value="1A2B", inline=True)
        embed.add_field(name=">slots [押金] [倍率]", value="拉霸機", inline=True)
        embed.add_field(name=">guess", value="終極密碼", inline=True)
        embed.add_field(name=">radar", value="雷達回波圖", inline=False)
        embed.add_field(name=">eq", value="最新 有編號 有感地震", inline=True)
        embed.add_field(name=">eqs", value="最新 小區域 有感地震", inline=False)


        embed.add_field(name=">clean [數量]", value="清除訊息", inline=False)
        embed.add_field(name=">avatar", value="用戶頭貼抓取功能", inline=True)
        embed.add_field(name=">profile", value="用戶個人簡介", inline=True)
        embed.add_field(name=">sp", value="伺服器簡介", inline=True)
        embed.add_field(name=">ping", value="檢視機器人延遲", inline=False)
        embed.add_field(name=">info", value="檢視機器人資訊", inline=False)
        embed.add_field(name=">yin", value="檢視機器人創作者資訊", inline=False)
        embed.set_footer(text = "YINLA", icon_url= "https://cdn.discordapp.com/avatars/940778743637606451/d8771ac9d0903242122e6bb89161f071.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def info(self, ctx):
        embed=discord.Embed(title="機器人資訊", color=0x16a5fe, timestamp = datetime.datetime.now())
        embed.set_author(name="YINLA", url="https://discord.gg/We6enK7wb3", icon_url="https://cdn.discordapp.com/avatars/940778743637606451/d8771ac9d0903242122e6bb89161f071.png")
        embed.add_field(name="🎂 ‖ 誕生日期", value="`2022/02/09`", inline=True)
        embed.add_field(name="🛑 ‖ 正式啟用", value="`????/??/??`", inline=True)
        embed.add_field(name="🖥️ ‖ 程式", value="`PYTHON`", inline=True)
        embed.add_field(name="📍 ‖ 指令", value="`>`", inline=True)
        embed.set_footer(text = "YINLA | YinCheng#8104 製", icon_url= "https://cdn.discordapp.com/avatars/940778743637606451/d8771ac9d0903242122e6bb89161f071.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def yin(self, ctx):
        embed=discord.Embed(title="機器人創作者資訊", color=0xffffff, timestamp = datetime.datetime.now())
        embed.set_author(name="Yin Cheng", url="https://allmy.bio/yincheng", icon_url="https://avatars.githubusercontent.com/u/99303523?v=4" )
        embed.add_field(name="IG", value="\_yincheng\_", inline=False)
        embed.add_field(name="Discord", value="YinCheng#8104", inline=True)
        embed.add_field(name="Twitter", value="@Yin_Cheng0106", inline=False)
        embed.add_field(name="Twitch", value="胤啦(yincheng0106)", inline=True)
        embed.set_footer(text = "YINLA | YinCheng#8104 製", icon_url= "https://cdn.discordapp.com/avatars/940778743637606451/d8771ac9d0903242122e6bb89161f071.png")
        await ctx.send(embed=embed)



#    @commands.command()
#    async def test(self, ctx):
#        embed = discord.Embed(title = f"real time embed test", color = discord.Color.green())
#        embed.add_field(name = 'Test', value = 'Hello this is a test')

#        update = await ctx.send(embed = embed)

#        new_em = discord.Embed(title = f"real time embed test", color = discord.Color.green())
#        new_em.add_field(name = 'Test', value = 'This text has changed')
#        update = await ctx.send(embed = new_em)
#        await update.edit(embed= new_em)

def setup(bot):
    bot.add_cog(Main(bot))