import requests
from bs4 import BeautifulSoup

# 请求html，得到response
res_comments = requests.get('https://music.facode.cn/index.php/Home/Index/voice_details/id/403778')
# 解析html
bs_comments = BeautifulSoup(res_comments.text, 'html.parser')
# 查找class属性值为“comment__list_item c_b_normal”的li标签，得到一个由标签组成的列表
list_comments = bs_comments.find_all('li', class_='comment__list_item c_b_normal')
# 对查找的结果执行循环
for comment in list_comments:
    # 打印出我们想要的用户名
    print(comment.find('a', class_='c_tx_thin').text)
    # 打印出我们想要的评论时间
    print(comment.find('div', class_='comment__date c_tx_thin').text)
    # 打印出我们想要的评论内容
    print(comment.find('p', class_='comment__text ').text)
