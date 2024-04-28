import requests

comment_url = 'https://music.facode.cn/index.php/Home/Index/pl_list.html'

page = 1
while True:
    payload = {
        'voice_id': 403778,
        'info': 2,
        'page': page
    }
    res = requests.post(comment_url, data=payload)
    json_data = res.json()
    list_comment = json_data['data']
    if len(list_comment) != 0:
        for comment in list_comment:
            print(comment['user_name'])
            print(comment['time'])
            print(comment['content'])
            print('\n')
        page = page + 1

    else:
        break
