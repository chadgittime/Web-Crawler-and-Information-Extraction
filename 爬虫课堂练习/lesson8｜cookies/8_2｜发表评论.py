import requests

url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
user = {'log': 'guowaiwai',
        'pwd': '20030312Gyy',
        'wp-submit': '登录',
        'redirect_to': ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
        'testcookie': 1
        }
login_in = requests.request('POST', url=url, headers=headers, data=user)

url_comment = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
comment = {
    'comment': input('请输入你想法的评论：\n'),
    'submit': '发表评论',
    'comment_post_ID': 13,
    'comment_parent': 0
}
comment = requests.request('POST', url=url_comment, headers=headers, data=comment, cookies=login_in.cookies)
print(comment.status_code)
