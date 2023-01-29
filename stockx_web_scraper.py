import requests
from bs4 import BeautifulSoup
URL ='https://stockx.com/en-gb/nike-dunk-low-grey-fog'

def extract_source(url):
    agent = {"User-Agent":"Mozilla/5.0"}
    page = requests.get(url, headers=agent)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

#, attrs={'date-component': 'LastSale' }

def get_price(page):
    pages_to_filter = page.find_all(class_='css-wpoilv')

    for pages in pages_to_filter:
        p_tags = pages.find_all('p')
        
    for p_tag in p_tags:

        if(p_tag.has_attr('class') and f"{p_tag['class'][0]} {p_tag['class'][1]}" == "chakra-text css-xfmxd4"):

            return p_tag.text.strip()


print(get_price(extract_source(URL)))