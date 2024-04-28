import openpyxl
import requests

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'contents'
sheet['A1'] = '用户名'
sheet['B1'] = '评论时间'
sheet['C1'] = '评论内容'

comment_url = 'https://music.facode.cn/index.php/Home/Index/pl_list.html'

for i in range(1, 4):
    payload = {
        'voice_id': 403778,
        'info': 2,
        'page': i
    }
    comment_res = requests.post(comment_url, data=payload)
    json_data = comment_res.json()
    list_comment = json_data['data']
    for comment in list_comment:
        user_name = comment['user_name']
        time = comment['time']
        content = comment['content']
        song = [user_name, time, content]
        sheet.append(song)

wb.save('contents.xlsx')
