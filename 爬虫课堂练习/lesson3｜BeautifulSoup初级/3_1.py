import requests

res = requests.request('GET', 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')

if res.status_code == 200:
    print(res.text)

else:
    exit()
