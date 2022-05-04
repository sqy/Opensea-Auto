from selenium import webdriver  # 引入selenium模块
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from PIL import Image  # 引入pillow模块
import xlrd   # 引入Excel读取模块
from xlutils.copy import copy  # 导入copy模块
import random
import sys
import time
import os
import pickle
import tkinter as tk
import tkinter.messagebox

# 获取数据
fileread = open('dataFile.txt', 'rb')  # 打开数据文件
datalist_rb = pickle.load(fileread)  # 读取数据
var_language = datalist_rb[1]
var_chrome_path = datalist_rb[2]
var_metamask_password = datalist_rb[3]
var_password_choice = datalist_rb[4]
var_nft_path = datalist_rb[5]
var_coll_name = datalist_rb[6]
var_nft_name = datalist_rb[7]
var_nft_number = datalist_rb[8]
var_add_number = datalist_rb[9]
var_name_suffix = datalist_rb[10]
var_no_number = datalist_rb[11]
var_nft_price = datalist_rb[12]
var_first = datalist_rb[13]
var_blockchain = datalist_rb[14]

# 切换页面
def switch_window(number):
    global handles
    handles = driver.window_handles  # 获取当前页面所有的句柄
    driver.switch_to.window(handles[number])

# 配置Chrome浏览器参数
option = webdriver.ChromeOptions()
option.add_argument("--user-data-dir=" + var_chrome_path)  # 加载Chrome全部插件
option.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
option.add_argument('--start-maximized')  # 全屏窗口

# 启动浏览器
try:
    global driver
    driver = webdriver.Chrome(chrome_options=option)  # 更改Chrome默认选项并启动
except Exception as e:
    # 未安装chromedriver
    if r"'chromedriver' executable needs to be in PATH" in repr(e):
        if var_language == 'chinese':
            tkinter.messagebox.showerror(title='', message=r"请正确配置'chromedriver'到路径中")
        if var_language == 'english':
            tkinter.messagebox.showerror(title='', message=r"'chromedriver' executable needs to be in PATH")
    # 需更新chromedriver
    elif r"This version of ChromeDriver only supports Chrome version" in repr(e):
        if var_language == 'chinese':
            tkinter.messagebox.showerror(title='', message=r"请更新'chromedriver'以支持目前Chrome版本")
        if var_language == 'english':
            tkinter.messagebox.showerror(title='', message=r"Please update 'chromedriver' to support the current version of Chrome")
    # 启动时存在Chrome浏览器未关闭或其它原因
    elif r"Chrome failed to start: crashed." in repr(e):
        if var_language == 'chinese':
            tkinter.messagebox.showerror(title='', message=r'启动浏览器出错，请在启动前关闭Chrome浏览器！')
        if var_language == 'english':
            tkinter.messagebox.showerror(title='', message=r'Error starting browser, please close Chrome browser before starting!')
    # 未知原因
    else:
        if var_language == 'chinese':
            tkinter.messagebox.showerror(title='', message=r'未知错误！')
        if var_language == 'english':
            tkinter.messagebox.showerror(title='', message=r'Unknown Error!')
    sys.exit()  # 终止代码

sign_slice = 1
sys_exit = 0
# 登录部分
class Sign:
    def __init__(self):
        print('slice=',sign_slice)
        if sign_slice == 1:
            self.check_zoom_level()
        if sign_slice == 2:
            self.get_url()
        if sign_slice == 3:
            self.click_account()
        if sign_slice == 4:
            self.wallet_select()
        if sign_slice == 5:
            self.enter_password()

    #  第1步，检测浏览器缩放比例
    def check_zoom_level(self):
        global zoom_level, sys_exit
        zoom_level = driver.execute_script('return (window.outerWidth/window.innerWidth)')
        # 浏览器缩放比例不为100%时发出提示并结束进程
        if zoom_level != 1:
            if var_language == 'chinese':
                tkinter.messagebox.showerror(title='', message='请调整浏览器缩放比例为100%后重新启动！')
            if var_language == 'english':
                tkinter.messagebox.showerror(title='', message='Please adjust the browser zoom to 100% and restart!')
            # 结束进程
            sys_exit = 1

    #  第2步，跳转opensea收藏夹页面
    def get_url(self):
        coll = ['treer-freshness-in-memory', 'treef-concentric-tree', 'worda-chinese-characters', 'coder-random-regular-polygon', 'treer-falling-cherry-blossoms', 'mat-comic',
                'stars-starry-starry-heights']
        url_coll = "https://opensea.io/collection/" + random.choice(coll)
        driver.get(url_coll)

    #  第3步，未自动跳转登录界面，点击用户来跳转登录界面
    def click_account(self):
        driver.find_element_by_xpath(xpath_button_account).click()  # 点击用户以进入登录界面
        time.sleep(3)

    #  第4步，钱包选择
    def wallet_select(self):
        for i in range(4):
            path_wallet_select = '/html/body/div[1]/div[1]/main/div/div/div/div[2]/ul/li[' + str(i + 1) + ']/button'
            if 'MetaMask' in driver.find_element_by_xpath(path_wallet_select).text:
                driver.find_element_by_xpath(path_wallet_select).click()
                break

    #  第5步，输入密码
    def enter_password(self):
        while True:
            try:
                switch_window(1)  # 切换至弹出页面
                print(handles)
                driver.find_element_by_id("password").send_keys(var_metamask_password)  # 输入密码
                time.sleep(180)
                driver.find_element_by_xpath(button_unlock).click()  # 点击解锁
                switch_window(0)  # 切换回主页面
                break
            except:
                time.sleep(1)

