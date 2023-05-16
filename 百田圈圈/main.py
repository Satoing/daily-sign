from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import datetime
import sys

bark_id = '你的bark id'

uname = '多多号'
pword = '密码'

if len(sys.argv) > 1:
    uname = sys.argv[1]
    pword = sys.argv[2]

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
# options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(chrome_options=options)

driver.get('http://qq.100bt.com/')
time.sleep(5)
element = driver.find_element(By.XPATH, '//*[@id="iCounter"]/a')
driver.execute_script("arguments[0].click()", element)

# 登录
# ---------------------------------------------------------------------
#定位到iframe
iframe=driver.find_element(By.CSS_SELECTOR, ".baitianCommonLoginIframe")
#句柄切换进iframe
driver.switch_to.frame(iframe)

driver.find_element(By.XPATH, '//*[@id="login_duoduoid"]').send_keys(uname)
driver.find_element(By.XPATH, '//*[@id="login_password"]').send_keys(pword)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[3]/div[2]/input').click()
time.sleep(5)

driver.get('http://qq.100bt.com/topic-106326485-1.html')
time.sleep(5)

start = int(driver.find_element(By.XPATH, '//*[@id="haslogin"]/dl/dd[1]/div/a[2]/span').text)
print(f"开始有{start}圈币")

# 帖子评论3次
# ----------------------------------------------------------
# print("开始评论")
def send_msg(url):
    # print(f"评论1次")
    #定位到iframe
    iframe=driver.find_element(By.CSS_SELECTOR, "#ueditor_2")
    #句柄切换进iframe
    driver.switch_to.frame(iframe)
    driver.find_element(By.XPATH, '/html/body').send_keys("顶顶")
    driver.switch_to.default_content()
    e = driver.find_element(By.XPATH, '//*[@id="sl-Topic"]/div[7]/div/div[2]/a[1]')
    driver.execute_script("arguments[0].click()", e)
    time.sleep(60)

for i in range(3): 
    if i == 0: send_msg('http://qq.100bt.com/topic-106326485-1.html')
    elif i == 1: send_msg('http://qq.100bt.com/topic-25647126-1.html')
    elif i == 2: send_msg('http://qq.100bt.com/topic-106326485-1.html')
time.sleep(5700)

# 在线奖励90分钟领取
# ----------------------------------------------------
def reward(id):
    reward = 0
    if id == 10: reward = 1
    elif id == 30: reward = 2
    elif id == 50: reward = 3
    elif id == 90: reward = 5
    driver.get('http://qq.100bt.com/topic-106326485-1.html')
    time.sleep(6)
    e = driver.find_element(By.CSS_SELECTOR, f".getOnlineReward{id}")
    driver.execute_script("arguments[0].click()", e)
    print(f"获得了{reward}积分")
    time.sleep(5)

times = [10, 30, 50, 90]
for t in times: reward(t)

# 帖子分享
# ---------------------------------------------
def share(id):
    driver.get('http://qq.100bt.com/13/')
    time.sleep(5)
    driver.find_element(By.XPATH, f'//*[@id="main"]/div[4]/div/div[1]/div[1]/table/tbody/tr[{id}]/td[2]/a').click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH, '//*[@id="st-Content"]/div[1]/div/div[4]/div[1]/a').click()
    driver.close()
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
for i in range(5): share(6+i)

# 4个圈子签到
# ---------------------------------------------------
quans = [231, 12, 13, 17]
for quan in quans:
    driver.get(f'http://qq.100bt.com/{quan}')
    time.sleep(5)
    e = driver.find_element(By.CSS_SELECTOR, '#rg-signUp div')
    driver.execute_script("arguments[0].click()", e)

# 统计并推送
# --------------------------------------------------
end = int(driver.find_element(By.XPATH, '//*[@id="haslogin"]/dl/dd[1]/div/a[2]/span').text)
if len(sys.argv) == 1: driver.get(f'https://api.day.app/{bark_id}/百田圈圈/领取到{end-start}圈币，当前余额为{end}?icon=https://tse4-mm.cn.bing.net/th/id/OIP-C.eN-WxekffTLkN-wkuxiudAHaHa')
time.sleep(5)