# 从selenium库中调用webdriver模块
import time

from selenium import webdriver

# 设置引擎为Chrome，真实地打开一个Chrome浏览器
driver = webdriver.Chrome()
# 访问页面
driver.get('https://www.baidu.com/')
time.sleep(5)  # 等待5秒

pageSource = driver.page_source  # 获取完整渲染的网页源代码
print(type(pageSource))  # 打印pageSource的类型
print(pageSource)  # 打印pageSource
driver.close()  # 关闭浏览器
