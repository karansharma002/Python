import discord
from discord.ext import commands,tasks
import datetime
from dateutil import parser
from datetime import timedelta
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
import json
import asyncio
from PIL import Image, ImageOps, ImageDraw, ImageFont


import requests

bot = commands.Bot(command_prefix= '%',intents = discord.Intents.all())

@commands.is_owner()
@bot.event
async def on_ready():
    print('------- SERVER HAS STARTED ------')

@bot.command()
async def start(ctx):
    sheet_name = 'Sheet1'
    with open('Config/Settings.json') as f:
        settings = json.load(f)
    
    while True:
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        SAMPLE_SPREADSHEET_ID = '1leFdTYHkoQepImoWNRMULYd-tea-Zta7FaMJMdeykDY'
        SAMPLE_RANGE_NAME = f'{sheet_name}!A1:F'
        SERVICE_ACCOUNT_FILE = 'Sheets.json'

        creds = None
        creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)
                
        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])
        if values is None:
            await ctx.send(':warning: Database is EMPTY.')
            return

        else:
            em = ['1️⃣','2️⃣','3️⃣']
            for num,x in enumerate(values[1:]):
                if 'Number' in settings:
                    if num >= settings['Number'] + 1:
                        question = x[0]
                        answer1 = x[1]
                        answer2 = x[2]
                        answer3 = x[3]
                        right = x[4]
                        print(x[5])
                        itr = x[5]
                        itr = int(itr) - 1

                        emoji = em[itr]
                        desc = f":arrow_right: {question}\n\n:one: {answer1}\n\n:two: {answer2}\n\n:three: {answer3}\n\n*React below to choose your answer*"
                        embed = discord.Embed(description = desc,title = 'QUESTION OF THE DAY')
                        channel = await bot.fetch_channel(settings['Channel'])
                        msg = await channel.send(embed = embed)
                        await msg.add_reaction('1️⃣')
                        await msg.add_reaction('2️⃣')
                        await msg.add_reaction('3️⃣')

                        settings['Number'] = num

                        with open('Config/Settings.json','w') as f:
                            json.dump(settings,f,indent =  3)
                    
                    else:
                        continue
                        
                else:
                    question = x[0]
                    answer1 = x[1]
                    answer2 = x[2]
                    answer3 = x[3]
                    right = x[4]
                    print(x[5])
                    itr = x[5]
                    itr = int(itr) - 1

                    emoji = em[itr]
                    desc = f":arrow_right: {question}\n\n:one: {answer1}\n\n:two: {answer2}\n\n:three: {answer3}\n\n*React below to choose your answer*"
                    embed = discord.Embed(description = desc,title = 'QUESTION OF THE DAY')
                    channel = await bot.fetch_channel(settings['Channel'])
                    msg = await channel.send(embed = embed)
                    await msg.add_reaction('1️⃣')
                    await msg.add_reaction('2️⃣')
                    await msg.add_reaction('3️⃣')

                    settings['Number'] = num
                    settings['Message'] = msg.id
                    with open('Config/Settings.json','w') as f:
                        json.dump(settings,f,indent =  3)
                
                now = datetime.datetime.now()
                dt = datetime.datetime.now() + timedelta(minutes = 1)
                await asyncio.sleep((dt - now).total_seconds())
                await channel.send(right)
                total_ = settings['Total_XP']
                await channel.send(f':tada: *{total_} XP has been been sent for correct answers :rocket:*')
                
                with open('Users.json') as f:
                    usr = json.load(f)
                
                with open('Answers.json') as f:
                    answers = json.load(f)
                
                for y in answers:
                    if answers[y] == emoji:
                        if y in usr:
                            usr[y]['Points'] += 500
                        else:
                            usr[y] = {} 
                            usr[y]['Points']= 500
                
                answers = {}
                with open('Answers.json','w') as f:
                    json.dump(answers,f,indent = 3)

                with open('Users.json','w') as f:
                    json.dump(usr,f,indent=  3)
                #! ADD XP
                break
                
@bot.command()
async def setchannel(ctx,channel:discord.TextChannel = None):
    if not channel:
        await ctx.send(':information_source: Usage: !setchannel #channel')
        return
    
    with open('Config/Settings.json') as f:
        settings = json.load(f)
    
    settings['Channel'] = channel.id
    with open('Config/Settings.json','w') as f:
        json.dump(settings,f,indent = 3)
    
    await ctx.send(':white_check_mark: Channel has been Changed.')


@bot.command()
async def setpoint(ctx,point:int = None):
    if not point:
        await ctx.send(':information_source: Usage: !setpoint `POINTS`')
        return
    
    with open('Config/Settings.json') as f:
        settings = json.load(f)
    
    settings['Total_XP'] = point
    with open('Config/Settings.json','w') as f:
        json.dump(settings,f,indent = 3)
    
    await ctx.send(f':white_check_mark: Points XP has been Changed to {point}')

