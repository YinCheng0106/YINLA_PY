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
    money = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]    
    return money


async def update_bank(user, change = 0, mode = "wallet"):
    pass
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    with open("main_bank.json", "w") as f:
        json.dump(users, f)
    bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]    
    return bal


class Money(Cog_EX):
    # >slots [押金] [倍率]
    @commands.command()
    async def slots(self, ctx, amount = None, mang = None):
        pass
        await open_account(ctx.author)
        if mang == None:
            await ctx.send("請輸入倍率")
            return

        bal = await update_bank(ctx.author)
        amount = int(amount)
        mang = int(mang)

        if bal[0] <= 0:
            await ctx.send("沒錢的，滾拉")
            return 
        if amount > bal[0]:
            await ctx.send("你沒這麼多錢拉幹")
            return
        if amount < 0:
            await ctx.send("正整數...")
            return
        # 做出限制
        if amount > 200 or mang > 10 :
            await ctx.send("不接受太高金額及倍率, 最高為199$$") 
            return
        final = []
        for i in range(3):
            a = random.choice(["X", "O", "Q"])
            final.append(a)
        ans = mang * amount
        pos = mang * amount * -1
        # win
        if final[0] == final[1] == final[2]:
            await update_bank(ctx.author, ans)
            await ctx.send("想贏嗎??")
            await asyncio.sleep(3)
            await ctx.send(str(final))
            await ctx.send(f"你贏了 `{ans}` 塊錢")
        # lose
        else:
            await update_bank(ctx.author, pos)
            await ctx.send("想贏嗎??")
            await asyncio.sleep(3)
            await ctx.send(str(final))
            await ctx.send(f"你輸了 `{pos}` 塊錢")

    @commands.command()
    async def beg(self, ctx):
        pass

        await open_account(ctx.author)

        users = await get_bank_data()
        user = ctx.author

        earnings = random.randrange(101)

        await ctx.send(f"有人給你 {earnings} 塊錢")

        users[str(user.id)]["wallet"] += earnings

        with open("main_bank.json", mode = "w") as f:
            json.dump(users, f)

    @commands.command()
    async def withdraw(self, ctx, amount = None):
        pass
        await open_account(ctx.author)
        if amount == None:
            await ctx.send("請輸入數字")
            return
        bal = await update_bank(ctx.author)
        amount = int(amount)
        if amount > bal[1]:
            await ctx.send("你沒這麼多錢拉幹")
            return 
        if amount > 200:
            await ctx.send("要小於200喔")
            return
        if amount< 0:
            await ctx.send("北七喔，錢有負的喔")
            return

        await update_bank(ctx.author, amount)
        await update_bank(ctx.author, -1 * amount, "bank")
        await ctx.send(f"你提款了 { amount } 塊錢!!!")

    @commands.command()
    async def deposit(self, ctx, amount = None):
        pass
        await open_account(ctx.author)
        if amount == None:
            await ctx.send("請輸入數字")
            return
        bal = await update_bank(ctx.author)
        amount = int(amount)
        if amount > bal[0]:
            await ctx.send("你沒這麼多錢拉幹")
            return 
        if amount > 200:
            await ctx.send("要小於200喔")
            return
        if amount< 0:
            await ctx.send("北七喔，錢有負的喔")
            return
            
        await update_bank(ctx.author, -1 * amount)
        await update_bank(ctx.author, amount, "bank")
        await ctx.send(f"你存了 { amount } 塊錢!!!")
    
    @commands.command()
    async def send(self, ctx, member:discord.Member, amount = None):
        await open_account(ctx.author)
        await open_account(member)
        if amount == None:
            await ctx.send("請輸入數字")
            return 
        bal = await update_bank(ctx.author)
        
        if amount == "all":
            amount = bal[0]
        amount = int(amount)
        if amount > bal[1]:
            await ctx.send("你沒這麼多錢拉幹")
            return 
        if amount< 0:
            await ctx.send("北七喔，錢有負的喔")
            return
        await update_bank(ctx.author, -1 * amount, "bank")
        await update_bank(member, amount, "bank")
        member = str(member)
        member = member.split("#")[0]
        await ctx.send(f"你給了{ member } { amount } 塊錢!!!")

def setup(bot):
    bot.add_cog(Money(bot))
