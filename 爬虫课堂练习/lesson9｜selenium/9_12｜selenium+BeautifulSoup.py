import time

from bs4 import BeautifulSoup as Bs
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://y.qq.com/n/ryqq/songDetail/000xdZuV2LcQ19')
time.sleep(2.5)

button = driver.find_element_by_class_name('comment__show_all_link')
driver.execute_script("arguments[0].click();", button)
time.sleep(2.5)

bs = Bs(driver.page_source, 'html.parser')
comments = bs.select('div.mod_hot_comment')[1].select('li.comment__list_item')

for comment in comments:
    user = comment.select('a.c_tx_thin')[0].text
    content = comment.find('p').text
    print('······························\n{}说:\n{}'.format(user, content))

driver.close()
