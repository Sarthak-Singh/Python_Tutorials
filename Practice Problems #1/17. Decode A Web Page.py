import requests
from bs4 import BeautifulSoup


base_url = 'https://www.nytimes.com/'


def article_titles(url):
    art = requests.get(url)
    obj = BeautifulSoup(art.text, 'html.parser')

    for titles in obj.find_all(class_="story-heading"):
        if titles.a:
            print(titles.a.text.replace('\n', ' ').strip())
        else:
            print(titles.content[0].strip())


article_titles(base_url)
