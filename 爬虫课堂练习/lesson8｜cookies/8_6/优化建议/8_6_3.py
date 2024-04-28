# 引用requests
import json
import requests

# 用requests.session()创建session对象，相当于创建了一个特定的会话，帮我们自动保持了cookies
session = requests.session()
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
data = {
    # 用input函数填写账号和密码，这样代码更优雅，而不是直接把账号密码填上去
    'log': input('请输入账号：'),
    'pwd': input('请输入密码：'),
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie': '1'
}
# 在创建的session下用post发起登录请求，放入参数：请求登录的网址、请求头和登录参数
session.post(url, headers=headers, data=data)

cookies_txt = open('cookies.txt', 'r')
# 以reader读取模式，打开名为cookies.txt的文件
cookies_dict = json.loads(cookies_txt.read())
# 调用json模块的loads函数，把字符串转成字典
cookies = requests.utils.cookiejar_from_dict(cookies_dict)
# 把转成字典的cookies再转成cookies本来的格式
session.cookies = cookies
# 获取cookies：就是调用requests对象（session）的cookies属性
# 把我们想要评论的文章网址赋值给url_1
url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
# 把有关评论的参数封装成字典
data_1 = {
    'comment': input('请输入你想要发表的评论：'),
    'submit': '发表评论',
    'comment_post_ID': '13',
    'comment_parent': '0'
}
# 在创建的session下用post发起评论请求，放入参数：文章网址，请求头和评论参数，并赋值给comment
comment = session.post(url_1, headers=headers, data=data_1)
# 打印comment
print(comment)
