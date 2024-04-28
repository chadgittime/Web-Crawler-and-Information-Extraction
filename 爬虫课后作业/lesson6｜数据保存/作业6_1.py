def save_csv():
    import csv
    with open('豆瓣TOP250.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['序号', '电影名', '评分', '推荐语', '链接'])
        writer.writerows(all_movies)
    print('csv文件保存成功')


def save_excel():
    import openpyxl
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = '豆瓣TOP250'
    sheet.append(['序号', '电影名', '评分', '推荐语', '链接'])
    for movie in all_movies:
        sheet.append(movie)
    wb.save('豆瓣TOP250.xlsx')
    print('excel文件保存成功')


def get_data():
    import requests
    global all_movies
    all_movies = []
    for i in range(0, 10):
        page_num = 25 * i

        from bs4 import BeautifulSoup as bs
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        res = requests.request("GET", 'https://movie.douban.com/top250?start=' + str(page_num), headers=header)
        bs = bs(res.text, 'html.parser')
        movies = bs.find_all('div', class_='item')
        for movie in movies:
            seq = movie.find('em').text
            name = movie.find('span', class_='title').text
            rate = movie.find('span', class_='rating_num').text
            try:
                recom = movie.find('span', class_='inq').text
            except:
                recom = ''
            link = movie.find('a')['href']

            movie = [seq, name, rate, recom, link]
            all_movies.append(movie)
    print('数据获取成功')


get_data()
save_csv()
save_excel()
