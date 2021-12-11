import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen


def fill_news_1(news, def_root):
    for s in def_root.findall(r'./channel/item'):
        date = s.findtext('pubDate')
        title = s.findtext('title')
        news.append({'pubDate': date, 'title': title})


def fill_news_2(news, def_root):
    for parent in def_root.findall(r'./channel/item'):
        dictionary = {}
        for child in parent:
            dictionary[child.tag] = child.text
        news.append(dictionary)


data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
news1 = []
news2 = []
fill_news_1(news1, root)
with open('news.json', 'w', encoding='utf-8') as file:
    json.dump(news1, fp=file, ensure_ascii=False, indent=4)
fill_news_2(news2, root)
with open('news2.json', 'w', encoding='utf-8') as file2:
    json.dump(news2, fp=file2, ensure_ascii=False, indent=4)
