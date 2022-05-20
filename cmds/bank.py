import discord
from discord.ext import commands
from core.classes import Cog_EX
import json
import random
import asyncio
import datetime

with open('setting.json', mode='r', encoding='utf8') as jfile:
   jdata = json.load(jfile)


async def open_account(user):
    pass

async def get_bank_data():
    pass

async def open_account(user):
        users = await get_bank_data()

        if str(user.id) in users:
            return False
        
        else:
            users[str(user.id)] = {}
            users[str(user.id)]["wallet"] = 0
            users[str(user.id)]["bank"] = 0

        with open("main_bank.json", mode = "w") as f:
            json.dump(users,f)
        
        return True

async def get_bank_data():
        with open("main_bank.json", mode = "r") as f:
            users = json.load(f)
        
        return users


class Bank(Cog_EX):

    @commands.command()
    async def m(self, ctx ):
        await open_account(ctx.author)

        user = ctx.author
        users = await get_bank_data()
        wallet = users[str(user.id)]["wallet"]
        bank = users[str(user.id)]["bank"]

        em = discord.Embed(title = f"{ctx.author} 的錢包", color = discord.Color.red(),timestamp = datetime.datetime.now())
        em.set_thumbnail(url = "https://3wtrade.com/wp-content/uploads/2021/08/bit.gif")
        em.set_author(name = "🏦 銀行資訊 🏦")
        em.add_field(name = "錢包餘額", value = f" `{wallet}` ")
        em.add_field(name = "銀行餘額", value = f" `{bank}` ")

        await ctx.send(ctx.author.mention,embed = em)

    @commands.command()
    async def lm(self, ctx, member : discord.Member ):
        await open_account(member)

        user = member
        users = await get_bank_data()
        wallet = users[str(user.id)]["wallet"]
        bank = users[str(user.id)]["bank"]

        em = discord.Embed(title = f"{member} 的錢包", color = discord.Color.red(),timestamp = datetime.datetime.now())
        em.set_thumbnail(url = "https://3wtrade.com/wp-content/uploads/2021/08/bit.gif")
        em.set_author(name = "🏦 銀行資訊 🏦")
        em.add_field(name = "錢包餘額", value = f" `{wallet}` ")
        em.add_field(name = "銀行餘額", value = f" `{bank}` ")

        await ctx.send(embed = em)
    #不知為何抓不到 user.avatar_url

def setup(bot):
    bot.add_cog(Bank(bot))