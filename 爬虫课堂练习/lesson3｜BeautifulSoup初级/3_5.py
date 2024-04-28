# 调用requests库
import requests
# 调用BeautifulSoup库
from bs4 import BeautifulSoup

# 返回一个Response对象，赋值给res
res = requests.get('https://localprod.pandateacher.com'
                   '/python-manuscript/crawler-html/'
                   'spider-men5.0.html')
# 把Response对象的内容以字符串的形式返回
html = res.text
# 把网页解析为BeautifulSoup对象
soup = BeautifulSoup(html, 'html.parser')
# 通过匹配标签和属性提取我们想要的数据
items = soup.find_all(class_='books')
# 打印items
print(items)
# 打印items的数据类型
print(type(items))
