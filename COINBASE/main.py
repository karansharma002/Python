import discord
from discord.ext import commands,tasks
import json
import os
from datetime import datetime
from datetime import timedelta
import requests
from bs4 import BeautifulSoup
import asyncio

bot = commands.Bot(command_prefix= '-')
#! DON'T REMOVE THIS LINE
bot.remove_command('help')

@bot.event
async def on_ready():
    print('-------------- PocketBot is alive ---------------')
    await bot.change_presence(activity=discord.Game('Monitoring Trades Across Servers'))


@tasks.loop(seconds = 30)
async def verify_data():
    pass

@bot.command()
async def bal(ctx,member:discord.User = None):
    bch = 0.0001

    if not member:
        member = ctx.author
    
    with open('Config/Data.json') as f:
        data = json.load(f)
    
    id_ = str(member.id)

    if not id_ in data:
        coin_bal = 0
    else:
        coin_bal = data[id_]['Coins']
    
    embed = discord.Embed(color = discord.Color.green(),description = f'{coin_bal} **__Pocket Coins__**\n{coin_bal * bch} **__BCH__**')
    embed.set_author(name = f"{member} | Balance",icon_url=member.avatar_url)
    await ctx.send(embed = embed)


@bot.command()
async def buy(ctx,amount:int = None):
    if not amount:
        await ctx.send(':information_source: Usage: !buy `<AMOUNT OF COINS>`')
        return
    
    bch = 0.0001
    description = '''
    **__Information__**
    *If you have not made the payment yet, please send the total amount of BCH to the address below.*\n
    **__Note:__** ``Please use: !verify (YOUR HASH ID) to confirm the Transaction``.
    '''
    embed = discord.Embed(color = discord.Color.green(),title = 'Buying Coins Help',description = description)
    embed.add_field(name = 'Amount Of Coins', value = amount,inline = False)
    embed.add_field(name = 'Total Cost (BCH)',value = amount * bch,inline = False)
    embed.add_field(name = 'Address',value = 'qrkhef7q7hvrpjmkqumcuvukenlzmp9dvgdremvjuk',inline = False)
    await ctx.send(embed = embed)


@bot.command()
async def send(ctx,member:discord.User = None,val:float = None):
    if not member:
        await ctx.send(':information_source: Usage: !send `<@user>` `<AMOUNT OF COINS>`')
        return

    with open('Config/Data.json') as f:
        data = json.load(f)
    
    id_1 = str(member.id)
    id_2 = str(ctx.author.id)
    if not id_2 in data:
        await ctx.send(":warning: You don't have enough COINS.")
        return
    
    elif data[id_2]['Coins'] < val or val < 0:
        await ctx.send(':warning: Make sure you have the enough COINS.')
        return
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        await ctx.send('Have you received your trade yet? `(Reply with Yes/No)`')
        confirmation = await bot.wait_for('message',check = check, timeout = 30)
        if confirmation.content.lower() in ('yes','y'):
            pass
        else:
            await ctx.send('Trade Cancelled')
            return
    
    except asyncio.TimeoutError:
        await ctx.send('----- Request Timedout ---')
        return
    
    if not id_1 in data:
        data[id_1] = {}
        data[id_1]['Coins'] = val
    else:
        data[id_1]['Coins'] += val

    data[id_2]['Coins'] -= val if not data[id_2]['Coins'] - val < 0 else 0
    with open('Config/Data.json', 'w') as f:
        json.dump(data, f,indent= 3)
    
    await ctx.send('Trade Successfull')

