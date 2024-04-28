import requests
from bs4 import BeautifulSoup as bs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
res = requests.request("GET", 'http://www.xiachufang.com/explore/', headers=headers)
foods = bs(res.text, 'html.parser')

name = foods.find_all('p', class_='name')
ingredients = foods.find_all('p', class_='ing ellipsis')

whole_menu = []
for i in range(len(name)):
    food = [name[i].text[18:-14], name[i].find('a')['href'], ingredients[i].text[1:-1]]
    whole_menu.append(food)
print(whole_menu)
