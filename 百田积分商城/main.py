#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import datetime
import sys

bark_id = '填入你的bark id'

def myjob(id):
    button = driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[3]/div/div[2]/div[{id}]/div[3]')
    print(f"开始做任务{id}")
    driver.execute_script("$(arguments[0]).click()",button)
    time.sleep(45)
    driver.get('http://www.100bt.com/m/creditMall/?gameId=2#task')
    time.sleep(10)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')

print("-----脚本开始执行-----")
print(f"日期：{datetime.date.today()}")

driver = webdriver.Chrome(chrome_options=options)
driver.get('http://www.100bt.com/m/creditMall/?gameId=2#user')

driver.delete_all_cookies()
with open(f'/root/aola/cookies/{sys.argv[1]}','r') as f:
    cookies_list = json.load(f)
    for cookie in cookies_list:
        driver.add_cookie(cookie)

driver.refresh()
driver.get('http://www.100bt.com/m/creditMall/?gameId=2#task')
time.sleep(10)

user = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/span[1]')
remain = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/span[2]')

if(user.text == '登录有礼'): 
    driver.get(f'https://api.day.app/{bark_id}/积分商城任务/{sys.argv[1]}失效?icon=https://tse4-mm.cn.bing.net/th/id/OIP-C.eN-WxekffTLkN-wkuxiudAHaHa')
    exit(0)
    
name = user.text
remain1 = remain.text

print("执行用户:"+name)
print("开始"+remain1)

# 完成任务1
try: myjob(1)
except: pass

# 完成任务2
try: myjob(2)
except: pass

# 完成任务3
try: myjob(3)
except: pass

# 完成任务4
try: myjob(4)
except: pass

# 完成任务5
try: myjob(5)
except: pass

# 完成任务6
try: myjob(6)
except: pass

# 获取余额
driver.get('http://www.100bt.com/m/creditMall/?gameId=2#task')
time.sleep(10)
remain = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/span[2]')
remain2 = remain.text
print(remain2)

driver.get(f'https://api.day.app/{bark_id}/积分商城任务完成/账号: {name} | {remain2}?icon=https://tse4-mm.cn.bing.net/th/id/OIP-C.eN-WxekffTLkN-wkuxiudAHaHa')
time.sleep(10)

print("-----脚本执行完毕-----")
driver.close()