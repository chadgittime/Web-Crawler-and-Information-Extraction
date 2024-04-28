import requests

session = requests.session()
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
data = {
    'log': input('请输入账号：\n'),
    'pwd': input('请输入密码：\n'),
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie': '1'
}
session.post(url, headers=headers, data=data)
# 打印cookies的类型,session.cookies就是登录的cookies
print(type(session.cookies))
# 打印cookies
print(session.cookies)
