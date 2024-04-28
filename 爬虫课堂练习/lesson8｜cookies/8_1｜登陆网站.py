# 引入requests
import requests

# 把登录的网址赋值给url
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
# 加请求头，前面有说过加请求头是为了模拟浏览器正常的访问，避免被反爬虫
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
# 把有关登录的参数赋值给data
data = {'log': 'guowaiwai',
        'pwd': '20030312Gyy',
        'wp-submit': '登录',
        'redirect_to': ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
        'testcookie': 1
        }
# 发送post请求，然后赋值给login_in
login_in = requests.request('POST', url=url, headers=headers, data=data)
# 打印login_in
print(login_in)
