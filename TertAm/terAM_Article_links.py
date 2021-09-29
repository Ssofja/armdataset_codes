from typing import List, Any
import requests
from bs4 import BeautifulSoup
import time


BASE = 'https://www.tert.am'
PATH = '/home/sofia/Desktop/url/TertAM/article_links.txt'
# CAT_PATH = '/home/sofia/Desktop/url/Infocom/catheg_links.txt'


def get_page_news_links(page):
    bsoup = BeautifulSoup(page, features='html.parser')
    news_list = []
    for a in bsoup.find_all('a', class_='list__link db fb'):
        news_list.append(BASE + a['href'])
    return news_list



def requestText(url):
    request = ''
    while request == '':
        try:
            request = requests.get(url)
            if request.status_code != 200:
                request = ''
        except:

            time.sleep(5)
            continue
    return request


def main():

    for i in range(1, 1412):
        page_link = f'https://www.tert.am/am/news/politics/{i}?from_date=&to_date='
        r = requestText(page_link)
        page_article_links = get_page_news_links(r.content)
        for article_link in page_article_links:
            with open(PATH, 'a') as f:
                f.write(article_link + '\n')

main()