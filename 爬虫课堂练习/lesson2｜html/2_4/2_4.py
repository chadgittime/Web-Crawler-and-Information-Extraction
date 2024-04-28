import requests

res = requests.request('GET', 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')

html = res.text

with open('pandateacher.html', 'w') as f:
    f.write(html)
