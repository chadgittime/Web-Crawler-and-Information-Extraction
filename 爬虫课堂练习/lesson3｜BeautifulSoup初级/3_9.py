import requests
from bs4 import BeautifulSoup as bs

res = requests.get('https://localprod.pandateacher.com'
                   '/python-manuscript/crawler-html/'
                   'spider-men5.0.html')
bs = bs(res.text, 'html.parser')

# 方法1
print('这是方法1')
books = bs.find_all(class_='books')
for book in books:
    print(book.find('h2').text)
    print(book.find(class_='title').text)
    print(book.find(class_='title')['href'])
    print(book.find(class_='info').text)
    print('\n')

# 方法2
print('这是方法2')
books = bs.select('div.books')
for book in books:
    print(book.select('a')[0].text)
    print(book.select('a')[1].text)
    print(book.select('a')[1]['href'])
    print(book.select('p.info')[0].text)
    print('\n')
