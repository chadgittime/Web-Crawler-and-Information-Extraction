# Chrome浏览器设置方法
import time

from selenium import webdriver  # 从selenium库中调用webdriver模块

driver = webdriver.Chrome()  # 设置引擎为Chrome，真实地打开一个Chrome浏览器

# 打开网页
driver.get('https://www.baidu.com')
# 等待5秒
time.sleep(5)
# 关闭浏览器
driver.close()