@bot.command()
async def withdraw(ctx,amount:float = None,*,address:str = None):
    if not amount or not address:
        await ctx.send(':information_source: Usage: !withdraw `<AMOUNT OF COINS TO WITHDRAW>` `<ADDRESS>` ')
        return

    try:
        id_ = str(ctx.author.id)

        with open('Config/Data.json') as f:
            data = json.load(f)
        
        if not id_ in data:
            await ctx.send(':warning: You have insufficient Balance')
            return

        if amount > data[id_]['Coins'] or amount <= 0:
            await ctx.send(':warning: You have insufficient Balance')
            return

        amount = amount
        val = (amount - 15) * 0.001

        data[id_]['Coins'] -= amount if not data[id_]['Coins'] - amount < 0 else 0
        msg = f'{ctx.author.mention} Your request for withdrawing f{amount} of coins has been received.'
        embed = discord.Embed(color = discord.Color.orange(),description = msg)
        embed.add_field(name = 'Fees', value = '15 COINS',inline = False)
        embed.add_field(name = 'OUTPUT AMOUNT', value = {val},inline = False)
        embed.set_footer(text = 'It can take up to 24 hours for the payment to transfer.')
        await ctx.send(embed = embed)

        channel = await bot.fetch_channel(871242552496504883)
        embed = discord.Embed(color = discord.Color.dark_green(),title = f'{ctx.author} | Withdrawl Request')
        embed.add_field(name = 'Fees', value = '15 COINS',inline = False)
        embed.add_field(name = 'Output Amount', value = f"{val} BCH",inline = False)
        embed.add_field(name = 'Address', value = {address},inline = False)
        await channel.send(embed = embed)

    except:
        await ctx.send('Transaction FAILED Please retry.')

@bot.command()
async def remove(ctx,member:discord.User = None,val:float = None):
    if not member or not val:
        await ctx.send(':information_source: Usage: !remove `<@user>` `<AMOUNT OF COINS>`')
        return
    
    with open('Config/Data.json') as f:
        data = json.load(f)
    
    id_ = str(member.id)

    if not id_ in data:
        data[id_] = {}
        data[id_]['Coins'] = 0
    else:
        if not data[id_]['Coins'] - val < 0:
            data[id_]['Coins'] -= val
        else:
            data[id_]['Coins'] = 0
    
    with open('Config/Data.json','w') as f:
        json.dump(data,f,indent = 3)
    
    await ctx.send(f':white_check_mark: Coins has been removed for {member}')

@bot.command()
async def add(ctx,member:discord.User = None,val:float = None):
    if not member or not val:
        await ctx.send(':information_source: Usage: !add `<@user>` `<AMOUNT OF COINS>`')
        return
    
    with open('Config/Data.json') as f:
        data = json.load(f)
    
    id_ = str(member.id)
    if not id_ in data:
        data[id_] = {}
        data[id_]['Coins'] = val

    else:
        data[id_]['Coins'] += val
    
    with open('Config/Data.json','w') as f:
        json.dump(data,f,indent = 3)
    
    await ctx.send(f':white_check_mark: Coins has been added for {member}')

@bot.command()
async def help(ctx):
    msg = '''
**!bal**
**!buy** `<AMOUNT OF COINS>`
**!send** `<@user>` `<AMOUNT OF COINS>`
**!verify** `<HASH ID>`
**!withdraw** `<COINBASE EMAIL>` `<AMOUNT OF COINS TO WITHDRAW>`
    '''
    embed = discord.Embed(title = 'Trade Commands',description = msg)
    await ctx.send(embed = embed)