@bot.command()
async def leaderboard(ctx):
    with open('Users.json') as f:
        users = json.load(f)


    high_score_list1 = sorted(users, key=lambda x : users[x].get('Points', 0), reverse=True)
    msg1 = ''
    for number,user in enumerate(high_score_list1):
        author = await bot.fetch_user(int(user))
        number += 1
        xp = users[user]['Points']
        msg1 += f"**‣ {number}**. {author} ⁃\nXP: **{xp}**\n\n"
        if number == 9:
            break
        else:
            number += 1

    embed = discord.Embed(
        title= ":money_with_wings: Leaderboard",
        color= 0x05ffda,
        description= msg1
        )
    
    await ctx.send(embed = embed)

@bot.event
async def on_raw_reaction_add(payload):
    with open('Config/Settings.json') as f:
        r = json.load(f)
    
    guild = str(payload.guild_id)
    channel = await bot.fetch_channel(payload.channel_id)
    user = channel.guild.get_member(payload.user_id)
    emoji = payload.emoji
    emoji = str(emoji)
    message_id = payload.message_id
    if message_id == r['Message'] and emoji in ['1️⃣','2️⃣','3️⃣']:
        with open('Answers.json') as f:
            answers = json.load(f)
        
        if str(user.id) in answers:
            return

        answers[str(user.id)] = emoji
        with open('Answers.json','w') as f:
            json.dump(answers,f,indent= 3)


def send_image(exp,level):
    images = '12 E20 E50 E70'
    if level == 0:
        level_end = 520
    elif level== 1:
        level_end = 910
    elif level== 2:
        level_end = 1110
    elif level == 3:
        level_end = 1350
    elif level == 4:
        level_end = 1500
    elif level == 5:
        level_end = 1790
    elif level == 6:
        level_end = 1800
    elif level == 7:
        level_end = 1850
    elif level == 8:
        level_end = 1900
    elif level == 9:
        level_end = 1950
    elif level == 10:
        level_end = 2000
    else:
        level_end = 2500
    
    if exp == 0:
        return '12'

    if level_end / exp <= 3:
        return '100'

    if level_end / exp <= 6:
        return 'E70'

    elif level_end / exp <= 10:
        return 'E50'
    elif level_end / exp <= 20:
        return 'E20'
    else:
        return '12'

@bot.command()
async def rank(ctx,user:discord.Member = None):
    with open('Users.json','r') as f:
        data = json.load(f)
    
    if not user:
        author = str(ctx.author.id)
        author2 = ctx.author
    else:
        author = str(user.id)
        author2 = user

    if not author in data:
        data[author] = {}
        data[author]['Level'] = 0
        data[author]['Points'] = 0
        with open('Users.json','w') as f:
            json.dump(data,f,indent = 3)

    if not 'Level' in data[author]:
        data[author]['Level'] = 0
        level = 0
        with open('Users.json','w') as f:
            json.dump(data,f,indent = 3)

    else:
        level = data[author]['Level']

    if level == 0:
        level_end = 520
    elif level== 1:
        level_end = 910
    elif level== 2:
        level_end = 1110
    elif level == 3:
        level_end = 1350
    elif level == 4:
        level_end = 1500
    elif level == 5:
        level_end = 1790
    elif level == 6:
        level_end = 1800
    elif level == 7:
        level_end = 1850
    elif level == 8:
        level_end = 1900
    elif level == 9:
        level_end = 1950
    elif level == 10:
        level_end = 2000
    else:
        level_end = 2500

    if data[author]['Points'] >= level_end:
        data[author]['Level'] += 1
        data[author]['Points'] = 0
        with open('Users.json','w') as f:
            json.dump(data,f,indent = 3)

    
    exp = data[author]['Points']

    url = author2.avatar_url
    with requests.get(url) as r:
        img_data = r.content		
    with open('image_name.webp', 'wb') as handler:
        handler.write(img_data)

    def human_format(num):
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0

        return '%.1f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])

    im = Image.open('image_name.webp')
    region = im.resize((105, 105))
    background = Image.open('Config/r.png')
    background.paste(region,(5,4))
    image_name = send_image(exp,level)
    d2 = Image.open(f'Config/{image_name}.png')
    background.paste(d2,(115,84))
    background.save('Config/os.png')
    img = Image.open('Config/os.png')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("l_10646.ttf", 18)
    draw.text((117,60),f"{author2}",(255, 255, 255),font=font)
    font = ImageFont.truetype("l_10646.ttf", 14)
    draw.text((190,85),f"Level {level}",(255, 255, 255),font=font)
    font = ImageFont.truetype("./l_10646.ttf", 11)
    draw.text((234,2),f"{human_format(exp)}/{human_format(level_end)} XP",(169,169,169),font=font)
    img.save('Config/sample-out.png')
    await ctx.send(file=discord.File('Config/sample-out.png'))
    
bot.run('ODI1MjA5MzU5MDQ2MTQ4MTM2.YF6mGg.3BmBB87r-f5CUzLY6eh7CmcE6SE')