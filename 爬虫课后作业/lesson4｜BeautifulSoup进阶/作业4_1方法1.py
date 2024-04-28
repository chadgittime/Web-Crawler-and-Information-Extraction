import requests

# 把全部电影的列表创建在此处是为了打印的时候能让所有结果存储于这个列表内
all_movie = []
for i in range(0, 3):
    # 在此处可以得到三个值，分别是0、25、50，正好对应了1、2、3页。
    page_num = 25 * i


    def get_data():
        from bs4 import BeautifulSoup as bs
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        res = requests.request("GET", 'https://movie.douban.com/top250?start=' + str(page_num), headers=header)
        bs = bs(res.text, 'html.parser')
        # 查找最小父级标签，此标签中包含了所有需要的信息。
        movies = bs.find_all('div', class_='item')
        for movie in movies:
            seq = movie.find('em').text
            name = movie.find('span', class_='title').text
            rate = movie.find('span', class_='rating_num').text
            try:
                recom = movie.find('span', class_='inq').text
            except:
                recom = '（无推荐语）'
            link = movie.find('a')['href']

            movie = [seq, name, rate, recom, link]
            all_movie.append(movie)


    get_data()

print(all_movie)
