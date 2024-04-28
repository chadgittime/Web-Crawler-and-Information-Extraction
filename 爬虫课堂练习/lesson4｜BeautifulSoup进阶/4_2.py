import requests
from bs4 import BeautifulSoup as bs

# 来个header，把自己伪装成一个浏览器的样子！
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
# ok可以requests了
res = requests.request('GET', 'https://www.xiachufang.com/explore/', timeout=30, headers=header)

# 把捕捉到的数据进行一个保存
with open('menu_list.html', 'w') as f:
    f.write(res.text)

# 再读取一下数据，用bs解析一下。
with open('menu_list.html', 'r') as f:
    html = f.read()
    bs = bs(html, 'html.parser')

menu = bs.find_all(class_='info pure-u')
print(menu)