@bot.command()
async def verify(ctx,*,id:str = None):
    if not id:
        await ctx.send(':information_source: Usage: !verify `<HASH ID>`')
        return
    else:
        with open('Config/Transactions.json') as f:
            transactions = json.load(f)

        if id in transactions:
            await ctx.send('This transaction ID is INVALID.')
            return

        msg = await ctx.send('-- Verifying the Transaction --')

        try:
            r = requests.get(f'https://www.blockchain.com/bch/tx/{id}')
            soup = BeautifulSoup(r.content,'lxml')
            app = soup.find_all('div',class_ = 'sc-1enh6xt-0 kiseLw')

            temp_data = []
            for x in app:
                for y in x:
                    temp_data.append(y.text)

            bch_data = {temp_data[i]: temp_data[i + 1] for i in range(0, len(temp_data), 2)}
            hash_ = str(bch_data['Hash'])
            sent_at = datetime.strptime(str(bch_data['Received Time']),'%Y-%m-%d %H:%M')
            input_amount = float(bch_data['Total Input'].replace(' BCH',''))
            fees = float(bch_data['Fees'].replace(' BCH',''))
            output_amount = float(bch_data['Total Output'].replace(' BCH',''))

            if bch_data['Status'] == 'Confirmed':
                if sent_at > datetime.now() - timedelta(hours = 12):
                    with open('Config/Transactions.json') as f:
                        transactions = json.load(f)
                    
                    transactions[hash_] = 'CONFIRMED'

                    with open('Config/Transactions.json','w') as f:
                        json.dump(transactions,f,indent = 3)
                    
                    with open('Config/Data.json','r') as f:
                        data = json.load(f)
                    
                    id_ = str(ctx.author.id)
                    amount = float(output_amount)
                    val = float(amount) / 0.001
                    if not id_ in data:
                        data[id_] = {}
                        data[id_]['Coins'] = val

                    else:
                        data[id_]['Coins'] += val

                    with open('Config/Data.json', 'w') as f:
                        json.dump(data, f,indent= 3)
                    
                    embed = discord.Embed(color = discord.Color.green(),description = f'{ctx.author.mention} You have purchased {val} Pocket Coins')
                    embed.add_field(name = 'Total BCH Received Without Fees',value = input_amount,inline = False)
                    embed.add_field(name = 'Total FEES',value = fees,inline = False)
                    embed.add_field(name = 'Total BCH Received With Fees',value = output_amount,inline = False)
                    await ctx.send(embed  = embed)
                    await msg.delete()
                
                else:
                    await ctx.send(':warning: Transaction create date is higher than 12 hours. Please contact admin to approve!')
                    return
            
            else:
                await ctx.send(':warning: This transaction is not CONFIRMED Yet. Please retry after some time!')
                return

        except Exception as e:
            await msg.delete()
            await ctx.send('Failed to verify. Please retry after sometime or make sure the ID is valid.')

r = requests.get(f'https://www.blockchain.com/bch/address/qrfh5807ynvcpvm8ykatd4pmkel84e4jcv4l9z3ehm')
soup = BeautifulSoup(r.content,'lxml')
app = soup.find_all('div',class_ = 'sc-1xo2hia-0 jhFHoy')

temp_data = []
for x in app:
    for y in x:
        temp_data.append(y.text)


bch_data = {temp_data[i]: temp_data[i + 1] for i in range(0, len(temp_data), 2)}
print(bch_data)
bot.run('ODI1MjA5MzU5MDQ2MTQ4MTM2.YF6mGg.3BmBB87r-f5CUzLY6eh7CmcE6SE')

A Discord bot with the following commands and the functionalities.
   
addproduct       
channelpoints    
coins            
daily            
dailyamount      
endseason        
export           
exportform       
formchannel      
imagepoints      
leaderboard      
linkpoints       
live             
maxpoints        
orderchannel     
pinfo            
reactpoints      
remove           
removechannel    
replypoints      
setchannel       
setcurrency      
seteventcooldown 
setlogchannel    
setreactcooldown 
shop             
tagpoints        
thumbpoints      
voicemaxpoints   
voicepoints      

In-Depth Explainations over here: https://fiverr-res.cloudinary.com/image/upload/q_auto,f_pdf/v1/secured-attachments/message/attachments/3e6cbf2fbc5882c53909c93f126247a7-1627649835084/Discord_Gamification_Bot_SOW.pdf?__cld_token__=exp=1628697109~hmac=51ac9e749454c29a60614ec4e8e7989de488050aef83647ae80a9f34819ca974
