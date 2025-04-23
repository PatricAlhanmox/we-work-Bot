import requests, time, test_funset
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

url = 'https://www.jiandaoyun.com/signin'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0'
}
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificates-errors')
options.add_experimental_option("excludeSwitches",['enable-automation'])
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
response = driver.get(url)

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[3]/div[4]/div[2]/div[3]"))
).click()

time.sleep(2)
try:
    iframe = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[2]/div[2]/div/iframe")
    driver.switch_to.frame(iframe)
    print("已切换到弹层iframe上下文")
except:
    print('无iframe')  # 无iframe则继续

ele = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='__nuxt']/div/div/section/div/img"))
)
img_url = ele.get_attribute("src")
img_data = requests.get(img_url).content
with open("./img.jpg", 'wb') as f:
    f.write(img_data)
f.close()

#test_funset.send_pic()
# 登陆后
time.sleep(30)
driver.get('https://www.jiandaoyun.com/dashboard#/')
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div/div/div[4]/div/div/div/div[1]/div[2]/div/div/input"))
).send_keys('中国民用航空飞行学院飞行放行单')

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div/div/div[4]/div/div/div/div[1]/div[2]/ul/li/div/span/mark"))
).click()

# 点击选择数据
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div/div/div[4]/div/div/div/div[1]/div[2]/ul/li/div/span/mark'))
).click()

time.sleep(2)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div'))
).click()
