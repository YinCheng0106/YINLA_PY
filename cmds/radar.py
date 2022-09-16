import mailbox
import discord
import requests
import json
from discord.ext import commands
from core.classes import Cog_EX
import datetime

class RADAR(Cog_EX):
    
    @commands.command()
    async def radar(self, ctx):
            radar = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0058-003?Authorization=CWB-85B18E4D-CE89-4D11-8018-F80812EA6E8F&format=JSON'
            b = requests.get(radar).json()
            

            time = str(b['cwbopendata']['dataset']['time']['obsTime'])
            url = str(b['cwbopendata']['dataset']['resource']['uri'])+'?'+time

            embed = discord.Embed(title="<a:ezgif:1000944717653090365> | 雷達回波圖",
                                description=f'時間：`{time}`',color=0x00FFFF, timestamp=datetime.datetime.now())
            embed.set_image(url=url)
            embed.set_footer(text="CWB 中央氣象局 提供", icon_url='https://media.discordapp.net/attachments/345147297539162115/732527875839885312/ROC_CWB.png')
            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(RADAR(bot))