def step_sign():
    global sign_slice, sys_exit
    if sign_slice == 2:
        try:
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath_text_coll)))
    elif  sign_slice == 3:
        try:
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath_text_wallet)))  # 等待钱包选择页面，Text:You need an Ethereum wallet to use OpenSea./Connect your wallet.
            time.sleep(3)
            if 'You need an Ethereum wallet' in driver.find_element_by_xpath(xpath_text_wallet).text:
                if sign_slice == 3:
                    if var_language == 'chinese':
                        tkinter.messagebox.showerror(title='', message=r'请安装Metamask钱包插件或检查Chrome浏览器个人资料路径！')
                    if var_language == 'english':
                        tkinter.messagebox.showerror(title='', message=r'Please install metamask wallet plug-in or check Chrome Profile path!')
                    # 结束进程
                    sys_exit = 1
                sign_slice = 3
                print('find You need an Ethereum wallet')
            elif 'Connect your wallet' in driver.find_element_by_xpath(xpath_text_wallet).text:
                sign_slice = 4
                print('find Connect your wallet')
        except:
            print('no find')
            driver.refresh()
    else:
        sign_slice = sign_slice + 1
    print('+slice=', sign_slice)

def check_sign_error():
    print(r"I'm writing")

def sign_in():
    while sign_slice < 6:
        try:
            Sign()  # 登录操作步骤
            # 结束循环
            if sys_exit == 1:
                break
            # 完成每步操作后对情况判定
            step_sign()
        except:
            check_sign_error()
    # 在结束循环后终止代码
    if sys_exit == 1:
        sys.exit()  # 终止代码

# 登录
def open_web():
    driver.get(url_coll)  # 设置打开网页
    try:
        WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located((By.XPATH, ))).click()  # 点击用户以进入登录界面
        try:
            WebDriverWait(driver, 60, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/main/div/div/div/div[2]/ul/li[1]/button')))
            for i in range(4):
                path_wallet_select = '/html/body/div[1]/div[1]/main/div/div/div/div[2]/ul/li[' + str(i + 1) + ']/button'
                if 'MetaMask' in driver.find_element_by_xpath(path_wallet_select).text:
                    driver.find_element_by_xpath(path_wallet_select).click()
                    break
        except:
            print('Wallet button select not found')
    except:
        print('Account button not found')

#open_web()



#driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/nav/div[2]/div/div/div/input').send_keys(Keys.CONTROL + '0')

def sign_in123():
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

if __name__ == "__main__":
    global xpath_button_account, xpath_text_coll, xpath_text_wallet, button_unlock
    xpath_button_account = '/html/body/div[1]/div[1]/div[1]/nav/ul/div/div/li/a'
    xpath_text_coll = '/html/body/div[1]/div/main/div/div/div[2]/div[2]/div[3]/h2'
    xpath_text_wallet = '/html/body/div[1]/div/main/div/div/h1'
    button_unlock = '/html/body/div[1]/div/div[2]/div/div/button'

    global sign_in_button, sign_in_unlock, sign_in_unlock2, opensea_path, metamask_sign, metamask_sign2
    sign_in_button = '//*[@id="__next"]/div[1]/main/div/div/div/div[2]/ul/li[1]/button'

    sign_in_unlock2 = '/html/body/div[1]/div/div[2]/div/div/button'
    opensea_path = '//*[@id="__next"]/div[1]/div[1]/nav/div[1]/a'
    metamask_sign = '/html/body/div[1]/div/div[2]/div/div[3]/button[2]'
    metamask_sign2 = '/html/body/div[1]/div/div[3]/div/div[3]/button[2]'
    global inputpic_path, names_path, descs_path, prop_switch_path, prop_type_path, prop_name_path, prop_save_path, lockcontent_switch_path, lockcontent_path, create_path
    inputpic_path = '//*[@id="media"]'
    names_path = '//*[@id="name"]'
    descs_path = '//*[@id="description"]'
    prop_switch_path = '//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/section/div[1]/div/div[2]/button'
    prop_type_path = '/html/body/div[2]/div/div/div/section/table/tbody/tr/td[1]/div/div/input'
    prop_name_path = '/html/body/div[2]/div/div/div/section/table/tbody/tr/td[2]/div/div/input'
    prop_save_path = '/html/body/div[2]/div/div/div/footer/button'
    lockcontent_switch_path = '//*[@id="unlockable-content-toggle"]'
    lockcontent_path = '//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/section/div[4]/div[2]/textarea'
    create_path = '/html/body/div[1]/div[1]/main/div/div/section/div[2]/form/div[9]/div[1]/span/button'
    global created_close_path, sellbutton_text, lowerprice_path
    created_close_path = '/html/body/div[5]/div/div/div/div[2]/button/i'  # 确定用link_text 'close' 无效
    sellbutton_text = 'Sell'
    lowerprice_path = '//*[@id="__next"]/div[1]/main/div/div/div[1]/div/button[2]'
    global price_path, plist_path, listitem_path, viewitem_path
    price_path = '/html/body/div[1]/div[1]/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[2]/div/div[2]/div/div/div[2]/input'
    plist_path = '/html/body/div[1]/div[1]/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[6]/button'
    listitem_path = '/html/body/div[4]/div/div/div/header/h4'
    viewitem_path = '/html/body/div[4]/div/div/div/footer/a'

    sign_in()
    print('111')
