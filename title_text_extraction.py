import requests
from bs4 import BeautifulSoup
import time


url = 'https://www.infocom.am/hy/Article/63274'

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

    req = requestText(url)
    bsoup = BeautifulSoup(req.content, 'html.parser')
    title_h1 = bsoup.find('h1', class_='news-title')
    title = title_h1.text.strip()

    divs = bsoup.find('div', class_='col-sm col-md-7 offset-md-1')
    children_divs = divs.findChildren('div')
    texts_aray = ''
    for children_div in children_divs:
        txt_div = children_div.findChildren('div')
        if len(txt_div) > 0:
            text = txt_div[0].text
            texts_aray += text + '\n'
    print(title + '\n', texts_aray)



