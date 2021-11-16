import requests
from bs4 import BeautifulSoup
import time
import json
import os




ARTICLE_PATH = '/home/sofia/Desktop/url/aravot.am/filtered_links.txt'
PATH = '/home/sofia/Desktop/url/aravot.am/json'


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
    with open(ARTICLE_PATH, "r") as file1:
        file_content = file1.read()
        lines = file_content.splitlines()
        for id, line in enumerate(lines):
            req = requestText(line)
            bsoup = BeautifulSoup(req.content, 'html.parser')
            title_h1 = bsoup.find('h1', class_='single-post-title')
            try:
                title = title_h1.getText()
            except:
                continue
            divs = bsoup.find('div', class_='single-entry-summary-post-content')
            children_divs = divs.findChildren('div')
            texts_aray = ''
            array_p = divs.findAll('p')
            for p in array_p:
                try:
                    text = p.getText()
                except:
                    continue
                if text.strip() != '':
                    texts_aray += p.text + '\n'

            exe = {'title': title, 'text': texts_aray}
            file_name = f'article{id}'
            with open(os.path.join(PATH, file_name), 'a') as f:
                json.dump(exe, f, ensure_ascii=False, indent=4)


main()
