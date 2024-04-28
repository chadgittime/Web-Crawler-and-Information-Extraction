# 引用requests库
import requests
# 引用BeautifulSoup库
from bs4 import BeautifulSoup

# 为躲避反爬机制，伪装成浏览器的请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# 获取数据
res_foods = requests.get('http://www.xiachufang.com/explore/', headers=headers)
# 解析数据
bs_foods = BeautifulSoup(res_foods.text, 'html.parser')
# 查找最小父级标签
list_foods = bs_foods.find_all('div', class_='info pure-u')

# 提取第0个父级标签中的<a>标签
tag_a = list_foods[0].find('a')
# 菜名，使用strip()函数去掉了多余的空格
name = tag_a.text.strip()
# 获取URL
URL = 'http://www.xiachufang.com' + tag_a['href']

# 提取第0个父级标签中的<p>标签
tag_p = list_foods[0].find(class_='ing ellipsis')
# 食材，使用strip()函数去掉了多余的空格
ingredients = tag_p.text.strip()
# 打印食材
print(ingredients)
