import requests
from bs4 import BeautifulSoup
import time
import json
import os




ARTICLE_PATH = '/home/sofia/Desktop/url/Infocom/filtered_links.txt'
PATH = '/home/sofia/Desktop/url/Infocom/json'


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
    with open(ARTICLE_PATH, "r") as file1:
        file_content = file1.read()
        lines = file_content.splitlines()
        for id,line in enumerate(lines):

            req = requestText(line)
            bsoup = BeautifulSoup(req.content, 'html.parser')
            title_h1 = bsoup.find('h1', class_='news-title')
            title = title_h1.text.strip()
            divs = bsoup.find('div', class_='col-sm col-md-7 offset-md-1')
            children_divs = divs.findChildren('div')
            texts_aray = ''
            if len(children_divs):
                for children_div in children_divs:
                    txt_div = children_div.findChildren('div')
                    if len(txt_div) > 0:
                        text = txt_div[0].text
                        texts_aray += text + '\n'
            else:
                array_p = divs.find('p')
                for children_p in divs:
                    try:
                        text = children_p.text
                    except:
                        continue
                    if text.strip()!= '':
                        texts_aray += children_p.text + '\n'

            exe = {'title': title, 'text': texts_aray}
            file_name = f'article{id}'
            with open(os.path.join(PATH, file_name), 'a') as f:
                json.dump(exe, f, ensure_ascii=False, indent=4)


main()




