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
        movies = bs(res.text, 'html.parser')

        # 将需要的信息提取出来
        seq = movies.find_all('em')
        name = movies.find_all('img')[:-1]
        rate = movies.find_all('span', class_='rating_num')
        recom = movies.find_all('span', class_='inq')
        link = movies.find_all('div', class_='pic')

        # 将seq作为总量，因为有多少个序号就一定有多少个电影。
        for i in range(len(seq)):
            # 把每一个电影的五项信息都填入它们独有的movie当中
            movie = [seq[i].text, name[i]['alt'], rate[i].text, recom[i].text, link[i].find('a')['href']]
            # 并将每个movie填入最终的all_movie列表当中
            all_movie.append(movie)


    get_data()
# 在get_data重复三遍，也就是全部信息都写入all_movie之后再打印。
for movie in all_movie:
    print(movie)
