from typing import List, Any
import requests
from bs4 import BeautifulSoup
import time


BASE = 'https://www.infocom.am'
PATH = '/home/sofia/Desktop/url/Infocom/news_links.txt'
CAT_PATH = '/home/sofia/Desktop/url/Infocom/catheg_links.txt'


def get_page_news_links(page):
    bsoup = BeautifulSoup(page, features='html.parser')
    news_list = []
    for a in bsoup.find_all('a', class_='infotag-page-news-item'):
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


def page_numbers(lin):
    r = requestText(lin)
    bsoup = BeautifulSoup(r.content, features='html.parser')
    ul = bsoup.find('ul', class_='pagination')
    lis = list(ul.children)
    if len(lis) < 2:
        return len(lis)
    pages_num = int(lis[-2].text)
    return pages_num


def main():
    all_cat_links = []
    with open(CAT_PATH, 'r') as f:
         all_cat_links = f.read().splitlines()

    for catheg_link in all_cat_links:
        page_num = page_numbers(catheg_link)

        for i in range(1, page_num + 1):
            page_link = f'{catheg_link}&p={i}'
            r = requestText(page_link)
            page_article_links = get_page_news_links(r.content)

            for article_link in page_article_links:
                with open(PATH, 'a') as f:
                    f.write(article_link + '\n')