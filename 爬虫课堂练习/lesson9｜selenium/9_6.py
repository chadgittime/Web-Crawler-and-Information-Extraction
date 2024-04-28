import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
time.sleep(5)
hot_news = driver.find_elements_by_class_name('title-content-title')
for i in hot_news:
    print(i.text)
driver.close()
