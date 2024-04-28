# 引入requests和json模块
import json

import requests

session = requests.session()
url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
data = {
    'log': input('请输入你的账号:\n'),
    'pwd': input('请输入你的密码:\n'),
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie': '1'
}

session.post(url, headers=headers, data=data)
cookies = session.cookies

# 把cookies转化成字典
cookies_dict = requests.utils.dict_from_cookiejar(cookies)

# 打印cookies_dict
print(cookies_dict)

# 为了美观
print('\n')

# 调用json模块的dumps函数，把cookies从字典再转成字符串
cookies_str = json.dumps(cookies_dict)

# 打印cookies_str
print(cookies_str)

# 存储转成字符串的cookies
with open('cookies.txt', 'w') as f:
    f.write(cookies_str)
