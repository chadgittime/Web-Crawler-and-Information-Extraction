import requests

# 创建一个session对话
session = requests.session()

url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
user = {'log': input('请输入账号：\n'),
        'pwd': input('请输入密码：\n'),
        'wp-submit': '登录',
        'redirect_to': ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
        'testcookie': 1
        }
login_in = session.post(url=url, headers=headers, data=user)
# 此时就不需要获取login_in.cookies了

url_comment = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
comment = {
    'comment': input('请输入你想法的评论：\n'),
    'submit': '发表评论',
    'comment_post_ID': 13,
    'comment_parent': 0
}
# 这里session.post已经自动获取
comment = session.post(url=url_comment, headers=headers, data=comment)
print(comment)
