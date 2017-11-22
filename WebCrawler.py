import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page=1
    while page<=max_pages:
        url='https://twitter.com/realDonaldTrump?lang=en'
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,"html.parser")
        for link in soup.findAll('a'):
            href=link.get('href')
            title=link.string
            print(href)
            #print(title)
            get_single_item_data(href)
        page+=1

def get_single_item_data(item_url):
    url = 'https://twitter.com/realDonaldTrump?lang=en'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.findAll('div',{'class':'AppContent'}):
        print(item_name.string)
trade_spider(1)