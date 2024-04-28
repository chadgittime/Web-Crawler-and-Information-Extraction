import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15',
}
payload = {
    'voice_id': 403778,
    'info': 2,
    'page': 1
}
res = requests.request("POST", 'https://music.facode.cn/index.php/Home/Index/pl_list.html', timeout=30, headers=header,
                       data=payload)
content = res.text
print(res.status_code)
print(type(res.text))
