#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 全局配置
bark_id = '你的bark id'
icon_url = 'https://tse4-mm.cn.bing.net/th/id/OIP-C.eN-WxekffTLkN-wkuxiudAHaHa'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options=options)

driver.get('http://www.100bt.com/m/creditMall/?gameId=2#home')
time.sleep(5)

js = "window.scrollBy(0,6000);"
driver.execute_script(js)
time.sleep(3)
js = "window.scrollBy(0,18000);"
driver.execute_script(js)
time.sleep(3)

items = driver.find_elements(By.XPATH, '//*[@class="item"]')

news = []
for item in items:
    title = item.find_element(By.XPATH, './/*[@class="reward"]/p').text
    remain = item.find_element(By.XPATH, './/*[@class="stock"]').text
    # print(title)
    if (title == "1奥币" or title == "10奥币" or title == "30奥币") and remain != "库存:0":
        news.append((title, remain))
    
for new in news:
    print(new[0])
    driver.get(f'https://api.day.app/{bark_id}/积分商城上新/{new[0]},{new[1]}?icon={icon_url}')
    time.sleep(2)

driver.close()