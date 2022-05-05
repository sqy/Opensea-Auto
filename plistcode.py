import pickle  # 引入pickle模块 数据
import tkinter.messagebox  # 引入tkinter模块 弹窗
import sys  # 引入sys模块 解释器
import time  # 引入time模块 时间
import random  # 引入random模块 随机函数
from selenium import webdriver  # 引入selenium模块 浏览器驱动
from selenium.webdriver.common.by import By  # 定位
from selenium.webdriver.support.ui import WebDriverWait  # 等待
from selenium.webdriver.support import expected_conditions as EC  # 判断
from selenium.webdriver.common.keys import Keys

# 获取基础数据
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

# 切换浏览器窗口
def switch_window(number):
    global handles
    handles = driver.window_handles  # 获取当前页面所有的句柄
    driver.switch_to.window(handles[number])

# 配置Chrome浏览器参数
option = webdriver.ChromeOptions()
option.add_argument("--user-data-dir=" + var_chrome_path)  # 加载Chrome全部插件
#option.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
option.add_argument('--start-maximized')  # 全屏窗口

# 启动浏览器
try:
    global driver
    driver = webdriver.Chrome(chrome_options=option)  # 更改Chrome默认选项并启动
except Exception as e:  ## 需增加chrome路径不正确提示
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

# 登录部分
class Sign:
    def __init__(self):
        if sign_slice == 'start':
            self.check_zoom_level()
        if sign_slice == 'get url':
            self.get_url()
        if sign_slice == 'click account':
            self.click_account()
        if sign_slice == 'wallet check':
            self.wallet_check()
        if sign_slice == 'wallet select':
            self.wallet_select()
        if sign_slice == 'enter password':
            self.enter_password()

    #  第1步，检测浏览器缩放比例  ## 不为100%的，无法操作为100%
    def check_zoom_level(self):
        global sign_slice
        zoom_level = driver.execute_script('return (window.outerWidth/window.innerWidth)')
        # 浏览器缩放比例不为100%时发出提示并结束进程
        if zoom_level != 1:
            if var_language == 'chinese':
                tkinter.messagebox.showerror(title='', message='请调整浏览器缩放比例为100%后重新启动！')
            if var_language == 'english':
                tkinter.messagebox.showerror(title='', message='Please adjust the browser zoom to 100% and restart!')
            sys.exit()  # 终止代码
        sign_slice = 'get url'

    #  第2步，跳转opensea收藏夹页面
    def get_url(self):
        global sign_slice
        url = 'https://opensea.io/collections'
        coll = ['treer-freshness-in-memory', 'treef-concentric-tree', 'worda-chinese-characters', 'coder-random-regular-polygon', 'treer-falling-cherry-blossoms', 'mat-comic',
                'stars-starry-starry-heights']
        url_coll = "https://opensea.io/collection/" + random.choice(coll)
        driver.get(url_coll)
        try:
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath_text_coll)))  # 等待推广收藏夹打开
            time.sleep(5)  # 成功打开，等待5秒
            sign_slice = 'click account'
        except:
            driver.get(url)  # 打不开推广收藏夹的跳转正常收藏夹网址
            try:
                WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath_button_account)))  # 至少等待一个账户按钮显示
                sign_slice = 'click account'
            except:  # 账户按钮都不显示的直接报错，检查网络
                if var_language == 'chinese':
                    tkinter.messagebox.showerror(title='', message='请检查网络！')
                if var_language == 'english':
                    tkinter.messagebox.showerror(title='', message='Check your network connection!')
                sys.exit()  # 终止代码


    #  第3步，未自动跳转登录界面，点击用户来跳转登录界面
    def click_account(self):
        global sign_slice
        driver.find_element_by_xpath(xpath_button_account).click()  # 点击用户以进入登录界面
        sign_slice = 'wallet check'

    #  第4步，判定是否安装metamask钱包  ## 未找到钱包等待页面，应增加网址判定
    def wallet_check(self):
        global sign_slice
        refresh_time = 0
        while refresh_time < 3:
            try:
                WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath_text_wallet)))  # 等待钱包选择页面，Text:You need an Ethereum wallet to use OpenSea./Connect your wallet.
                time.sleep(3)
                if 'Connect your wallet' in driver.find_element_by_xpath(xpath_text_wallet).text:  # 检查正确，进行下一步
                    print('find Connect your wallet')
                    sign_slice = 'wallet select'
                    break
                elif 'You need an Ethereum wallet' in driver.find_element_by_xpath(xpath_text_wallet).text:  # 检查错误
                    time.sleep(3)  # 检查错误，追加一次等待
                    if 'Connect your wallet' in driver.find_element_by_xpath(xpath_text_wallet).text:  # 追加等待，检查正确，进行下一步
                        print('find Connect your wallet')
                        sign_slice = 'wallet select'
                        break
                    elif 'You need an Ethereum wallet' in driver.find_element_by_xpath(xpath_text_wallet).text:  # 追加等待，仍错误
                        refresh_time = refresh_time + 1
                        driver.refresh()
                        print('find You need an Ethereum wallet')
            except:
                print('no find')
                url_wallet = 'https://opensea.io/login?referrer=%2Fcollections'
                driver.get(url_wallet)  # 未找到钱包等待页面，直接跳转至选择钱包页面

        # 成功进入钱包选择页面，但刷新三次仍显示未安装钱包的报错处理
        if refresh_time == 3:
            if var_language == 'chinese':
                tkinter.messagebox.showerror(title='', message=r'请检查Metamask钱包插件是否安装正确！')
            if var_language == 'english':
                tkinter.messagebox.showerror(title='', message=r'Please check metamask wallet plug-in!')
            sys.exit()

    #  第5步，钱包选择
    def wallet_select(self):
        global sign_slice
        path_wallet_select_default = '/html/body/div[1]/div[1]/main/div/div/div/div[2]/ul/li[1]/button'
        try:
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, path_wallet_select_default)))  # 钱包选择按钮存在判定
            for i in range(4):
                path_wallet_select = '/html/body/div[1]/div[1]/main/div/div/div/div[2]/ul/li[' + str(i + 1) + ']/button'
                if 'MetaMask' in driver.find_element_by_xpath(path_wallet_select).text:
                    driver.find_element_by_xpath(path_wallet_select).click()
                    sign_slice = 'enter password'
                    break
        except:
            print('Not find path_wallet_select_default')
            sign_slice = 'wallet check'

    #  第6步，输入密码  ## 卡登录弹窗问题
    def enter_password(self):
        global sign_slice
        switch_time = 0
        while switch_time < 10:
            switch_time = switch_time + 1
            try:
                switch_window(1)  # 切换至弹出页面
                print(handles)
                driver.find_element_by_id("password").send_keys(var_metamask_password)  # 输入密码
                time.sleep(1)
                driver.find_element_by_xpath(xpath_button_unlock).click()  # 点击解锁
                time.sleep(5)
                switch_window(0)  # 切换回主页面
                sign_slice = "finish"
                break
            except:
                time.sleep(1)
                # 超10秒未弹出输入密码窗口，进行页面刷新处理
                if switch_time == 10:
                    driver.refresh()
                    sign_slice = 'wallet select'

