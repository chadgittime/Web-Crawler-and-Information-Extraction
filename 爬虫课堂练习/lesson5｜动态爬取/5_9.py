# 导入模块
import requests

# 设置评论区请求链接
comment_url = 'https://music.facode.cn/index.php/Home/Index/pl_list.html'
# 设置第 1 页表单提交数据

for i in range(1, 4):
    payload = {
        'voice_id': 403778,
        'info': 2,
        'page': i
    }

    # 发起请求，获取网页内容
    comment_res = requests.post(comment_url, data=payload)

    # 使用json()方法，将response对象，转为列表/字典
    json_data = comment_res.json()
    # 一层一层地取字典，获取评论列表
    list_comment = json_data['data']
    # list_comment是一个列表，comment是它里面的元素
    for comment in list_comment:
        # 以user_name为键，查找用户名
        print(comment['user_name'])
        print(comment['time'])
        print(comment['content'])
        print('\n')
