import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

fw = open('news.txt', 'w')
for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        fw.write(story_heading.a.text.replace("\n", " ").strip())
    else:
        fw.write(story_heading.contents[0].strip())
fw.close()
