import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup=BeautifulSoup(r_html,'html.parser')

tags=soup('meta')


for t in tags:
    print(t.get('content',None))
    # print(t.content[0])