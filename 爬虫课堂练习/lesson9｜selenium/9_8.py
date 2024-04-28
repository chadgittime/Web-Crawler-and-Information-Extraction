# Chrome浏览器设置方法
import time  # 调用time模块

from selenium import webdriver  # 从selenium库中调用webdriver模块

driver = webdriver.Chrome()  # 设置引擎为Chrome，真实地打开一个Chrome浏览器

driver.get('https://www.baidu.com/')  # 访问页面
time.sleep(5)  # 暂停5秒，等待浏览器缓冲

# 找到【百度】的输入框位置
baidu_input = driver.find_element_by_id('kw')
# 输入文字
baidu_input.send_keys('python')
# 找到【百度一下】按钮
button = driver.find_element_by_class_name('s_btn')
# 点击【百度一下】按钮
button.click()
time.sleep(5)
driver.close()  # 关闭浏览器
