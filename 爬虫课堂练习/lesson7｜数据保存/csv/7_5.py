# 导入csv模块
import csv

# 调用open函数，读取模式打开demo.csv文件，newline=''、encoding='utf-8’
csv_file = open('/爬虫课堂练习/lesson6｜数据保存｜数据保存/7_4/demo.csv', 'r', newline='',
                encoding='utf-8')
# 用csv.reader()函数创建一个reader对象。
reader = csv.reader(csv_file)
# for循环遍历reader对象每一行并打印每行
for row in reader:
    print(row)

# 关闭文件
csv_file.close()
