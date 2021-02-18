import requests
from bs4 import BeautifulSoup


base_url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
html = requests.get(base_url)
cleaned_html = BeautifulSoup(html.content, 'html.parser')
data1 = cleaned_html.find_all('div', {"class:", 'dek'})
for item in data1:
    print(item.text)
data2 = cleaned_html.find_all('section', {'class:', 'content-section'})
for item in data2:
    print(item.text)
