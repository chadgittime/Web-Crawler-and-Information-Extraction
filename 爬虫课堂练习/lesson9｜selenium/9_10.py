import time  # 调用time模块

from selenium import webdriver  # 从selenium库中调用webdriver模块

driver = webdriver.Chrome()  # 设置引擎为Chrome，真实地打开一个Chrome浏览器

driver.get('https://y.qq.com/n/ryqq/songDetail/000xdZuV2LcQ19')  # 访问页面
time.sleep(5)  # 暂停5秒，等待浏览器缓冲

comment_jc = driver.find_elements_by_class_name('mod_hot_comment')[1]
comments = comment_jc.find_elements_by_class_name('comment__list_item')  # 使用class_name找到评论
print(len(comments))  # 打印获取到的评论个数
for comment in comments:  # 循环
    sweet = comment.find_element_by_tag_name('p')  # 找到评论
    print('评论：%s\n ---\n' % sweet.text)  # 打印评论
driver.close()
