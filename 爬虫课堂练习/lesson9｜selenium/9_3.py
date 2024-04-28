# 从selenium库中调用webdriver模块
import time

from selenium import webdriver

# 设置引擎为Chrome，真实地打开一个Chrome浏览器
driver = webdriver.Chrome()
# 访问页面
driver.get('https://www.baidu.com/')
time.sleep(5)  # 等待5秒
# 解析网页并提取第一个<span class='title-content-title'>标签
hot_new = driver.find_element_by_class_name('title-content-title')
# 打印hot_new的文本
print(hot_new.text)
driver.close()  # 关闭浏览器
