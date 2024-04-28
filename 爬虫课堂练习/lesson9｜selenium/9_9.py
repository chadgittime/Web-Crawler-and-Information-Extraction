# 从selenium库中调用webdriver模块
# 调用time模块
import time

from selenium import webdriver

# 设置引擎为Chrome，真实地打开一个Chrome浏览器
wd = webdriver.Chrome()

# 访问页面https://y.qq.com/n/ryqq/songDetail/000xdZuV2LcQ19
wd.get('https://y.qq.com/n/ryqq/songDetail/000xdZuV2LcQ19')
# 暂停5秒，等待浏览器缓冲
time.sleep(5)
