# Importing the Libraries module
import json
import asyncio
from os import F_OK, name
from typing import ItemsView
import tweepy
from amazon.paapi import AmazonAPI
from datetime import datetime
from itertools import zip_longest

#! TODO

data_list = []

items_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)
data_list = []

# Loading the Data from the File
#KEY = data['Amazon_Key']
#SECRET = data['Amazon_Secret']

KEY = 'AKIAIULDEDVFO5IDUXEQ'#data['Twitter_CONSUMER_KEY']
SECRET = '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'#data['Twitter_CONSUMER_SECRET']
TAG_UK = 'ukps5notify-21'#data['Amazon_Tag_UK']
amazon = AmazonAPI(KEY, SECRET, TAG_UK, 'UK')

products = amazon.get_products(['https://www.amazon.com/Gigabyte-AORUS-GeForce-MASTER-Graphics/dp/B095X622XV?crid=2Z1OV7I7NT4NU&dchild=1&keywords=3080+ti&qid=1622914861&s=computers&sprefix=3080%2Ccomputers%2C159&sr=1-1&linkCode=ll1&tag=ukps5notify-21&linkId=486c35bc3b5429502d1affb8cc9bb25f&language=en_GB&ref_=as_li_ss_tl','https://www.amazon.com/dp/B096KVBBHQ?&linkCode=ll1&tag=ukps5notify-21&linkId=c84ff8494911dfc6c68e599fb01ddfa7&language=en_GB&ref_=as_li_ss_tl'])
for x in products:
    print(x.url)



#TAG_DE = data['Amazon_Tag_DE']
#TAG_ES = data['Amazon_Tag_ES']
#TAG_FR = data['Amazon_Tag_FR']
#TAG_IT = data['Amazon_Tag_IT']


#ACCESS_KEY = data['Twitter_ACCESS_KEY']
#ACCESS_SECRET = data['Twitter_ACCESS_SECRET']
stock_messages = ['In stock.','Usually dispatched within 2 to 3 days.','Usually dispatched within 2 to 4 days.','Usually dispatched within 3 to 4 days.','Usually dispatched within 6 to 10 days.','Temporarily out of stock. We are working hard to be back in stock. Place your order and we’ll email you when we have an estimated delivery date.','In stock on July 14, 2021. Order it now.','In stock on July 1, 2021.']


async def UK_stock_searcher():
    await asyncio.sleep(20)
    while True:
        with open('UK_Links.json') as f:
            items_list = json.load(f)

        def grouper(n, iterable, fillvalue=None):
            "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
            args = [iter(iterable)] * n
            return zip_longest(fillvalue=fillvalue, *args)

        for x1,x2,x3,x4,x5,x6,x7,x8,x9,x10 in grouper(10, list(items_list)):
            data_list = []
            if not x1 == None:
                data_list.append(x1)
            if not x2 == None:
                data_list.append(x2)
            if not x3 == None:                
                data_list.append(x3)
            if not x4 == None:
                data_list.append(x4)
            if not x5 == None:
                data_list.append(x5)
            if not x6 == None:
                data_list.append(x6)
            if not x7 == None:
                data_list.append(x7)
            if not x8 == None:
                data_list.append(x8)
            if not x9 == None:
                data_list.append(x9)
            if not x10 == None:
                data_list.append(x10)
            
            amazon = AmazonAPI(KEY, SECRET, TAG_UK, 'UK')
            products = amazon.get_products(data_list)
            for x,raw in zip(products,data_list):
                with open('Cache.json') as f:
                    cache = json.load(f)
                try:
                    seller_name = x.raw_info._offers._listings[0].merchant_info.name
                except:
                    continue
                
                hash_tags = items_list[raw]['Hash Tags']
                max_price = items_list[raw]['Max Price']

                stock = x.prices.availability.message
                title = x.title
                truncated_title = title[:55]
                price = x.prices.price.value
                format_ = '%H:%M:%S'
                date_now = datetime.strftime(datetime.now(), format_)
                link = raw
                print(title)
                print(link)
                print('------------------------------')
                print('------------------------------')
                if stock is not None:
                    if price > max_price and not 'amazon' in seller_name.lower():
                        continue

                    if not raw in cache['Sent_Tweets_UK']:
                        #auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
                        #auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
                        #api = tweepy.API(auth)

                        print(link,title)
                        if 'amazon' in seller_name.lower():
                            msg = f'Amazon​.co.uk: {truncated_title}\n✅Sold by Amazon\n🔗{link}\n💸 £{price} as of 🕒 {date_now}\n{hash_tags}'
                        else:
                            msg = f'Amazon​.co.uk: {truncated_title}\n🔗{link}\n💸 £{price} as of 🕒 {date_now}\n{hash_tags}'

                        try:

                            #api.update_status(status = msg)
                            print(f'TWEET UPDATED FOR\n{msg}')
                            cache['Sent_Tweets_UK'].append(raw)
                            with open('Cache.json','w') as f:
                                json.dump(cache,f,indent = 3)   
                            
                            if not 'UK_STOCK_DETAILS' in cache:
                                cache['UK_STOCK_DETAILS'] = {}
                            
                            cache['UK_STOCK_DETAILS'][title] = price

                            with open('Cache.json','w') as f:
                                json.dump(cache,f,indent = 3)  
                                                    
                        except Exception as e:
                            print(e)
                            continue
                    
                    elif 'UK_STOCK_DETAILS' in cache:
                        if title in cache['UK_STOCK_DETAILS']:
                            if cache['UK_STOCK_DETAILS'][title] != price and cache['UK_STOCK_DETAILS'][title] < price:
                                cache['UK_STOCK_DETAILS'].remove(title)

                                with open('Cache.json','w') as f:
                                    json.dump(cache,f,indent = 3)                              

                            if raw in cache['Sent_Tweets_UK']:
                                cache['Sent_Tweets_UK'].remove(raw)
                                with open('Cache.json','w') as f:
                                    json.dump(cache,f,indent = 3)

                else:
                    if raw in cache['Sent_Tweets_UK']:
                        cache['Sent_Tweets_UK'].remove(raw)
                        with open('Cache.json','w') as f:
                            json.dump(cache,f,indent = 3)

                await asyncio.sleep(5)
        
        await asyncio.sleep(120)

loop = asyncio.get_event_loop()
loop.run_until_complete(UK_stock_searcher())
loop.close()