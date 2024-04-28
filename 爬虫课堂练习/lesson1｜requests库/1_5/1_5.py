import requests

res = requests.get('https://www.baidu.com/')

html = res.text

txt = open('html.txt', 'a', encoding='utf-8')
# encoding='utf-8'部分在运行出问题时需要写一个

txt.write(html)

txt.close()
