from selenium import webdriver  # 引入selenium模块
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from PIL import Image  # 引入pillow模块
import xlrd   # 引入Excel读取模块
from xlutils.copy import copy  # 导入copy模块
import time
import os
import pickle

#获取数据
fileread = open('dataFile.txt', 'rb')  # 打开数据文件
datalist_rb = pickle.load(fileread)  # 读取数据
plug_path = datalist_rb[1]
metamask_password = datalist_rb[2]
metamask_password_choice = datalist_rb[3]

# 启用带插件的浏览器
url = r"https://opensea.io/login?referrer=%2Faccount"
option = webdriver.ChromeOptions()
option.add_argument("--user-data-dir=" + plug_path)  # 加载Chrome全部插件
option.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
option.add_argument('--start-maximized')  # 全屏窗口
driver = webdriver.Chrome(chrome_options=option)  # 更改Chrome默认选项
# 登录
driver.get(url)  # 设置打开网页
try:
    print('1')
    sign_in_button = '//*[@id="main"]/div/div/div/div[2]/ul/li[1]/a/div[2]'
    print('2')
    WebDriverWait(driver, 60, 0.5).until(EC.presence_of_element_located((By.XPATH, sign_in_button)))
    print('3')
    text = driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div/div/h1').text
    print('4')
    print(text)
    #WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, 'You need an Ethereum wallet to use OpenSea.'))).send_keys(Keys.CONTROL + '0')
    print('find')
except:
    print('nothing')
    #'/html/body/div[1]/div[1]/main/div/div/h1'
    #'/html/body/div[1]/div[1]/main/div/div/h1'

def sign_in():
    driver.get(url)  # 设置打开网页
    while True:
        try:
            WebDriverWait(driver, 60, 0.5).until(EC.presence_of_element_located((By.XPATH, sign_in_button))).send_keys(Keys.CONTROL + '0')
            driver.find_element_by_xpath(sign_in_button).click()  # 点击登录键
            break
        except:
            driver.refresh()
    while True:
        try:
            change_window(1)  # 切换至弹出页面
            driver.find_element_by_id("password").send_keys(password_metamask)  # 输入密码
            try:
                driver.find_element_by_xpath(sign_in_unlock).click()  # 点确定
            except:
                driver.find_element_by_xpath(sign_in_unlock2).click()  # 点确定
            change_window(0)  # 切换回主页面
            break
        except:
            time.sleep(1)