#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import datetime
import sys

bark_id = '你的bark id'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options=options)

uname = sys.argv[1]
pword = sys.argv[2]

driver.get('https://www.wiring-world.com/shop.html')
driver.maximize_window()
time.sleep(3)

element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/ul/li[1]/a/span')
driver.execute_script("arguments[0].click()", element)
time.sleep(3)

# print("开始登录")
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/form/dl/dd[1]/div/input').send_keys(uname)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/form/dl/dd[2]/div/input').send_keys(pword)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/form/dl/dd[4]/div/input').click()
# print("登录成功")
time.sleep(3)

driver.get('https://www.wiring-world.com/home/user/points.html')
time.sleep(3)
start = int(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]').text)
# print(start)

driver.find_element(By.XPATH, '/html/body/div[5]/ul/li[1]/div[1]/a/span').click()
time.sleep(2)
end = int(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]').text)
print(end)
if 9999 <= end <= 10006: 
    driver.get(f'https://api.day.app/{bark_id}/线束商城/可以换水杯了?icon=https://pic3.zhimg.com/v2-c6daa17de7d7b7c2da126d3d9aee57c6_xll.jpg')
elif 16999 <= end <= 17006: 
    driver.get(f'https://api.day.app/{bark_id}/线束商城/可以换水壶了?icon=https://pic3.zhimg.com/v2-c6daa17de7d7b7c2da126d3d9aee57c6_xll.jpg')