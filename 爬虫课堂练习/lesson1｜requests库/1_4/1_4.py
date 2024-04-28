import requests

res = requests.get('https://www.baidu.com/favicon.ico')

pic = res.content

photo = open('baidu.ico', 'wb')

photo.write(pic)

photo.close()
