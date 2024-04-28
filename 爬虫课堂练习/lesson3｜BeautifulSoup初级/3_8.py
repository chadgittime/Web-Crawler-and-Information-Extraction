import requests
from bs4 import BeautifulSoup as bs

res = requests.get('https://localprod.pandateacher.com'
                   '/python-manuscript/crawler-html/'
                   'spider-men5.0.html')
bs = bs(res.text, 'html.parser')

books = bs.find_all(class_='books')
for book in books:
    print(type(book.find('h2').text))
    print(type(book.find(class_='title')['href']))
    print(type(book.find(class_='title').text))
    print(type(book.find(class_='info').text))
    print('\n')
