# 3 音频下载
# 要求：获取下面的音乐，并且储存它。
import requests

res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')

music = res.content

with open('music.mp3', 'wb') as f:
    f.write(music)
