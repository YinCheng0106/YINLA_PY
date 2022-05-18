import discord
from discord.ext import commands
from core.classes import Cog_EX
import json
import random
import asyncio

with open('setting.json', mode='r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

async def open_account(user):
    pass

async def get_bank_data():
    pass

async def update_bank(user, change = 0, mode = "wallet"):
    pass
    users = await get_bank_data()
    users[str(user.id)][mode] += change

    with open("main_bank.json", "w") as f:
        json.dump(users, f)

    money = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]    
    return money

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

async def update_bank(user, change = 0, mode = "wallet"):
    pass
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    with open("main_bank.json", "w") as f:
        json.dump(users, f)
    bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]    
    return bal



class Bank(Cog_EX):

    @commands.command()
    async def money(self, ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()
        wallet = users[str(user.id)]["wallet"]
        bank = users[str(user.id)]["bank"]

        em = discord.Embed(title = f"{ctx.author.name} 的錢包", color = discord.Color.red())
        em.add_field(name = "錢包餘額", value = wallet)
        em.add_field(name = "銀行餘額", value = bank)
        await ctx.send(embed = em)

    # >slots [押金] [倍率]




def setup(bot):
    bot.add_cog(Bank(bot))