import smtplib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from price_parser import Price

PRODUCT_URL_CSV = 'data/products.csv'
SEND_MAIL= True

def get_urls(csv):
    df = pd.read_csv(csv)
    return df

def extract_source(url):
    agent = {"User-Agent":"Mozilla/5.0"}
    res = requests.get(url, headers=agent)
    return res.text

def get_price(html):
    soup = BeautifulSoup(html, 'html.parser')

    return soup.find_all('p', class_="chakra-text css-qhbnuv")
    # print(price_string)

def get_dicts(df):
    return df.to_dict('records')


print(get_price(extract_source('https://stockx.com/en-gb/nike-dunk-low-grey-fog')))
# print(extract_source(get_dicts(get_urls(PRODUCT_URL_CSV))[0]['url']))