#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import datetime
import sys

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options=options)

uname = '你的账号'
pword = '你的密码'

driver.get('https://www.xmy365.com/user/login')
driver.maximize_window()
time.sleep(3)

print("开始登录")
driver.find_element(By.XPATH, '//*[@id="myform"]/div[1]/p[2]/input').send_keys(uname)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(pword)
driver.find_element(By.XPATH, '//*[@id="myform"]/div[5]/button').click()
print("登录成功")

time.sleep(3)
driver.get('https://www.xmy365.com/point/pointStore?show=6')
time.sleep(3)

# print(driver.execute_script("return document.documentElement.outerHTML"))
# start = int(driver.find_element(By.XPATH, '//*[@id="accPoints"]').text)
# print(start)
element = driver.find_element(By.XPATH, '//*[@id="sign"]')
driver.execute_script("arguments[0].click()", element)
# time.sleep(2)
# end = int(driver.find_element(By.XPATH, '//*[@id="accPoints"]').text)
# print(end)
# if(end >= 1300): pass