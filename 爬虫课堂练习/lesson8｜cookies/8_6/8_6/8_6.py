import json

import requests

session = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}


def read_cookies():
    with open('/Users/tomatotaco1/PycharmProjects/pythonProject/爬虫课堂练习/lesson8｜cookies/8_6/8_6/cookies.txt', 'r') as f:
        cookies_dict = json.loads(f.read())
        cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    return cookies


def sign():
    url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    user = {'log': input('请输入你的账号：\n'),
            'pwd': input('请输入你的密码：\n'),
            'wp-submit': '登录',
            'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
            'testcookie': '1'}
    session.post(url=url, headers=headers, data=user)
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    cookies_str = json.dumps(cookies_dict)
    with open('/Users/tomatotaco1/PycharmProjects/pythonProject/爬虫课堂练习/lesson8｜cookies/8_6/8_6/cookies.txt', 'w') as f:
        f.write(cookies_str)


def commenting():
    comment_url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
    content = {
        'comment': input('请输入你要发表的评论：\n'),
        'submit': '发表评论',
        'comment_post_ID': '13',
        'comment_parent': '0'
    }
    return session.post(comment_url, headers=headers, data=content)


try:
    session.cookies = read_cookies()
    print('cookies加载成功')
except:
    sign()
    print('登陆成功')

if commenting().status_code == 200:
    print('评论发送成功')
else:
    print('评论发送失败')
    sign()
    commenting()
