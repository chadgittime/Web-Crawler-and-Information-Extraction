import requests
from bs4 import BeautifulSoup as bs

res = requests.get('https://localprod.pandateacher.com'
                   '/python-manuscript/crawler-html/'
                   'spider-men5.0.html')
bs = bs(res.text, 'html.parser')
items = bs.find_all(class_='books')

for i in items:
    print(i)
    print('\n')