# 尝试签名
def try_sign(s):
    print('Trying sign')
    times = 0
    while times < s:
        times += 1
        try:
            switch_window(1)
            try:
                driver.find_element_by_xpath(metamask_sign).click()  # 签名
            except:
                driver.find_element_by_xpath(metamask_sign2).click()  # 签名
            switch_window(0)
            break
        except:
            time.sleep(1)

def get_text(path):
    element = driver.find_element(By.XPATH, path)
    content = element.text
    return content

# 上传部分
class Upload:
    def __init__(self):
        try_sign(1)
        if upload_slice == 'start':
            print('slice=', upload_slice)
            self.check_start()
        if upload_slice == 'get url coll':
            print('slice=', upload_slice)
            self.get_url_coll()
        if upload_slice == 'get username coll':
            print('slice=', upload_slice)
            self.get_username_coll()
        if upload_slice == 'get link coll':
            print('slice=', upload_slice)
            self.get_link_coll()

    #  第1步，是否能正常开始的基础判定
    def check_start(self):
        global upload_slice
        try:
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath_logo_opensea)))  # 是否正常的基础判定
            upload_slice = 'get url coll'
        except:
            upload_slice = 'finish'
            print('Upload Error')

    #  第2步，跳转收藏夹地址
    def get_url_coll(self):
        global upload_slice
        url_coll = 'https://opensea.io/collections'
        driver.get(url_coll)
        upload_slice = 'get username coll'

    #  第3步，获取收藏夹用户名
    def get_username_coll(self):
        global upload_slice
        try:
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath_first_coll_by_who)))
            username = get_text(xpath_first_coll_by_who)
            if username == 'you':
                upload_slice = 'get link coll'
            else:
                driver.refresh()
                time.sleep(10)
        except:
            upload_slice = 'get url coll'
            print('get username coll Error')

    #  第4步，获取收藏夹链接  ## 如果收藏夹未加载，将获取失败，目前获取12个收藏夹
    def get_link_coll(self):
        global upload_slice
        print('var_coll_name = ', var_coll_name)
        for i in range(1, 100):
            xpath_coll_name = '/html/body/div[1]/div/main/div/div/section/div/div/div[1]/div[{}]/a/div[2]/div[3]/div'.format(i)
            try:
                collname = get_text(xpath_coll_name)
                if collname == var_coll_name:
                    xpath_coll_link = '/html/body/div[1]/div/main/div/div/section/div/div/div[1]/div[{}]/a'.format(i)
                    temp_url = driver.find_elements_by_xpath(xpath_coll_link)
                    for get_url in temp_url:
                        finish_url = str(get_url.get_attribute("href"))
                    create_url = '{}/assets/create'.format(finish_url)
                    driver.get(create_url)
                    upload_slice = 'finish'
                    break
            except:
                print('Not find the name of collection')
                break




# 元素地址
# 登录界面
global xpath_button_account, xpath_text_coll, xpath_text_wallet, xpath_button_unlock
xpath_button_account = '/html/body/div[1]/div[1]/div[1]/nav/ul/div/div/li/a'
xpath_text_coll = '/html/body/div[1]/div/main/div/div/div[2]/div[2]/div[3]/h2'
xpath_text_wallet = '/html/body/div[1]/div/main/div/div/h1'
xpath_button_unlock = '/html/body/div[1]/div/div[2]/div/div/button'

#
global xpath_logo_opensea, xpath_first_coll_by_who
xpath_logo_opensea = '/html/body/div[1]/div/div[1]/nav/div[1]/a'
xpath_first_coll_by_who = '/html/body/div[1]/div/main/div/div/section/div/div/div[1]/div[1]/a/div[2]/div[4]/div/a/span'

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

# 主程序
if __name__ == "__main__":
    # 成功启动浏览器，配置参数
    global sign_slice
    sign_slice = 'start'  # 默认登陆操作第1步

    # 登录操作
    while sign_slice != "finish":
        try:
            Sign()  # 登录操作步骤
        except:
            print("sign_slice=", sign_slice, ", Sign Error")

    # 成功登录，配置参数
    global upload_slice
    upload_slice = 'start'
    while upload_slice != "finish":
        try:
            Upload()  # 上传操作步骤
        except:
            print("upload_slice=", upload_slice, ", Upload Error")

    print('finish')