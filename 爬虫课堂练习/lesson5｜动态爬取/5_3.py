import requests
from bs4 import  BeautifulSoup

# 请求html，得到response
res_comments = requests.get('https://music.facode.cn/index.php/Home/Index/voice_details/id/403778')
# 打印它
print(res_comments.text)