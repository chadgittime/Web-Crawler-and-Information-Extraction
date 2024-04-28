import requests
from bs4 import BeautifulSoup

url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spder-men0.0.html'
res = requests.get(url)
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')
# 使用find()方法提取首个<div>元素，并放到变量item里。
item = soup.find_all('div')
# 打印item的数据类型
print(type(item))
# 打印item
print(item)
