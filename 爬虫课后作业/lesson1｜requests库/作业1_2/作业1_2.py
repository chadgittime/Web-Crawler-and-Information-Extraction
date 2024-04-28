# 2 图像下载
# 要求：获取下面的图片，并且储存图片。
import requests

res = requests.get('https://weibo.com/favicon.ico')

photo = res.content

with open('weibo.ico', 'wb') as f:
    f.write(photo)
