import requests
from bs4 import BeautifulSoup
import time
import json
import os
import concurrent.futures


ARTICLE_PATH = '/home/sofia/Desktop/url/168Am/filtered_links.txt'
PATH = '/home/sofia/Desktop/url/168Am/json_test'


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


def run(i):
    id = i[0]
    line = i[1]
    req = requestText(line)
    bsoup = BeautifulSoup(req.content, 'html.parser')
    title_h1 = bsoup.find('h1', class_='single-title')
    try:
        title = title_h1.text.strip()
    except:
        return
    divs = bsoup.find('div', class_='single-content-wrapper')
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

def main():
    with open(ARTICLE_PATH, "r") as file1:
        file_content = file1.read()
        lines = file_content.splitlines()
        with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executor:
            print(len(lines))
            future_to_url = {executor.submit(run, i): i for i in list(enumerate(lines))}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future.result()


main()
