import requests
from bs4 import BeautifulSoup
import time
import json
import os


ARTICLE_PATH = '/home/sofia/Desktop/url/TertAM/filtered_links.txt'
PATH = '/home/sofia/Desktop/url/TertAM/json'


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
        for id, line in enumerate(lines):
            if id < 16711:
                continue
            req = requestText(line)
            bsoup = BeautifulSoup(req.content, 'html.parser')
            title_h1 = bsoup.find('h1', class_='inner-content__article-title fb fs20')
            try:
                title = title_h1.text.strip()
            except:
                return 0
            divs = bsoup.find('div', {'id': 'news-content-container'})
            texts_array = ''
            for children_p in divs:
                try:
                    text = children_p.text
                except:
                    continue
                if text.strip() != '':
                    texts_array += children_p.text + '\n'
            exe = {'title': title, 'text': texts_array}
            file_name = f'article{id}'
            with open(os.path.join(PATH, file_name), 'a') as f:
                json.dump(exe, f, ensure_ascii=False, indent=4)


main()
