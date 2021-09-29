import requests
from bs4 import BeautifulSoup
import time


BASE = 'https://www.infocom.am'
CAT_PATH = '/home/sofia/Desktop/url/Infocom/catheg_links.txt'


def get_cathegory_links(page):
    bsoup = BeautifulSoup(page, features='html.parser')
    catheg_list = []
    for a in bsoup.find_all('a', class_='infotag-list-item'):
        catheg_list.append(a['href'])
    return catheg_list


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
    all_scraped_news = []
    for i in range(1, 54):
        page_link = 'https://www.infocom.am/hy/Infotags?p=i'.format(i)
        r = requestText(page_link)
        page_categ_links = get_cathegory_links(r.content)
        for catheg_link in page_categ_links:
            with open(CAT_PATH, 'a') as f:
                f.write(catheg_link + '\n')
        

