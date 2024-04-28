def get_html():
    import requests
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                      '100.0.4896.127 Safari/537.36'
    }
    res = requests.request("GET", 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html',
                           headers=header,
                           timeout=30)

    with open('Travel_book.html', 'w') as f:
        f.write(res.text)


def analysis():
    global bs
    from bs4 import BeautifulSoup as bs
    with open('Travel_book.html', 'r') as f:
        html = f.read()
        bs = bs(html, 'html.parser')
    return bs


def get_data():
    n = 1
    books = bs.select('article.product_pod')
    for book in books:
        book_name = book.find('a')['href'][9:-11].split('_')[0]
        book_point = book.find('p')['class'][1]
        book_price = book.find(class_='price_color').text.replace('Â', '')
        print("Travel类别下的第" + str(n) + "本书")
        print("书名：" + book_name)
        if str(book_point) == 'One':
            print("评分：一颗星")
        elif str(book_point) == 'Two':
            print("评分：两颗星")
        elif str(book_point) == 'Three':
            print("评分：三颗星")
        elif str(book_point) == 'Four':
            print("评分：四颗星")
        elif str(book_point) == 'Five':
            print("评分：五颗星")
        print("价钱：" + book_price)
        print('\n')
        n = n + 1


if __name__ == '__main__':
    get_html()
    analysis()
    get_data()
