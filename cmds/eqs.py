
import mailbox
import discord
import requests
import json
from discord.ext import commands
from core.classes import Cog_EX
import datetime


class EQS(Cog_EX):

    @commands.command()
    async def eqs(self, ctx):
        cwbAPI_1 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization=CWB-85B18E4D-CE89-4D11-8018-F80812EA6E8F&format=JSON'
        b = requests.get(cwbAPI_1).json()

        time = str(b['records']['earthquake'][0]
                    ['earthquakeInfo']['originTime'])
        location = str(b['records']['earthquake'][0]['earthquakeInfo']['epiCenter']['location']) + " " + "東經：" + str(b['records']['earthquake'][0]['earthquakeInfo']
                                                                                                                        ['epiCenter']['epiCenterLon']['value']) + " " + "北緯：" + str(b['records']['earthquake'][0]['earthquakeInfo']['epiCenter']['epiCenterLat']['value'])
        depth = str(b['records']['earthquake'][0]
                    ['earthquakeInfo']['depth']['value'])
        magnitude = str(b['records']['earthquake'][0]
                        ['earthquakeInfo']['magnitude']['magnitudeValue'])
        message = str(b['records']['earthquake'][0]['reportContent'])
        img = str(b['records']['earthquake'][0]['reportImageURI'])

        m = int(b['records']['earthquake'][0]['earthquakeInfo']
                ['magnitude']['magnitudeValue'])

        if m == 0:
            msg = "⚪ " + magnitude + " `(極微)`"
        elif m == 1:
            msg = "🟢 " + magnitude + " `(極微)`"
        elif m == 2:
            msg = "🟢 " + magnitude + " `(極微)`"
        elif m == 3:
            msg = "🟢 " + magnitude + " `(微小)`"
        elif m == 4:
            msg = "🟡 " + magnitude + " `(輕微)`"
        elif m == 5:
            msg = "🟠 " + magnitude + " `(中等)`"
        elif m == 6:
            msg = "🔴 " + magnitude + " `(強烈)`"
        elif m == 7:
            msg = "🟣 " + magnitude + " `(重大)`"
        elif m == 8:
            msg = "🟣 " + magnitude + " `(極大)`"
        elif m == 9:
            msg = "⚫ " + magnitude + " `(極大)`"
        else:
            msg = "❓`(未知)`"

        embed = discord.Embed(title="<a:ezgif:1000944717653090365> | 地震報告",
                                description=message, color=0xff0000, timestamp=datetime.datetime.now())
        embed.add_field(name="編號", value="`小區域有感地震`")
        embed.add_field(name="發生時間", value=f"`{time}`")
        embed.add_field(name="震央位置", value=f"`{location}`")
        embed.add_field(name="深度", value=f"`{depth}`" + " 公里")
        embed.add_field(name="芮氏規模", value=msg)
        embed.set_image(url=img)
        embed.set_footer(
            text="地震報告提供", icon_url='https://media.discordapp.net/attachments/345147297539162115/732527875839885312/ROC_CWB.png')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(EQS(bot))
