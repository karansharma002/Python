import requests
import time
import asyncio
import json


import pyshopee
client = pyshopee.Client(366518508, 2001612, '3f1c72222db556ac82a3ae0e3220f50cb30d0ab9a9ba98f643bbbfc8f578f30a' )
COUNTY_CODE = '+'
import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix= '=')

@bot.event
async def on_ready():
    print('--------- STARTED SHOPEE SERVER -------------')

@bot.command()
async def purchase(ctx):
    global COUNTY_CODE
    KEY = 'b395149d4b5bb7cb969f5ce27d536Ae3'
    def check(reaction, user):
        return user == ctx.author and reaction.channel == ctx.channel

    embed = discord.Embed(description = f'{ctx.author.mention}\nHi there, please create ticket with react 📩',color = discord.Color.blue())
    msg = await ctx.send(embed = embed)
    def check(reaction, user):
        return user == ctx.author and reaction.emoji == '📩'

    await msg.add_reaction('📩')
    reaction,user = await bot.wait_for('reaction_add',check = check,timeout = 60)
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.guild.me: discord.PermissionOverwrite(read_messages=True,send_messages = True)
    }
    channel = await ctx.guild.create_text_channel(f'{ctx.author.name}-transcript', overwrites=overwrites)
    while True:
        embed = discord.Embed(description = f'Hi, {ctx.author.mention}, how can I help you today? ^_^\n\n📱 Claim Number\n💰 Check Balance\n🔒 Close',color = discord.Color.blue())
        await msg.delete()
        msg = await channel.send(embed = embed)
        for x in ('📱','💰','🔒'):
            await msg.add_reaction(x)

        def check(reaction, user):
            return user == ctx.author and reaction.emoji in ('📱','💰','🔒')
        
        reaction,user = await bot.wait_for('reaction_add',check = check,timeout = 60)
        try:
            if reaction.emoji == '📱':
                with open('Data.json') as f:
                    data = json.load(f)
                
                if not str(ctx.author.id) in data:
                    embed = discord.Embed(description = 'INSUFFICIENT BALANCE',color = discord.Color.red())
                    await msg.edit(embed = embed)
                    return

                elif not data[str(ctx.author.id)] >= 0.85:
                    embed = discord.Embed(description = 'INSUFFICIENT BALANCE',color = discord.Color.red())
                    await msg.edit(embed = embed)
                    return


                embed = discord.Embed(description = f'May I  know which country number should you take?\n\n🇮🇩 Indonesia\n🇻🇳 Vietnam\n🔒 Close',color = discord.Color.blue())
                await msg.delete()
                msg = await channel.send(embed = embed)
                for x in ('🇮🇩','🇻🇳','🔒'):
                    await msg.add_reaction(x)

                def check(reaction, user):
                    return user == ctx.author and reaction.emoji in ('🇮🇩','🇻🇳','🔒')
                reaction,user = await bot.wait_for('reaction_add',check = check,timeout = 60)

                if reaction.emoji == '🇮🇩':
                    COUNTY = 6
                elif reaction.emoji == '🇻🇳':
                    COUNTY = 10
                else:
                    embed = discord.Embed(description = 'TICKET CLOSED',color = discord.Color.red())
                    await channel.delete()
                    return

                #STATUS CODES
                CANCEL = -1
                CONFIRM = 1
                RESEND = 3
                END = 6

                while True:
                    url = f'https://sms-activate.ru/stubs/handler_api.php?api_key={KEY}&action=getNumber&service=nz&ref=$ref&country={COUNTY}&freePrice=false&maxPrice=1000'
                    r = requests.get(url)
                    content = r.text.split(':')
                    try:
                        STATUS = content[0]
                        ID = content[1]
                        NUMBER = content[2]

                    except Exception as e:
                        continue
                    
                    embed = discord.Embed(title = f"{COUNTY_CODE}{NUMBER}", description = 'Please click Waiting Code when you’re waiting for it.\n\nRemark:\n\nIf you do not want to use this number, click Reset. If not, we will deduct your balance after 20 mins.\n⏳ Waiting Code\n❌ Reset',color = discord.Color.blue())
                    await msg.delete()
                    msg = await channel.send(embed = embed)
                    for x in ('⏳','❌'):
                        await msg.add_reaction(x)

                    def check(reaction, user):
                        return user == ctx.author and reaction.emoji in ('⏳','❌')

                    reaction,user = await bot.wait_for('reaction_add',check = check,timeout = 60)
                    if reaction.emoji == '❌':
                        url = f'https://sms-activate.ru/stubs/handler_api.php?api_key={KEY}&action=setStatus&status=-1&id={ID}'
                        r = requests.get(url)
                        break

                    elif reaction.emoji == '⏳':
                        url = f'https://sms-activate.ru/stubs/handler_api.php?api_key={KEY}&action=setStatus&status=1&id={ID}'
                        requests.get(url)
                        while True:
                            embed = discord.Embed(description = 'Please wait for a moment ya. During seeking for your code.\n\nIt may take up to 30sec to 1 minute.',color = discord.Color.blue())
                            await msg.delete()
                            msg = await channel.send(embed = embed)
                            import datetime
                            endTime = datetime.datetime.now() + datetime.timedelta(minutes=1)
                            while True:
                                url = f'https://sms-activate.ru/stubs/handler_api.php?api_key={KEY}&action=getStatus&id={ID}' #! FOR STATUS
                                r = requests.get(url)
                                print(r.text)
                                if r.text == 'STATUS_WAIT_CODE' or r.text == 'STATUS_CANCEL':
                                    status = 'STATUS_WAIT_CODE'
                                else:
                                    content = r.text.split(':')
                                    print(content)
                                    status = content[0]
                                    code = content[1]

                                if status == 'STATUS_OK':
                                    embed = discord.Embed(title = f'Woahh! I found your code: [{code}]',description = f'Remember key in Voucher Code before page order ya.\n\nFor the voucher, you may refer to #VoucherChannel',color = discord.Color.blue())
                                    await msg.delete()
                                    msg = await channel.send(embed = embed)
                                    await msg.add_reaction('🔒')
                                    with open('Data.json') as f:
                                        data = json.load(f)
                                    
                                    author = str(ctx.author.id)
                                    p_add = data[author]
                                    p_add = round(p_add - 0.85 if COUNTY == 6 else 1,2)
                                    data[author] -= p_add
                                    
                                    with open('Data.json','w') as f:
                                        json.dump(data,f,indent = 3)

                                    def check(reaction, user):
                                        return user == ctx.author and reaction.emoji in ('🔒')
                                    reaction,user = await bot.wait_for('reaction_add',check = check,timeout = 60)
                                                            
                                    if reaction.emoji == '🔒':
                                        embed = discord.Embed(description = 'TICKET CLOSED',color = discord.Color.red())
                                        await channel.delete()
                                        return

                                    url = f'https://sms-activate.ru/stubs/handler_api.php?api_key={KEY}&action=setStatus&status=6&id={ID}'
                                    r = requests.get(url)

                                if datetime.datetime.now() >= endTime:
                                    cont = 'Uh-Oh~ I did’t get your code. Can you press resend for 1 time?\n\nOr click Reset get another new number.\n\nThanks ^-^ Still no code? Please refer to #Help-Channel'
                                    embed = discord.Embed(description = cont,color = discord.Color.blue())
                                    await msg.delete()
                                    msg = await channel.send(embed = embed)
                                    await msg.add_reaction('⏳')
                                    await msg.add_reaction('❌')
                                    def check(reaction, user):
                                        return user == ctx.author and reaction.emoji in ('⏳','❌')

                                    reaction,user = await bot.wait_for('reaction_add',check = check,timeout = 60)
                                    if reaction.emoji == '❌':
                                        break
                                    else:
                                        embed = discord.Embed(description = 'Please wait for a moment ya. During seeking for your code.\n\nIt may take up to 30sec to 1 minute.',color = discord.Color.blue())
                                        await msg.delete()
                                        msg = await channel.send(embed = embed)
                                        

                                await asyncio.sleep(1)
                
            elif reaction.emoji == '🔒':
                embed = discord.Embed(description = 'TICKET CLOSED',color = discord.Color.red())
                await channel.delete()
                return

            elif reaction.emoji == '💰':
                with open('Data.json') as f:
                    data = json.load(f)
                
                author = str(ctx.author.id)
                if not author in data:
                    bal = 0
                else:
                    bal = data[author]
                
                embed = discord.Embed(description = f'Hi [{ctx.author.mention}], you have current [{bal} Points].\n\nMay I know what can I assist you? ^-^\
                    \n\n📱 Claim Number\n👛 Redeem Balance\n🔒 Close',color = discord.Color.blue())
                
                await msg.delete()
                msg = await channel.send(embed = embed)
                for x in ('📱','👛','🔒'):
                    await msg.add_reaction(x)

                def check(reaction, user):
                    return user == ctx.author and reaction.emoji in ('📱','👛','🔒')

                reaction,user = await bot.wait_for('reaction_add',check = check,timeout = 60)
                if reaction.emoji == '🔒':
                    embed = discord.Embed(description = 'TICKET CLOSED',color = discord.Color.red())
                    await channel.delete()
                    return

                elif reaction.emoji == '📱':
                    with open('Data.json') as f:
                        data = json.load(f)
                    
                    if not str(ctx.author.id) in data:
                        embed = discord.Embed(description = 'INSUFFICIENT BALANCE',color = discord.Color.red())
                        await msg.edit(embed = embed)
                        return

                    elif not data[str(ctx.author.id)] >= 0.85:
                        embed = discord.Embed(description = 'INSUFFICIENT BALANCE',color = discord.Color.red())
                        await msg.edit(embed = embed)
                        return

                    embed = discord.Embed(description = f'May I  know which country number should you take?\n\n🇮🇩 Indonesia\n🇻🇳 Vietnam\n🔒 Close',color = discord.Color.blue())
                    await msg.delete()
                    msg = await channel.send(embed = embed)
                    for x in ('🇮🇩','🇻🇳','🔒'):
                        await msg.add_reaction(x)

                    def check(reaction, user):
                        return user == ctx.author and reaction.emoji in ('🇮🇩','🇻🇳','🔒')
                    reaction,user = await bot.wait_for('reaction_add',check = check,timeout = 60)

                    if reaction.emoji == '🇮🇩':
                        COUNTY = 6
                    elif reaction.emoji == '🇻🇳':
                        COUNTY = 10
                    else:
                        await channel.delete()
                        return

                    #STATUS CODES
                    CANCEL = -1
                    CONFIRM = 1
                    RESEND = 3
                    END = 6

                    while True:
                        url = f'https://sms-activate.ru/stubs/handler_api.php?api_key={KEY}&action=getNumber&service=nz&ref=$ref&country={COUNTY}&freePrice=false&maxPrice=1000'
                        r = requests.get(url)
                        print(r.text)
                        content = r.text.split(':')
                        try:
                            STATUS = content[0]
                            ID = content[1]
                            NUMBER = content[2]

                        except Exception as e:
                            continue
                        
                        embed = discord.Embed(title = NUMBER, description = 'Please click Waiting Code when you’re waiting for it.\n\nRemark:\n\nIf you do not want to use this number, click Reset. If not, we will deduct your balance after 20 mins.\n⏳ Waiting Code\n❌ Reset',color = discord.Color.blue())
                        await msg.delete()
                        msg = await channel.send(embed = embed)
                        for x in ('⏳','❌'):
                            await msg.add_reaction(x)

                        def check(reaction, user):
                            return user == ctx.author and reaction.emoji in ('⏳','❌')
                        reaction,user = await bot.wait_for('reaction_add',check = check,timeout = 60)
                        if reaction.emoji == '❌':
                            break
                        elif reaction.emoji == '⏳':

                            url = f'https://sms-activate.ru/stubs/handler_api.php?api_key={KEY}&action=setStatus&status=1&id={ID}'
                            requests.get(url)

                            embed = discord.Embed(description = 'Please wait for a moment ya. During seeking for your code.\n\nIt may take up to 30sec to 1 minute.',color = discord.Color.blue())
                            await msg.delete()
                            msg = await channel.send(embed = embed)
                            import datetime
                            while True:
                                endTime = datetime.datetime.now() + datetime.timedelta(minutes=1)
                                while True:
                                    url = f'https://sms-activate.ru/stubs/handler_api.php?api_key={KEY}&action=getStatus&id={ID}' #! FOR STATUS
                                    r = requests.get(url)
                                    if r.text == 'STATUS_WAIT_CODE' or r.text == 'STATUS_CANCEL':
                                        status = 'STATUS_WAIT_CODE'
                                    else:
                                        content = r.text.split(':')
                                        print(content)
                                        status = content[0]
                                        code = content[1]
                
                                    if status == 'STATUS_OK':
                                        embed = discord.Embed(description = f'Woahh! I found your code: [{code}]\n\nRemember key in Voucher Code before page order ya.\n\nFor the voucher, you may refer to #VoucherChannel',color = discord.Color.blue())
                                        await msg.delete()
                                        msg = await channel.send(embed = embed)
                                        await msg.add_reaction('🔒')
                                        with open('Data.json') as f:
                                            data = json.load(f)
                                        
                                        author = str(ctx.author.id)
                                        p_add = data[author]
                                        p_add = round(p_add - 0.85 if COUNTY == 6 else 1,2)
                                        data[author] -= p_add
                                            
                                        with open('Data.json','w') as f:
                                            json.dump(data,f,indent = 3)

                                        def check(reaction, user):
                                            return user == ctx.author and reaction.emoji in ('🔒')
                                        reaction,user = await bot.wait_for('reaction_add',check = check,timeout = 60)
                                                                
                                        if reaction.emoji == '🔒':
                                            await channel.delete()
                                            return

                                        url = f'https://sms-activate.ru/stubs/handler_api.php?api_key={KEY}&action=setStatus&status=6&id={ID}'
                                        r = requests.get(url)

                                    if datetime.datetime.now() >= endTime:
                                        cont = 'Uh-Oh~ I did’t get your code. Can you press resend for 1 time?\n\nOr click Reset get another new number.\n\nThanks ^-^ Still no code? Please refer to #Help-Channel'
                                        embed = discord.Embed(description = cont,color = discord.Color.blue())
                                        await msg.delete()
                                        msg = await channel.send(embed = embed)
                                        await msg.add_reaction('⏳')
                                        await msg.add_reaction('❌')
                                        def check(reaction, user):
                                            return user == ctx.author and reaction.emoji in ('⏳','❌')

                                        reaction,user = await bot.wait_for('reaction_add',check = check,timeout = 60)
                                        if reaction.emoji == '❌':
                                            while True:
                                                url = f'https://sms-activate.ru/stubs/handler_api.php?api_key={KEY}&action=setStatus&status=-1&id={ID}'
                                                r = requests.get(url)
                                                url = f'https://sms-activate.ru/stubs/handler_api.php?api_key={KEY}&action=getNumber&service=nz&ref=$ref&country={COUNTY}&freePrice=false&maxPrice=1000'
                                                r = requests.get(url)
                                                content = r.text.split(':')
                                                try:
                                                    STATUS = content[0]
                                                    ID = content[1]
                                                    NUMBER = content[2]

                                                except Exception as e:
                                                    await channel.send('ERROR', e)
                                                
                                                embed = discord.Embed(title = f"{COUNTY_CODE}{NUMBER}", description = 'Please click Waiting Code when you’re waiting for it.\n\nRemark:\n\nIf you do not want to use this number, click Reset. If not, we will deduct your balance after 20 mins.\n⏳ Waiting Code\n❌ Reset',color = discord.Color.blue())
                                                await msg.delete()
                                                msg = await channel.send(embed = embed)
                                                for x in ('⏳','❌'):
                                                    await msg.add_reaction(x)
                                                
                                                def check(reaction, user):
                                                    return user == ctx.author and reaction.emoji in ('⏳','❌')

                                                reaction,user = await bot.wait_for('reaction_add',check = check,timeout = 60)
                                                if reaction.emoji == '⏳':
                                                    break
                                                elif reaction.emoji == '❌':
                                                    url = f'https://sms-activate.ru/stubs/handler_api.php?api_key={KEY}&action=setStatus&status=-1&id={ID}'
                                                    r = requests.get(url)
                                                    continue

                                        else:
                                            embed = discord.Embed(description = 'Please wait for a moment ya. During seeking for your code.\n\nIt may take up to 30sec to 1 minute.',color = discord.Color.blue())
                                            await msg.delete()
                                            msg = await channel.send(embed = embed)
                                    await asyncio.sleep(1)

                elif reaction.emoji == '👛':
                    while True:
                        embed = discord.Embed(color = discord.Color.green(),description = 'Please enter your Shopee Order ID below to redeem balance. ^-^\n**Enter Close To Close the Ticket**')
                        await msg.delete()
                        msg = await channel.send(embed = embed)

                        def check(m):
                            return m.author == ctx.author and m.channel == ctx.channel

                        inp = await bot.wait_for('message',check = check,timeout = 60)
                        content = inp.content
                        if content.lower() == 'close':
                            await channel.delete()
                            return

                        else:
                            with open('Cache.json') as f:
                                cache = json.load(f)
                            
                            if content in cache:
                                embed = discord.Embed(description = 'Uh-Oh~ Seems like you had enter an invalid Order ID. Please try again.\n\n✏️ Re-enter\n🔒 Close',color = discord.Color.red())
                                await msg.delete()
                                msg = await channel.send(embed = embed)
                                for x in ('✏️','🔒'):
                                    await msg.add_reaction(x)

                                def check(reaction, user):
                                    return user == ctx.author and reaction.emoji in ('✏️','🔒')

                                reaction,user = await bot.wait_for('reaction_add',check = check,timeout = 60)
                                if reaction.emoji == '🔒':
                                    await channel.delete()
                                    return

                                else:
                                    continue

                            ordersn_list = [content]
                            resp = client.order.get_order_detail(ordersn_list = ordersn_list )
                            if not resp['errors'] == []:
                                embed = discord.Embed(description = 'Uh-Oh~ Seems like you had enter an invalid Order ID. Please try again.\n\n✏️ Re-enter\n🔒 Close',color = discord.Color.red())
                                await msg.delete()
                                msg = await channel.send(embed = embed)
                                for x in ('✏️','🔒'):
                                    await msg.add_reaction(x)

                                def check(reaction, user):
                                    return user == ctx.author and reaction.emoji in ('✏️','🔒')

                                reaction,user = await bot.wait_for('reaction_add',check = check,timeout = 60)
                                if reaction.emoji == '🔒':
                                    await channel.delete()
                                    return

                                else:
                                    continue
                            
                            elif resp['orders'][0]['order_status'] == 'COMPLETED':
                                embed = discord.Embed(description = 'Uh-Oh~ Seems like you had enter an invalid Order ID. Please try again.\n\n✏️ Re-enter\n🔒 Close',color = discord.Color.red())
                                await msg.delete()
                                msg = await channel.send(embed = embed)
                                for x in ('✏️','🔒'):
                                    await msg.add_reaction(x)

                                def check(reaction, user):
                                    return user == ctx.author and reaction.emoji in ('✏️','🔒')

                                reaction,user = await bot.wait_for('reaction_add',check = check,timeout = 60)
                                if reaction.emoji == '🔒':
                                    await channel.delete()
                                    return

                                else:
                                    continue

                            else:
                                resp = resp['orders'][0]['items'][0]['variation_quantity_purchased']

                                with open('Data.json') as f:
                                    data = json.load(f)
                                
                                if not str(ctx.author.id) in data:
                                    data[str(ctx.author.id)] = int(resp)
                                else:
                                    data[str(ctx.author.id)] += int(resp)
                                
                                bal = data[str(ctx.author.id)]
                                
                                with open('Data.json','w') as f:
                                    json.dump(data,f,indent = 3)
                                
                                with open('Cache.json') as f:
                                    cache = json.load(f)
                                
                                cache[content] = 'VERIFIED'
                                with open('Cache.json','w') as f:
                                    json.dump(cache,f,indent = 3)

                                embed = discord.Embed(color = discord.Color.green(),description = f'Thanks for your order {ctx.author.mention}!\n\bYou had redeemed [{int(resp)} Points] successfully.\n\nYour new balance is {bal} Points.')
                                await msg.delete()
                                msg = await channel.send(embed = embed)
                                return

        except asyncio.TimeoutError:
            embed = discord.Embed(color = discord.Color.red(), title = 'TICKET TIMED-OUT')
            await msg.delete()
            await channel.send(embed = embed)
            return
        
        except Exception as e:
            import traceback
            traceback.print_exc()
            embed = discord.Embed(title = F'ERROR: {e}',color = discord.Color.red())
            await msg.delete()
            await channel.send(embed = embed)
            return

@commands.has_permissions(administrator = True)
@bot.command()
async def adminpredeem(ctx,user:discord.User = None,amount:float = None):
    if not user or not amount:
        await ctx.send(':information_source: Usage: =adminpredeem `<@USER ID or Mention>` `<AMOUNT TO LOAD>`')
        return
    
    with open('Data.json') as f:
        data = json.load(f)

    if not str(user.id) in data:
        data[str(user.id)] = amount
    else:
        data[str(user.id)] += amount

    with open('Data.json','w') as f:
        json.dump(data,f,indent = 3)
    
    await ctx.send(f"{ctx.author}, you had reload {amount} Points to {user.id}")

bot.run('ODc3OTUxMjg0NTYzNTU4NDgy.YR6F2Q.lLpgcWoYTai6zwFjdzD3TAPOmYc')
