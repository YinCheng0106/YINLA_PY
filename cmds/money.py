import discord
from discord.ext import commands
from core.classes import Cog_EX
import json
import random
import asyncio
import datetime

with open('p/setting.json', mode='r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

#shop = [
#            {"name": "Watch", "price": 8},
#            {"name": "Laptop", "price": 87},
#            {"name": "PC", "price": 870},
#            {"name": "PS5", "price": 690},
#            {"name": "Cat", "price": 1000}
#        ]

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

#async def buySomething(user, itemName, amount):
#    name = None
#    itemName = itemName.lower()
#    for item in shop:
#        Item_Name = item["name"].lower()
#        if Item_Name == itemName:
#            name = Item_Name
#            price = item["price"]
#            break
#    if name == None:
#        return [False, 1]
#    cost = price * amount
    
#    users = await get_bank_data()
#    bal = await update_bank(user)
    
#    if bal[0] < cost :
#        return [False , 2] 
#    try:
    # 使用count確認位置
#        count = 0
    # 預設為0先認定它不存在，如存在則改為1
#        exist = 0
#        for cargo in users[str(user.id)]["bag"]:
#            item = cargo["item"]
#            if item == itemName:
#                oldAmount = cargo["amount"]
#                newAmount = oldAmount + amount
#                users[str(user.id)]["bag"][count]["amount"] = newAmount
#                exist = 1
#                break
#            count += 1
#        if exist == 0:
#            beginexist = {"item":itemName, "amount":amount}
#            users[str(user.id)]["bag"].append(beginexist)
        
#    except:
#        beginexist = {"item" : itemName, "amount" : amount}
#        users[str(user.id)]["bag"] = [beginexist]
#    with open("bank.json", "w") as f:
#        json.dump(users, f)
    
#    await update_bank(user, cost*-1, "wallet")
#    return [True, "worked"]


class Money(Cog_EX):
    # >slots [押金] [倍率]
    @commands.command()
    async def slots(self, ctx, amount = None, mang = None):
        pass
        await open_account(ctx.author)
        if amount == None:
            embed=discord.Embed(title="請輸入金額+倍率", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 錯誤 ⚠️")
            embed.set_thumbnail(url="https://play-lh.googleusercontent.com/i-0HlK6I-K5ZVI28HFa4iXz0T22Mg2WjQ4gMsEYvqmSNdifp2NE41ZiaUCavmbIimQ")
            msg = await ctx.send(embed=embed)
            await ctx.message.delete()
            await asyncio.sleep(5)
            await msg.delete()
            return

        if mang == None:
            embed=discord.Embed(title="請輸入正整數的倍率，並且介於 0 ~ 10 之間", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 錯誤 ⚠️")
            embed.set_thumbnail(url="https://play-lh.googleusercontent.com/i-0HlK6I-K5ZVI28HFa4iXz0T22Mg2WjQ4gMsEYvqmSNdifp2NE41ZiaUCavmbIimQ")
            msg = await ctx.send(embed=embed)
            await ctx.message.delete()
            await asyncio.sleep(5)
            await msg.delete()
            return

        bal = await update_bank(ctx.author)
        amount = int(amount)
        mang = int(mang)

        if mang < 0:
            embed=discord.Embed(title="請輸入正整數的倍率，並且介於 0 ~ 10 之間", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 錯誤 ⚠️")
            embed.set_thumbnail(url="https://play-lh.googleusercontent.com/i-0HlK6I-K5ZVI28HFa4iXz0T22Mg2WjQ4gMsEYvqmSNdifp2NE41ZiaUCavmbIimQ")
            msg = await ctx.send(embed=embed)
            await ctx.message.delete()
            await asyncio.sleep(5)
            await msg.delete()
            return
        
        if bal[0] <= 0:
            embed=discord.Embed(title="餘額不足", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 銀行系統 ⚠️")
            embed.set_thumbnail(url="https://c.tenor.com/o6_Suc3YJq4AAAAC/no-money-please.gif")
            msg = await ctx.send(embed=embed)
            await ctx.message.delete()
            await asyncio.sleep(5)
            await msg.delete()
            return 
        if amount > bal[0]:
            embed=discord.Embed(title="餘額不足", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 銀行系統 ⚠️")
            embed.set_thumbnail(url="https://c.tenor.com/o6_Suc3YJq4AAAAC/no-money-please.gif")
            msg = await ctx.send(embed=embed)
            await ctx.message.delete()
            await asyncio.sleep(5)
            await msg.delete()
            return
        if amount < 0:
            embed=discord.Embed(title="請輸入 `正值` ", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 銀行系統 ⚠️")
            embed.set_thumbnail(url="https://c.tenor.com/o6_Suc3YJq4AAAAC/no-money-please.gif")
            msg = await ctx.send(embed=embed)
            await ctx.message.delete()
            await asyncio.sleep(5)
            await msg.delete()
            return
        # 做出限制
        if amount > 201 or mang > 10 :
            embed=discord.Embed(title="請輸入正整數的倍率，並且介於 0 ~ 10 之間", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 錯誤 ⚠️")
            embed.set_thumbnail(url="https://play-lh.googleusercontent.com/i-0HlK6I-K5ZVI28HFa4iXz0T22Mg2WjQ4gMsEYvqmSNdifp2NE41ZiaUCavmbIimQ")
            msg = await ctx.send(embed=embed)
            await ctx.message.delete()
            await asyncio.sleep(5)
            await msg.delete() 
            return

        final = []
        for i in range(3):
            a = random.choice([ "X", "O", "Q" ])
            final.append(a)
        ans = mang * amount
        pos = mang * amount * -1
        # win
        if final[0] == final[1] == final[2]:
            msg0 = await ctx.send("想贏嗎??")
            await asyncio.sleep(3)
            await msg0.delete()
            await update_bank(ctx.author, ans)
            em_1=discord.Embed(title=f"{final}", color=0xff0000, timestamp = datetime.datetime.now())
            em_1.set_author(name="🎰 拉霸機 🎰")
            await ctx.message.delete()
            await ctx.send(embed=em_1)

            em_2=discord.Embed(title=f"你贏了 `{ans}` 塊錢", color=0xff0000, timestamp = datetime.datetime.now())
            em_2.set_author(name="🎰 拉霸機 🎰")
            await ctx.send(ctx.author.mention,embed=em_2)
        # lose
        else:
            msg0 = await ctx.send("想贏嗎??")
            await asyncio.sleep(3)
            await msg0.delete()
            await update_bank(ctx.author, pos)
            em_1=discord.Embed(title=f"{final}", color=0xff0000, timestamp = datetime.datetime.now())
            em_1.set_author(name="🎰 拉霸機 🎰")
            await ctx.message.delete()
            await ctx.send(embed=em_1)
            em_2=discord.Embed(title=f"你輸了 `{pos}` 塊錢", color=0xff0000, timestamp = datetime.datetime.now())
            em_2.set_author(name="🎰 拉霸機 🎰")
            await ctx.send(ctx.author.mention,embed=em_2)
            await update_bank(ctx.author, pos)

    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self, ctx):
        pass
        
        await open_account(ctx.author)

        users = await get_bank_data()
        user = ctx.author

        earnings = random.randrange(101)

        embed=discord.Embed(title=f"✅ ‖ 已簽到\n 獲得 {earnings} 塊錢", color=0xff0000, timestamp = datetime.datetime.now())
        embed.set_author(name="⚠️ 銀行系統 ⚠️")
        embed.set_thumbnail(url="https://mavsocial-wpengine.netdna-ssl.com/wp-content/uploads/2017/10/Showering-in-money-GIF.gif")
        await ctx.send(embed=embed)

        users[str(user.id)]["wallet"] += earnings

        with open("main_bank.json", mode = "w") as f:
            json.dump(users, f)

    @commands.command()
    async def withdraw(self, ctx, amount = None):
        pass
        await open_account(ctx.author)
        if amount == None:
            embed=discord.Embed(title="請輸入\n`提款 金額(正整數)`", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 銀行系統 ⚠️")
            embed.set_thumbnail(url="https://1.bp.blogspot.com/-K61Esafa0YU/XdjEr0_IckI/AAAAAAAOt3g/EYVmGyvW5TweaExeeSVr3rHpIjyDoTrXgCLcBGAsYHQ/s1600/AW4048160_16.gif")
            await ctx.send(embed=embed)
            return

        bal = await update_bank(ctx.author)
        amount = int(amount)
        if amount > bal[1]:
            embed=discord.Embed(title="存款不足", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 銀行系統 ⚠️")
            embed.set_thumbnail(url="https://1.bp.blogspot.com/-K61Esafa0YU/XdjEr0_IckI/AAAAAAAOt3g/EYVmGyvW5TweaExeeSVr3rHpIjyDoTrXgCLcBGAsYHQ/s1600/AW4048160_16.gif")
            await ctx.send(embed=embed)
            return 
        if amount > 10000:
            embed=discord.Embed(title="一次能 提款 的金額為`10000`元", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 銀行系統 ⚠️")
            embed.set_thumbnail(url="https://1.bp.blogspot.com/-K61Esafa0YU/XdjEr0_IckI/AAAAAAAOt3g/EYVmGyvW5TweaExeeSVr3rHpIjyDoTrXgCLcBGAsYHQ/s1600/AW4048160_16.gif")
            await ctx.send(embed=embed)
            return
        if amount < 0:
            embed=discord.Embed(title="請輸入\n`提款 金額(正整數)`", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 銀行系統 ⚠️")
            embed.set_thumbnail(url="https://1.bp.blogspot.com/-K61Esafa0YU/XdjEr0_IckI/AAAAAAAOt3g/EYVmGyvW5TweaExeeSVr3rHpIjyDoTrXgCLcBGAsYHQ/s1600/AW4048160_16.gif")
            await ctx.send(embed=embed)
            return

        await update_bank(ctx.author, amount)
        await update_bank(ctx.author, -1 * amount, "bank")
        embed=discord.Embed(title=f"你提款了 { amount } 塊錢!!!", color=0xff0000, timestamp = datetime.datetime.now())
        embed.set_author(name="⚠️ 銀行系統 ⚠️")
        embed.set_thumbnail(url="https://media0.giphy.com/media/3oz8xZGfHArTvh99YI/giphy.gif")
        await ctx.send(embed=embed)

    @commands.command()
    async def deposit(self, ctx, amount = None):
        pass
        await open_account(ctx.author)
        if amount == None:
            embed=discord.Embed(title="請輸入`存款 金額(正整數)`", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 銀行系統 ⚠️")
            embed.set_thumbnail(url="https://1.bp.blogspot.com/-K61Esafa0YU/XdjEr0_IckI/AAAAAAAOt3g/EYVmGyvW5TweaExeeSVr3rHpIjyDoTrXgCLcBGAsYHQ/s1600/AW4048160_16.gif")
            await ctx.send(embed=embed)
            return
        bal = await update_bank(ctx.author)
        amount = int(amount)
        if amount > bal[0]:
            embed=discord.Embed(title="錢包餘額不足", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 銀行系統 ⚠️")
            embed.set_thumbnail(url="https://1.bp.blogspot.com/-K61Esafa0YU/XdjEr0_IckI/AAAAAAAOt3g/EYVmGyvW5TweaExeeSVr3rHpIjyDoTrXgCLcBGAsYHQ/s1600/AW4048160_16.gif")
            await ctx.send(embed=embed)
            return 
        if amount > 10000:
            embed=discord.Embed(title="一次能 存款 的金額為`10000`元", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 銀行系統 ⚠️")
            embed.set_thumbnail(url="https://1.bp.blogspot.com/-K61Esafa0YU/XdjEr0_IckI/AAAAAAAOt3g/EYVmGyvW5TweaExeeSVr3rHpIjyDoTrXgCLcBGAsYHQ/s1600/AW4048160_16.gif")
            await ctx.send(embed=embed)
            return
        if amount< 0:
            embed=discord.Embed(title="請重新輸入`存款 金額(正整數)`", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 銀行系統 ⚠️")
            embed.set_thumbnail(url="https://1.bp.blogspot.com/-K61Esafa0YU/XdjEr0_IckI/AAAAAAAOt3g/EYVmGyvW5TweaExeeSVr3rHpIjyDoTrXgCLcBGAsYHQ/s1600/AW4048160_16.gif")
            await ctx.send(embed=embed)
            return
            
        await update_bank(ctx.author, -1 * amount)
        await update_bank(ctx.author, amount, "bank")
        embed=discord.Embed(title=f"你存了 { amount } 塊錢!!!", color=0xff0000, timestamp = datetime.datetime.now())
        embed.set_author(name="⚠️ 銀行系統 ⚠️")
        embed.set_thumbnail(url="https://media0.giphy.com/media/WqFyl0uk1n54zHYxIK/giphy.gif")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def send(self, ctx, member:discord.Member, amount = None):
        await open_account(ctx.author)
        await open_account(member)
        if amount == None:
            embed=discord.Embed(title="請輸入`轉帳 金額(正整數)`", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 銀行系統 ⚠️")
            embed.set_thumbnail(url="https://1.bp.blogspot.com/-K61Esafa0YU/XdjEr0_IckI/AAAAAAAOt3g/EYVmGyvW5TweaExeeSVr3rHpIjyDoTrXgCLcBGAsYHQ/s1600/AW4048160_16.gif")
            await ctx.send(embed=embed)
            return 
        bal = await update_bank(ctx.author)
        
        if amount == "all":
            amount = bal[0]
        amount = int(amount)
        if amount > bal[1]:
            embed=discord.Embed(title="存款不足", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 銀行系統 ⚠️")
            embed.set_thumbnail(url="https://1.bp.blogspot.com/-K61Esafa0YU/XdjEr0_IckI/AAAAAAAOt3g/EYVmGyvW5TweaExeeSVr3rHpIjyDoTrXgCLcBGAsYHQ/s1600/AW4048160_16.gif")
            await ctx.send(embed=embed)
            return 
        if amount< 0:
            embed=discord.Embed(title="請輸入`轉帳 金額(正整數)`", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="⚠️ 銀行系統 ⚠️")
            embed.set_thumbnail(url="https://1.bp.blogspot.com/-K61Esafa0YU/XdjEr0_IckI/AAAAAAAOt3g/EYVmGyvW5TweaExeeSVr3rHpIjyDoTrXgCLcBGAsYHQ/s1600/AW4048160_16.gif")
            await ctx.send(embed=embed)
            return
        await update_bank(ctx.author, -1 * amount, "bank")
        await update_bank(member, amount, "bank")
        member = str(member)
        member = member.split("#")[0]
        embed=discord.Embed(title=f"你給了{ member } `{ amount }` 塊錢!!!", color=0xff0000, timestamp = datetime.datetime.now())
        embed.set_author(name="⚠️ 銀行系統 ⚠️")
        embed.set_thumbnail(url="https://c.tenor.com/A_d18TlTmycAAAAC/counting-money-money.gif")
        await ctx.send(embed=embed)
    
#    @commands.command()
#    async def market(self, ctx):
#        pass
#        em = discord.Embed(title = "market", color = 0x6345)
#        em.set_thumbnail(url = "https://www.formula-ai.com/wp-content/uploads/2020/09/python_or_java_meme.jpg")
    
#        for item in shop:
#            name = item["name"]
#            price = item["price"]
#            em.add_field(name = name, value = f"${price}")
#        await ctx.send(embed = em)

#    @commands.command()
#    async def bag(self, ctx):
#        await open_account(ctx.author)
#        user = ctx.author    
#        users = await get_bank_data()
#        try:
#            bag = users[str(user.id)]["bag"]
#        except:
#            bag = []
#        em = discord.Embed(title = "Bag", color = 0xFF5733)
#        em.set_thumbnail(url = user.avatar_url)
#        for item in bag:
#            name = item["item"]
#            amount = item["amount"]
    
#            em.add_field(name = name, value = amount)
#        await ctx.send(embed = em)

#    @commands.command()
#    async def buy(self, ctx, item, amount = 1):
#        pass
#        await open_account(ctx.author)
    
#        res = await buy_this(ctx.author, item, amount)
    
#        if res[0] == False :
#            if res[1] == 1 :
#                await ctx.send("沒有這個東西喔")
#                return
#            if res[1] == 2 :
#                await ctx.send(f"你的錢包裡沒有足夠的錢去買 {item}")
#                return
        
#        await ctx.send(f"你買到了 {amount} x {item}")

def setup(bot):
    bot.add_cog(Money(bot))
