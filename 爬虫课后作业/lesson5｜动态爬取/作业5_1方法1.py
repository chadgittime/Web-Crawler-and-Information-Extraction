import requests

comment_url = 'https://music.facode.cn/index.php/Home/Index/pl_list.html'


def get_page():
    global page_num

    payload = {
        'voice_id': 403778,
        'info': 2,
        'page': 1
    }

    res = requests.post(comment_url, data=payload)

    json_data = res.json()

    totalnum = int(json_data['totalnum'])

    page_num = int(totalnum / 10) + 1


def get_data():
    for page in range(1, page_num + 1):
        payload = {
            'voice_id': 403778,
            'info': 2,
            'page': page
        }
        res = requests.post(comment_url, data=payload)
        json_data = res.json()
        list_comment = json_data['data']
        for comment in list_comment:
            print(comment['user_name'])
            print(comment['time'])
            print(comment['content'])
            print('\n')


get_page()
get_data()
