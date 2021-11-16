from typing import List, Any
import requests
from bs4 import BeautifulSoup
import time


BASE = 'https://168.am/'
PATH = '/home/sofia/Desktop/url/168Am/article_links.txt'


def get_page_news_links(page):
    news_list = []
    bsoup = BeautifulSoup(page, features='html.parser')
    divs = bsoup.find_all('div', class_='realated-item clearfix')
    for div in divs:
        contents = div.contents
        if len(contents) > 1:
            a = contents[1]
        else:
            continue
        news_list.append(a['href'])
    return news_list


def requestText(url):
    request = ''
    counter = 0
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    while request == '' and counter < 5:
        try:
            request = requests.get(url, headers=headers)
            if request.status_code != 200:
                request = ''
            if request.status_code == 404:
                break
            else:
                break
        except:
            time.sleep(5)
            counter += 1
            continue
    return request


def main():
    for i in range(1, 33):
        page_link = f'https://168.am/section/interesting/page/{i}'
        r = requestText(page_link)
        if r == '':
            continue
        page_article_links = get_page_news_links(r.content)
        for article_link in page_article_links:
            with open(PATH, 'a') as f:
                f.write(article_link + '\n')


main()