from pickletools import read_uint1
from posixpath import split
import requests
from bs4 import BeautifulSoup
import datetime
from datetime import timedelta
from zoneinfo import ZoneInfo


def pray_time(a, til):
    while True:
        # print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
        # print(datetime.datetime.now().month)
        current_time = datetime.datetime.now(tz=ZoneInfo("Asia/Tashkent")).strftime('%H:%M:%S')
        date = datetime.date.today()
        url = f'https://islom.uz/vaqtlar/{a}/{datetime.datetime.now().month}'
        # url = f'https://islom.uz/vaqtlar/13/6'
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'lxml')
        # print(soup)
        if soup.find_all('tr', class_='juma bugun'):
            city_href = soup.find_all('tr', class_='juma bugun')
        else:
            city_href = soup.find_all('tr', class_='p_day bugun')
            # print('yoq')
        xafta = {"kr":{
    "Душанба": 'Душанба', 'Сешанба': 'Сешанба', 'Чоршанба': 'Чоршанба', 'Пайшанба': 'Пайшанба',
                'Жума': "Жума", 'Шанба': 'Шанба', 'Якшанба': 'Якшанба'
        },

        "uz":{
            "Душанба": 'Dushanba', 'Сешанба': 'Sеshanba', 'Чоршанба': 'Chorshanba', 'Пайшанба': 'Payshanba',
                        'Жума': "Juma", 'Шанба': 'Shanba', 'Якшанба': 'Yakshanba'
        },

        "ru":{
            "Понедельник": 'Душанба', 'Сешанба': 'Вторник', 'Чоршанба': 'Среда', 'Пайшанба': 'Четверг',
                        'Жума': "Пятница", 'Шанба': 'Суббота', 'Якшанба': 'Воскресенье'
        }
    }

        dict = {"kr":{
            "27": 'Тошкент', '37': 'Фарғона', '1': 'Андижон', '15': 'Наманган',
                        '4': "Бухоро", '9': 'Жиззах', '25': 'Қарши', '16': 'Нукус',
                        '14': 'Навоий', '18': 'Самарқанд', '21': 'Хива', '5': 'Гулистон', '6': 'Денов',
                        '26': 'Қўқон', '13': 'Марғилон', '3': 'Бишкек', '19': 'Туркистон',
                        '61': 'Зарафшон', '20': 'Ўш', '78': 'Урганч', '74': 'Термиз'
                },

                "uz":{
                    "27": 'Toshkеnt', '37': 'Fargʻona', '1': 'Andijon', '15': 'Namangan',
                        '4': "Buxoro", '9': 'Jizzax', '25': 'Qarshi', '16': 'Nukus',
                        '14': 'Navoiy', '18': 'Samarqand', '21': 'Xiva', '5': 'Guliston', '6': 'Denov',
                        '26': 'Qoʻqon', '13': 'Margʻilon', '3': 'Bishkek', '19': 'Turkiston',
                        '61': 'Zarafshon', '20': 'oʻsh', '78': 'Urganch', '74': 'Termiz'
                },

                "ru":{
                    "27": 'Ташкент', '37': 'Фарғона', '1': 'Андижан', '15': 'Наманган',
                        '4': "Бухара", '9': 'Джизак', '25': 'Карши', '16': 'Нукус',
                        '14': 'Навои', '18': 'Самарканд', '21': 'Хива', '5': 'Гулистан', '6': 'Денов',
                        '26': 'Коканж', '13': 'Маргилан', '3': 'Бишкек', '19': 'Туркмстон',
                        '61': 'Зарафшон', '20': 'Ўш', '78': 'Урганч', '74': 'Термиз'
                }
                }
        shaxar = dict[til][str(a)]
        
        for i in city_href:
            table_data = i.find_all('td')
            data = [j.text for j in table_data]
            kun_s = data[1]
            kun = data[2]
            tong = data[3]
            quyosh = data[4]
            pewn = data[5]
            asr = data[6]
            shom = data[7]
            xufton = data[8]
            kuni = xafta[til][kun]  
            dict_time = {
                'kun':kuni,
                'shaxar':shaxar,
                'tong':tong,
                'quyosh':quyosh,
                'peshin':pewn,
                'asr':asr,
                'shom':shom,
                'xufton':xufton,
                'soat':current_time
            }
            # print(kun_s , kun, tong, quyosh, pewn, asr, shom, xufton, date, current_time)
            # print(dict_time)
        
        return dict_time
        
        
