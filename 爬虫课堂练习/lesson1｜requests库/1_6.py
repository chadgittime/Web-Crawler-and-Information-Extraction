# 引用requests库
import requests

# 下载百度源代码，我们得到一个对象，它被命名为res
res = requests.get('https://www.baidu.com/')

# 定义Response对象的编码为gbk
res.encoding = 'gbk'

# 把Response对象的内容以字符串的形式返回
html = res.text

# 打印html
print(html)
