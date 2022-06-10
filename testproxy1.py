import random
from fake_useragent import UserAgent
import requests
from proxy_auth_data1 import login1, password1
import time
import json
import telebot


TOKEN = '5149999072:AAFKNlHohGWRFWY_uYTp0iNvkYyIBzWn34E'
bot = telebot.TeleBot(TOKEN)
proxy_list = [
    '181.177.87.65:9820',
    '181.177.86.123:9876',
    '181.177.85.200:9813',
    '181.177.85.157:9977',
    '181.177.85.209:9292',
    '181.177.85.2:9102',
    '181.177.86.127:9065',
    '181.177.86.148:9473',
    '181.177.85.64:9568',
    '181.177.84.164:9797',
]
y = []
h = 0

def collect_data():
    global h
    global TOKEN
    global bot
    id_channel = '@steamparser'
    gun_info = []

    h += 1
    with open('result5.json') as file:
        file_content = file.read()
        templates = json.loads(file_content)

    # with open('resul_0.json') as file2:
    #     file_content2 = file2.read()
    #     rare_float = json.loads(file_content2)

    proxies = {
        "http": f"http://{login1}:{password1}@{random.choice(proxy_list)}"
    }

    r = requests.get(
        url=f'https://api.dmarket.com/exchange/v1/market/items?side=market&orderBy=updated&orderDir=desc&title=&priceFrom=2&priceTo=1540&treeFilters=exterior%5B%5D=factory%20new,exterior%5B%5D=minimal%20wear,exterior%5B%5D=field-tested,exterior%5B%5D=well-worn,exterior%5B%5D=battle-scarred,category_1%5B%5D=not_souvenir&gameId=a8db&types=dmarket&cursor=&limit=100&currency=USD',
        headers={'user-agent': f'{UserAgent().random}'})
    # print(r.status_code)
    data = r.json()
    items = data.get('objects')

    for i in items:
        pre_stickers = []
        items_stickers = i.get('extra').get('stickers')
        if items_stickers != None:
            for j in items_stickers:
                pre_stickers.append(j.get('name'))
        else:
            pre_stickers.append("NoSticker")
        gun_info.append({
            'Name': i.get('title'),
            'Float':  i.get('extra').get('floatValue'),
            "linkid": i.get('extra').get('linkId'),
            'Stickers': pre_stickers,
            'Rungame': i.get('extra').get('inspectInGame'),
            'Price': (float(i.get('price').get('USD')) / 100),
            'SuggestedPrice': (float(i.get('suggestedPrice').get('USD')) / 100)
    })
    for i in gun_info:
        k = 0
        a = 0
        for j in i.get('Stickers'):
            if j != 'NoSticker':
                if templates.get('Sticker | ' + j) != None:
                    x = (templates.get('Sticker | ' + j))
                    if type(x) == float:
                        k += x
        round(k, 2)
        price_own = i.get('Price')
        price_sugg = i.get('SuggestedPrice')


        len_prestickers = len(i.get('Stickers'))

        if len_prestickers == 4 and price_own < price_sugg and k > 2 and price_own < 0.8:
            n = 1
            for b in range(0,3):
                if i.get('Stickers')[b] == i.get('Stickers')[b+1]:
                    n += 1
            if n == 4:
                y.append(i)
                for z in y:
                    if i == z:
                        a += 1
                if a == 1:
                    name = i.get("Name")
                    floatt = i.get("Float")
                    stickers = i.get("Stickers")
                    rungame = str(i.get("Rungame"))
                    link = f"https://dmarket.com/ingame-items/item-list/csgo-skins?userOfferId={i.get('linkid')}"
                    price = i.get("Price")
                    s_price = i.get("SuggestedPrice")
                    bot.send_message(id_channel,
                                     text=f'#4samestickers \n\n {name} \n Флоат: {floatt} \n Цена оружия: {price}$ \n средняя цена оружия: {s_price} \n \n Стикеры: {stickers} \n \n Общая цена стикеров: {k}$ \n\n Смотреть в игре: {rungame} \n\n ссылка: {link}')

        if len_prestickers == 4 and price_own < price_sugg and k > 4 and 0.8 < price_own < 4:
            n = 1
            for b in range(0,3):
                if i.get('Stickers')[b] == i.get('Stickers')[b+1]:
                    n += 1
            if n == 4:
                y.append(i)
                for z in y:
                    if i == z:
                        a += 1
                if a == 1:
                    name = i.get("Name")
                    floatt = i.get("Float")
                    stickers = i.get("Stickers")
                    rungame = str(i.get("Rungame"))
                    link = f"https://dmarket.com/ingame-items/item-list/csgo-skins?userOfferId={i.get('linkid')}"
                    price = i.get("Price")
                    s_price = i.get("SuggestedPrice")
                    bot.send_message(id_channel,
                                     text=f'#4samestickers \n\n {name} \n Флоат: {floatt} \n Цена оружия: {price}$ \n средняя цена оружия: {s_price} \n \n Стикеры: {stickers} \n \n Общая цена стикеров: {k}$ \n\n Смотреть в игре: {rungame} \n\n ссылка: {link}')

        if len_prestickers == 4 and price_own < price_sugg and k > 10:
            n = 1
            for b in range(0,3):
                if i.get('Stickers')[b] == i.get('Stickers')[b+1]:
                    n += 1
            if n == 4:
                y.append(i)
                for z in y:
                    if i == z:
                        a += 1
                if a == 1:
                    name = i.get("Name")
                    floatt = i.get("Float")
                    stickers = i.get("Stickers")
                    rungame = str(i.get("Rungame"))
                    link = f"https://dmarket.com/ingame-items/item-list/csgo-skins?userOfferId={i.get('linkid')}"
                    price = i.get("Price")
                    s_price = i.get("SuggestedPrice")
                    bot.send_message(id_channel,
                                     text=f'#4samestickers \n\n {name} \n Флоат: {floatt} \n Цена оружия: {price}$ \n средняя цена оружия: {s_price} \n \n Стикеры: {stickers} \n \n Общая цена стикеров: {k}$ \n\n Смотреть в игре: {rungame} \n\n ссылка: {link}')


        if len_prestickers == 3 and price_own < price_sugg and k > 1.5 and price_own < 0.8:
            n = 1
            for b in range(0, 2):
                if i.get('Stickers')[b] == i.get('Stickers')[b+1]:
                    n += 1
            if n == 3:
                y.append(i)
                for z in y:
                    if i == z:
                        a += 1
                if a == 1:
                    name = i.get("Name")
                    floatt = i.get("Float")
                    stickers = i.get("Stickers")
                    rungame = str(i.get("Rungame"))
                    link = f"https://dmarket.com/ingame-items/item-list/csgo-skins?userOfferId={i.get('linkid')}"
                    price = i.get("Price")
                    s_price = i.get("SuggestedPrice")
                    bot.send_message(id_channel,
                                     text=f'#3samestickers \n\n {name} \n Флоат: {floatt} \n Цена оружия: {price}$ \n средняя цена оружия: {s_price} \n \n Стикеры: {stickers} \n \n Общая цена стикеров: {k}$ \n\n Смотреть в игре: {rungame} \n\n ссылка: {link}')


        if len_prestickers == 3 and price_own < price_sugg and k > 5 and 0.8 < price_own < 4 :
            n = 1
            for b in range(0, 2):
                if i.get('Stickers')[b] == i.get('Stickers')[b+1]:
                    n += 1
            if n == 3:
                y.append(i)
                for z in y:
                    if i == z:
                        a += 1
                if a == 1:
                    name = i.get("Name")
                    floatt = i.get("Float")
                    stickers = i.get("Stickers")
                    rungame = str(i.get("Rungame"))
                    link = f"https://dmarket.com/ingame-items/item-list/csgo-skins?userOfferId={i.get('linkid')}"
                    price = i.get("Price")
                    s_price = i.get("SuggestedPrice")
                    bot.send_message(id_channel,
                                     text=f'#3samestickers \n\n {name} \n Флоат: {floatt} \n Цена оружия: {price}$ \n средняя цена оружия: {s_price} \n \n Стикеры: {stickers} \n \n Общая цена стикеров: {k}$ \n\n Смотреть в игре: {rungame} \n\n ссылка: {link}')

        if len_prestickers == 3 and price_own < price_sugg and k > 10:
            n = 1
            for b in range(0, 2):
                if i.get('Stickers')[b] == i.get('Stickers')[b+1]:
                    n += 1
            if n == 3:
                y.append(i)
                for z in y:
                    if i == z:
                        a += 1
                if a == 1:
                    name = i.get("Name")
                    floatt = i.get("Float")
                    stickers = i.get("Stickers")
                    rungame = str(i.get("Rungame"))
                    link = f"https://dmarket.com/ingame-items/item-list/csgo-skins?userOfferId={i.get('linkid')}"
                    price = i.get("Price")
                    s_price = i.get("SuggestedPrice")
                    bot.send_message(id_channel,
                                     text=f'#3samestickers \n\n {name} \n Флоат: {floatt} \n Цена оружия: {price}$ \n средняя цена оружия: {s_price} \n \n Стикеры: {stickers} \n \n Общая цена стикеров: {k}$ \n\n Смотреть в игре: {rungame} \n\n ссылка: {link}')


        if len_prestickers == 2 and price_own < price_sugg and k > 1.5 and price_own < 0.8:
            n = 1
            for b in range(0, 1):
                if i.get('Stickers')[b] == i.get('Stickers')[b+1]:
                    n += 1
            if n == 2:
                y.append(i)
                for z in y:
                    if i == z:
                        a += 1
                if a == 1:
                    name = i.get("Name")
                    floatt = i.get("Float")
                    stickers = i.get("Stickers")
                    rungame = str(i.get("Rungame"))
                    link = f"https://dmarket.com/ingame-items/item-list/csgo-skins?userOfferId={i.get('linkid')}"
                    price = i.get("Price")
                    s_price = i.get("SuggestedPrice")
                    bot.send_message(id_channel,
                                     text=f'#2samestickers \n\n {name} \n Флоат: {floatt} \n Цена оружия: {price}$ \n средняя цена оружия: {s_price} \n \n Стикеры: {stickers} \n \n Общая цена стикеров: {k}$ \n\n Смотреть в игре: {rungame} \n\n ссылка: {link}')

        if len_prestickers == 2 and price_own < price_sugg and k > 6 and 0.8 < price_own < 4:
            n = 1
            for b in range(0, 1):
                if i.get('Stickers')[b] == i.get('Stickers')[b+1]:
                    n += 1
            if n == 2:
                y.append(i)
                for z in y:
                    if i == z:
                        a += 1
                if a == 1:
                    name = i.get("Name")
                    floatt = i.get("Float")
                    stickers = i.get("Stickers")
                    rungame = str(i.get("Rungame"))
                    link = f"https://dmarket.com/ingame-items/item-list/csgo-skins?userOfferId={i.get('linkid')}"
                    price = i.get("Price")
                    s_price = i.get("SuggestedPrice")
                    bot.send_message(id_channel,
                                     text=f'#2samestickers \n\n {name} \n Флоат: {floatt} \n Цена оружия: {price}$ \n средняя цена оружия: {s_price} \n \n Стикеры: {stickers} \n \n Общая цена стикеров: {k}$ \n\n Смотреть в игре: {rungame} \n\n ссылка: {link}')

        if len_prestickers == 2 and price_own < price_sugg and k > 10:
            n = 1
            for b in range(0, 1):
                if i.get('Stickers')[b] == i.get('Stickers')[b+1]:
                    n += 1
            if n == 2:
                y.append(i)
                for z in y:
                    if i == z:
                        a += 1
                if a == 1:
                    name = i.get("Name")
                    floatt = i.get("Float")
                    stickers = i.get("Stickers")
                    rungame = str(i.get("Rungame"))
                    link = f"https://dmarket.com/ingame-items/item-list/csgo-skins?userOfferId={i.get('linkid')}"
                    price = i.get("Price")
                    s_price = i.get("SuggestedPrice")
                    bot.send_message(id_channel,
                                     text=f'#2samestickers \n\n {name} \n Флоат: {floatt} \n Цена оружия: {price}$ \n средняя цена оружия: {s_price} \n \n Стикеры: {stickers} \n \n Общая цена стикеров: {k}$ \n\n Смотреть в игре: {rungame} \n\n ссылка: {link}')


        if k >= 3 and price_own < price_sugg and  price_own < 0.11:
            y.append(i)
            for z in y:
                if i == z:
                    a += 1
            if a == 1:
                name = i.get("Name")
                floatt = i.get("Float")
                stickers = i.get("Stickers")
                rungame = str(i.get("Rungame"))
                link = f"https://dmarket.com/ingame-items/item-list/csgo-skins?userOfferId={i.get('linkid')}"
                price = i.get("Price")
                s_price = i.get("SuggestedPrice")
                bot.send_message(id_channel,
                                 text=f'{name} \n Флоат: {floatt} \n Цена оружия: {price}$ \n средняя цена оружия: {s_price} \n \n Стикеры: {stickers} \n \n Общая цена стикеров: {k}$ \n\n Смотреть в игре: {rungame} \n\n ссылка: {link}')


        if k >= 5 and price_own < price_sugg and 0.11 < price_own < 0.8:
            y.append(i)
            for z in y:
                if i == z:
                    a += 1
            if a == 1:
                name = i.get("Name")
                floatt = i.get("Float")
                stickers = i.get("Stickers")
                rungame = str(i.get("Rungame"))
                link = f"https://dmarket.com/ingame-items/item-list/csgo-skins?userOfferId={i.get('linkid')}"
                price = i.get("Price")
                s_price = i.get("SuggestedPrice")
                bot.send_message(id_channel,
                                 text=f'{name} \n Флоат: {floatt} \n Цена оружия: {price}$ \n средняя цена оружия: {s_price} \n \n Стикеры: {stickers} \n \n Общая цена стикеров: {k}$ \n\n Смотреть в игре: {rungame} \n\n ссылка: {link}')

        if k >= 10 and price_own < price_sugg and 0.8 < price_own < 4:
            y.append(i)
            for z in y:
                if i == z:
                    a += 1
            if a == 1:
                name = i.get("Name")
                floatt = i.get("Float")
                stickers = i.get("Stickers")
                rungame = str(i.get("Rungame"))
                link = f"https://dmarket.com/ingame-items/item-list/csgo-skins?userOfferId={i.get('linkid')}"
                price = i.get("Price")
                s_price = i.get("SuggestedPrice")
                bot.send_message(id_channel,
                                text=f'{name} \n Флоат: {floatt} \n Цена оружия: {price}$ \n средняя цена оружия: {s_price} \n \n Стикеры: {stickers} \n \n Общая цена стикеров: {k}$ \n\n Смотреть в игре: {rungame} \n\n ссылка: {link}')

        if k >= 15 and price_own < price_sugg:
            y.append(i)
            for z in y:
                if i == z:
                    a += 1
            if a == 1:
                name = i.get("Name")
                floatt = i.get("Float")
                stickers = i.get("Stickers")
                rungame = str(i.get("Rungame"))
                link = f"https://dmarket.com/ingame-items/item-list/csgo-skins?userOfferId={i.get('linkid')}"
                price = i.get("Price")
                s_price = i.get("SuggestedPrice")
                bot.send_message(id_channel,
                                text=f'{name} \n Флоат: {floatt} \n Цена оружия: {price}$ \n средняя цена оружия: {s_price} \n \n Стикеры: {stickers} \n \n Общая цена стикеров: {k}$ \n\n Смотреть в игре: {rungame} \n\n ссылка: {link}')


        a = 0
        floattt = i.get("Float")
        if floattt != None:
            if floattt < 0.009 and price_own < price_sugg and price_own > 5:
                y.append(i)
                for z in y:
                    if i == z:
                        a += 1
                if a == 1:
                    name = i.get("Name")
                    floatt = i.get("Float")
                    stickers = i.get("Stickers")
                    rungame = str(i.get("Rungame"))
                    link = f"https://dmarket.com/ingame-items/item-list/csgo-skins?userOfferId={i.get('linkid')}"
                    price = i.get("Price")
                    s_price = i.get("SuggestedPrice")
                    bot.send_message(id_channel,
                                     text=f'"#rarefloat" \n\n {name} \n Флоат: {floatt} \n Цена оружия: {price}$ \n средняя цена оружия: {s_price} \n \n Стикеры: {stickers} \n \n Общая цена стикеров: {k}$ \n\n Смотреть в игре: {rungame} \n\n ссылка: {link}')

    # print(f"итерация {h}")
    time.sleep(2)

def task():
    while True:
        for m in range(0, 1800):
            collect_data()
        time.sleep(400)


@bot.message_handler(commands=['start'])
def start_func(messege):
    task()

@bot.message_handler(commands=['stopp'])
def start_func(messege):
    task.quit()


bot.polling()
