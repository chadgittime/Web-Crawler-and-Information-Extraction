# 导入模块
import requests

# 设置评论区请求链接
comment_url = 'https://music.facode.cn/index.php/Home/Index/pl_list.html'
# 设置第 1 页表单提交数据
payload = {
    'voice_id': 403778,
    'info': 2,
    'page': 1
}

# 发起请求，获取网页内容
res = requests.post(comment_url, data=payload)

# 读取 JSON 数据，查看json方法读取数据后的数据类型
json_data = res.json()['data']
for name in json_data:
    print(name['user_name'])
