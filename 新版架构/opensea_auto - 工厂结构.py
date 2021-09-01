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

# 启用带插件的浏览器
#plug_path = r"C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/"
plug_path = r"C:/Users/Suqing/AppData/Local/Google/Chrome/User Data/"
#plug_path = r"C:/Users/mayn/AppData/Local/Google/Chrome/User Data/"
url = r"https://opensea.io/collections"
option = webdriver.ChromeOptions()
option.add_argument("--user-data-dir="+plug_path)  # 加载Chrome全部插件
option.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
option.add_argument('--start-maximized')         # 全屏窗口
driver = webdriver.Chrome(chrome_options=option)  # 更改Chrome默认选项

class General:
    def change_window(self, number):
        handles = driver.window_handles  # 获取当前页面所有的句柄
        driver.switch_to.window(handles[number])
    def try_sign(self, times):
        for i in range(1, times + 1):
            try:
                self.change_window(1)  # 切换至弹出页面
                driver.find_element_by_id("password").send_keys(password_metamask)  # 输入密码
                driver.find_element_by_xpath(sign_in_unlock).click()  # 点确定
                self.change_window(0)  # 切换回主页面
                break
            except:
                time.sleep(1)
    def try_sign_True(self):
        while True:
            try:
                self.change_window(1)  # 切换至弹出页面
                driver.find_element_by_id("password").send_keys(password_metamask)  # 输入密码
                driver.find_element_by_xpath(sign_in_unlock).click()  # 点确定
                self.change_window(0)  # 切换回主页面
                break
            except:
                time.sleep(1)
Gen = General()
class Check:
    def collection(self, coll):
        while True:
            try:
                WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, coll)))  # 框
                try:
                    driver.find_element_by_link_text("Suqingyan")
                    break
                except:
                    driver.find_element_by_xpath(opensea_path).click()  # 点击Opeasea
                    try:
                        WebDriverWait(driver, 60, 0.5).until(EC.presence_of_element_located((By.XPATH, homecreate_path)))
                        driver.find_element_by_xpath(homecreate_path).click()  # 点击首页Create
                    except:
                        driver.get(url)
            except:
                driver.get(url)
Check = Check()

class Prepare:
    def sign_in_metamask(self):
        driver.get(url)
        while True:
            try:
                WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, sign_in_button)))
                driver.find_element_by_xpath(sign_in_button).click()  # 点击登录键
                break
            except:
                driver.refresh()
        while True:
            try:
                Gen.change_window(1)  # 切换至弹出页面
                driver.find_element_by_id("password").send_keys(password_metamask)  # 输入密码
                driver.find_element_by_xpath(sign_in_unlock).click()  # 点确定
                Gen.change_window(0)  # 切换回主页面
                break
            except:
                time.sleep(1)
    def sign_in(coll_num):


        driver.get(url)  # 设置打开网页
        sign_in_metamask()
        check_coll()
        global add_item_url
        coll = '//*[@id="__next"]/div[1]/main/div/div/section/div/div/div[1]/div[' + str(coll_num) + ']/a'
        coll_url = driver.find_elements_by_xpath(coll)
        for get_url in coll_url:
            add_item_url = str(get_url.get_attribute("href")) + '/assets/create'


if __name__ == "__main__":
    global sign_in_button, sign_in_unlock, opensea_path, homecreate_path
    sign_in_button = '//*[@id="__next"]/div[1]/main/div/div/div/div[1]/div[2]/button'
    sign_in_unlock = '//*[@id="app-content"]/div/div[3]/div/div/button/span'
    opensea_path = '//*[@id="__next"]/div[1]/div[1]/nav/div[1]/a'
    homecreate_path = '//*[@id="__next"]/div[1]/main/div/div/div[1]/div[2]/div[1]/div[1]/a'
    global inputpic_path, names_path, descs_path, prop_switch_path, prop_type_path, prop_name_path, prop_save_path, lockcontent_switch_path, lockcontent_path
    inputpic_path = '//*[@id="media"]'
    names_path = '//*[@id="name"]'
    descs_path = '//*[@id="description"]'
    prop_switch_path = '//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/section[6]/div[1]/div/div[2]/button'
    prop_type_path = '/html/body/div[2]/div/div/div/section/table/tbody/tr/td[1]/div/div/input'
    prop_name_path = '/html/body/div[2]/div/div/div/section/table/tbody/tr/td[2]/div/div/input'
    prop_save_path = '/html/body/div[2]/div/div/div/footer/button'
    lockcontent_switch_path = '//*[@id="unlockable-content-toggle"]'
    lockcontent_path = '//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/section[6]/div[4]/div[2]/textarea'
    global password_metamask
    password_metamask = r"elysion0922"