# 引入requests库
import requests
# 从bs4引入BeautifulSoup并为了方便命名为bs
from bs4 import BeautifulSoup as bs

# 解析一下url
res = requests.request('GET', 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')

# 判断url是否解析成功
if res.status_code == 200:
    # 调用bs，并使用html.parser，将结果命名为bs。
    bs = bs(res.text, 'html.parser')
    # 打印bs的类型
    print(type(bs))
    # 打印bs本身
    print(bs)

else:
    exit()
