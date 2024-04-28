import requests
from bs4 import BeautifulSoup as bs

# 来个header，把自己伪装成一个浏览器的样子！
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
# ok可以requests了
res = requests.request('GET', 'https://www.xiachufang.com/explore/', timeout=30, headers=header)

bs = bs(res.text, 'html.parser')

whole_menu = []
# 按要求将所需数据打印出来
for i in bs.select('div.info.pure-u'):
    menu = []
    name = i.p.text.strip()
    ingredients = i.select('.ing.ellipsis')[0].text.strip()
    url = "https://www.xiachufang.com" + i.select('a')[0]['href']
    menu.append(name)
    menu.append(ingredients)
    menu.append(url)
    whole_menu.append(menu)

print(whole_menu)
