# 从selenium库中调用webdriver模块
import time

from selenium import webdriver

# 设置引擎为Chrome，真实地打开一个Chrome浏览器
driver = webdriver.Chrome()
# 访问页面
driver.get('https://www.baidu.com/')
time.sleep(5)  # 等待5秒
# 根据<span class='title-content-title'>标签提取所有元素
hot_news = driver.find_elements_by_class_name('title-content-title')
# 打印hot_news的数据类型
print(type(hot_news))
# 打印hot_news
print(hot_news)
driver.close()  # 关闭浏览器
