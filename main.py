import smtplib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from price_parser import Price
from lxml import html, etree
from itertools import cycle
import json
import random

PRODUCT_URL_CSV = 'data/products.csv'
SEND_MAIL= True
# proxies = {
#     'http://129.226.33.104:3218',
#     'http://169.57.1.85:8123',
#     'http://85.25.91.141:15333',
#     'http://103.149.162.195:80',
#     'http://8.218.213.95:10809'
#     'http://114.121.248.251:8080'
# }

def get_proxies():

    proxies_req = requests.get('https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc',  headers={'Accept': 'application/json'})
    proxies = proxies_req.json()['data']

    
    return proxies


def format_proxy(proxy):
    return f"http://{proxy['ip']}:{proxy['port']}"

# def get_urls(csv):
#     df = pd.read_csv(csv)
#     return df

def extract_source(url):
    headers={'accept':'about/buying',
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
	}
    proxies = get_proxies()

    for i in range(0, len(proxies)):
        random_number = random.randint(0, len(proxies))
        proxy_candidate = format_proxy(proxies[random_number])
        print('proxy_candidate', proxy_candidate)

        try:
            res = requests.get(url, headers=headers, proxies={'http': proxy_candidate}, timeout=15)
            return res.text
        except OSError as e:
            print('Error', e)



def get_price(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all('div', class_='css-722v25')
   

# def get_dicts(df):
#     return df.to_dict('records')
    
print(extract_source('https://stockx.com/en-gb/buy/nike-dunk-low-grey-fog?size=9&defaultBid=true/robots.txt'))
# print(extract_source('https://stockx.com/en-gb/nike-dunk-low-grey-fog').text)
print(get_price(extract_source('https://stockx.com/en-gb/buy/nike-dunk-low-grey-fog?size=9&defaultBid=true/robots.txt')))
# print(extract_source(get_dicts(get_urls(PRODUCT_URL_CSV))[0]['url']))