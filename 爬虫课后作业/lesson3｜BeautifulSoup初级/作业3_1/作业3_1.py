import requests


def get_html():
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                      '100.0.4896.127 Safari/537.36'
    }
    res = requests.request("GET", 'http://books.toscrape.com/', headers=header, timeout=30)

    with open('/爬虫课后作业/lesson3｜BeautifulSoup初级/作业3_1/Books to Scrape.html', 'w') as f:
        f.write(res.text)


def analysis():
    from bs4 import BeautifulSoup as bs
    global bs
    with open('/爬虫课后作业/lesson3｜BeautifulSoup初级/作业3_1/Books to Scrape.html', 'r') as f:
        html = f.read()
        bs = bs(html, 'html.parser')
    return bs


def get_data():
    # 首先找到书记类别所在的那个标签，应为所有ul当中的第三个。
    ul = bs.select('ul')[2]
    # 然后把标签里的所有小类别都拿出来
    each = ul.select('li')
    print('所有书籍类型：')
    for i in each:
        print(i.text.replace(' ', '').replace('\n', ''))


if __name__ == '__main__':
    get_html()
    analysis()
    get_data()
