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
import os

# 获取基础数据
fileread = open('dataFile.txt', 'rb')  # 打开数据文件
datalist_rb = pickle.load(fileread)  # 读取数据
var_language = datalist_rb[1]
var_chrome_path = datalist_rb[2]  # 配置Chrome浏览器参数调用
var_metamask_password = datalist_rb[3]  # Sign，第6步调用
var_password_choice = datalist_rb[4]
var_nft_path = datalist_rb[5]  # Upload_prepare，第5步调用
var_coll_name = datalist_rb[6]  # Upload_prepare，第4步调用
var_nft_name = datalist_rb[7]  # Fill，第2步调用
var_nft_number = datalist_rb[8]  # Fill，第2步调用
var_add_number = datalist_rb[9]
var_name_suffix = datalist_rb[10]  # Fill，第2步调用
var_no_number = datalist_rb[11]
var_nft_price = datalist_rb[12]
var_first = datalist_rb[13]
var_blockchain = datalist_rb[14]  # Fill，第9步调用
var_supply = datalist_rb[15]  # Fill，第9步调用

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
        elif sign_slice == 'get url':
            self.get_url()
        elif sign_slice == 'click account':
            self.click_account()
        elif sign_slice == 'wallet check':
            self.wallet_check()
        elif sign_slice == 'wallet select':
            self.wallet_select()
        elif sign_slice == 'enter password':
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
    times = 0
    while times < s:
        times += 1
        try:
            switch_window(1)
            try:
                driver.find_element_by_xpath(metamask_sign).click()  # 签名
            except:
                print('Not find sign name button')
            switch_window(0)
            break
        except:
            time.sleep(1)

# 获取元素文本内容
def get_text(xpath):
    element = driver.find_element(By.XPATH, xpath)
    content = element.text
    return content

# 获取元素链接
def get_href(xpath):
    temp_url = driver.find_elements_by_xpath(xpath)
    for get_url in temp_url:
        finish_url = str(get_url.get_attribute("href"))
    return finish_url

# 获取目录文件夹内的全部文件拼装绝对路径
def get_files_path(path):
    listdir = os.listdir(path)  # 定位文件夹位置
    #filepath = os.getcwd()  # 当前工作目录
    allfile = []  # 定义为数组
    for file in listdir:
        #allfile.append(filepath + '\\' + path + '\\' + file)  # 拼装地址
        allfile.append(path + '/' + file)  # 拼装地址
    return allfile

# 准备上传部分
class Upload_prepare:
    def __init__(self):
        try_sign(1)
        if upload_prepare_slice == 'start':
            self.check_start()
        elif upload_prepare_slice == 'get url coll':
            self.get_url_coll()
        elif upload_prepare_slice == 'get username coll':
            self.get_username_coll()
        elif upload_prepare_slice == 'get link coll':
            self.get_link_coll()
        elif upload_prepare_slice == 'get item path':
            self.get_item_path()

    #  第1步，是否能正常开始的基础判定
    def check_start(self):
        global upload_prepare_slice
        try:
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath_logo_opensea)))  # 是否正常的基础判定
            upload_prepare_slice = 'get url coll'
        except:
            upload_prepare_slice = 'finish'
            print('Upload Error')

    #  第2步，跳转收藏夹地址
    def get_url_coll(self):
        global upload_prepare_slice
        url_coll = 'https://opensea.io/collections'
        driver.get(url_coll)
        upload_prepare_slice = 'get username coll'

    #  第3步，获取收藏夹用户名
    def get_username_coll(self):
        global upload_prepare_slice
        try:
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath_first_coll_by_who)))
            username = get_text(xpath_first_coll_by_who)
            if username == 'you':
                upload_prepare_slice = 'get link coll'
            else:
                driver.refresh()
                time.sleep(10)
        except:
            upload_prepare_slice = 'get url coll'
            print('get username coll Error')

    #  第4步，获取收藏夹链接  ## 如果收藏夹未加载，将获取失败，目前获取12个收藏夹
    def get_link_coll(self):
        global upload_prepare_slice, create_url
        for i in range(1, 100):
            xpath_coll_name = '/html/body/div[1]/div/main/div/div/section/div/div/div[1]/div[{}]/a/div[2]/div[3]/div'.format(i)  # 拼装收藏夹名字元素地址
            try:
                collname = get_text(xpath_coll_name)
                if collname == var_coll_name:
                    xpath_coll_link = '/html/body/div[1]/div/main/div/div/section/div/div/div[1]/div[{}]/a'.format(i)  # 拼装收藏夹链接元素地址
                    temp_url = get_href(xpath_coll_link)  # 获取元素链接
                    create_url = '{}/assets/create'.format(temp_url)  # 增加对应收藏夹Add Item页面链接的后缀
                    driver.get(create_url)  # 跳转Add Item界面
                    upload_prepare_slice = 'get item path'
                    break
            except:
                print('Not find the name of collection')
                break

    #  第5步，获取收藏夹链接  ## 如果收藏夹未加载，将获取失败，目前获取12个收藏夹
    def get_item_path(self):
        global upload_prepare_slice, path_items
        path_items = get_files_path(var_nft_path)
        upload_prepare_slice = 'finish'

class Fill:
    def __init__(self, path_item):
        try_sign(1)
        if fill_slice == 'upload item':
            print('fill_slice=', fill_slice)
            self.upload_item(path_item)
        elif fill_slice == 'item name':
            print('fill_slice=', fill_slice)
            self.item_name()
        elif fill_slice == 'item description':
            print('fill_slice=', fill_slice)
            self.item_description()
        elif fill_slice == 'item properties':
            print('fill_slice=', fill_slice)
            self.item_properties()
        elif fill_slice == 'item levels':
            print('fill_slice=', fill_slice)
            self.item_levels()
        elif fill_slice == 'item stats':
            print('fill_slice=', fill_slice)
            self.item_stats()
        elif fill_slice == 'item content':
            print('fill_slice=', fill_slice)
            self.item_content()
        elif fill_slice == 'item sensitive':
            print('fill_slice=', fill_slice)
            self.item_sensitive()
        elif fill_slice == 'item blockchain':
            print('fill_slice=', fill_slice)
            self.item_blockchain()
        elif fill_slice == 'item create':
            print('fill_slice=', fill_slice)
            self.item_create()


    #  第1步，上传项目
    def upload_item(self, path_item):
        global fill_slice
        try:
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath_item_input)))  # 新步骤基础判定元素是否存在
            print('Find item input')
            driver.find_element_by_xpath(xpath_item_input).send_keys(path_item)  # 上传Item
            fill_slice = 'item name'  # 进行下一步
        except:
            print('upload_item Error')
            driver.get(create_url)  # 跳转Add Item界面
            time.sleep(1)
            try_sign(1)

    #  第2步，填入名称  ## 名称拼装功能及判定，以及全部完成后写入pickle功能
    def item_name(self):
        global fill_slice
        print('var_name_suffix = ', var_name_suffix)
        if var_name_suffix == 1 :
            name_input = '{} #{}'.format(var_nft_name, var_nft_number)
            driver.find_element_by_xpath(names_path).send_keys(name_input)  # 填入Item名称
        else:
            driver.find_element_by_xpath(names_path).send_keys(var_nft_name)  # 填入Item名称
        fill_slice = 'item blockchain'

    #  第3步，填入描述
    def item_description(self):
        global fill_slice
        print("I'll write code")

    #  第4步，填入属性，矩形的文本特征
    def item_properties(self):
        global fill_slice
        print("I'll write code")

    #  第5步，填入等级，进度条的数字特征
    def item_levels(self):
        global fill_slice
        print("I'll write code")

    #  第6步，填入统计数据，数字形式显示的数字特征
    def item_stats(self):
        global fill_slice
        print("I'll write code")

    #  第7步，可解锁内容
    def item_content(self):
        global fill_slice
        print("I'll write code")

    #  第8步，敏感内容
    def item_sensitive(self):
        global fill_slice
        print("I'll write code")

    #  第9步，块链选择
    def item_blockchain(self):
        global fill_slice
        # var_blockchain目前有'Ethereum'和'Polygon'
        driver.execute_script("window.scrollTo(0,1800);")  # 拖滚动条下移，防止界面找不到元素
        element = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/section/div[2]/form/div[7]/div/div[2]/input')
        var_element = element.get_attribute('value')
        if var_blockchain == var_element:
            print('The blockchain is same')
            time.sleep(1200)
        else:
            print('Fuck')
            # 展开选项
            xpath_blockchain_showmore = '/html/body/div[1]/div/main/div/div/section/div[2]/form/div[7]/div/div[2]/div[2]/i'
            driver.find_element_by_xpath(xpath_blockchain_showmore).click()
            # 匹配选项
            xpath_blockchain_logo1 = '/html/body/div[1]/div/main/div/div/section/div[2]/form/div[7]/div/div[3]/div/div/div/ul/li[1]/button/div[2]/span[1]'  # logo1
            xpath_blockchain_logo2 = '/html/body/div[1]/div/main/div/div/section/div[2]/form/div[7]/div/div[3]/div/div/div/ul/li[2]/button/div[2]/span[1]'  # logo2
            xpath_blockchain_logo3 = '/html/body/div[1]/div/main/div/div/section/div[2]/form/div[7]/div/div[3]/div/div/div/ul/li[3]/button/div[2]/span[1]'  # logo3
            if var_blockchain == get_text(xpath_blockchain_logo1):
                driver.find_element_by_xpath(xpath_blockchain_logo1).click()
            elif var_blockchain == get_text(xpath_blockchain_logo2):
                driver.find_element_by_xpath(xpath_blockchain_logo2).click()
            elif var_blockchain == get_text(xpath_blockchain_logo3):
                driver.find_element_by_xpath(xpath_blockchain_logo3).click()
            time.sleep(1200)




    #  第10步，点击创建和判定
    def item_create(self):
        global fill_slice
        print("I'll write code")


# 元素地址
# 登录界面
global xpath_button_account, xpath_text_coll, xpath_text_wallet, xpath_button_unlock
xpath_button_account = '/html/body/div[1]/div[1]/div[1]/nav/ul/div/div/li/a'
xpath_text_coll = '/html/body/div[1]/div/main/div/div/div[2]/div[2]/div[3]/h2'
xpath_text_wallet = '/html/body/div[1]/div/main/div/div/h1'
xpath_button_unlock = '/html/body/div[1]/div/div[2]/div/div/button'

# 准备上传操作
global xpath_logo_opensea, xpath_first_coll_by_who
xpath_logo_opensea = '/html/body/div[1]/div/div[1]/nav/div[1]/a'
xpath_first_coll_by_who = '/html/body/div[1]/div/main/div/div/section/div/div/div[1]/div[1]/a/div[2]/div[4]/div/a/span'

global sign_in_button, sign_in_unlock, opensea_path, metamask_sign, metamask_sign2
sign_in_button = '//*[@id="__next"]/div[1]/main/div/div/div/div[2]/ul/li[1]/button'
sign_in_unlock = '/html/body/div[1]/div/div[2]/div/div/button'
opensea_path = '//*[@id="__next"]/div[1]/div[1]/nav/div[1]/a'
metamask_sign = '/html/body/div[1]/div/div[2]/div/div[3]/button[2]'
metamask_sign2 = '/html/body/div[1]/div/div[3]/div/div[3]/button[2]'

# Add Item界面
global xpath_item_input, names_path, descs_path, prop_switch_path, prop_type_path, prop_name_path, prop_save_path, lockcontent_switch_path, lockcontent_path, create_path
xpath_item_input = '//*[@id="media"]'
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
    while True:
        try:
            if sign_slice == "finish":
                print('Sign Done')
                break
            Sign()  # 登录操作步骤
        except:
            print("sign_slice=", sign_slice, ", Sign Error")

    # 成功登录，配置参数
    global upload_prepare_slice
    upload_prepare_slice = 'start'

    # 准备上传操作
    while True:
        try:
            if upload_prepare_slice == 'finish':
                print('Prepare Done')
                break
            Upload_prepare()  # 上传操作步骤
        except:
            print("upload_prepare_slice=", upload_prepare_slice, ", Upload Error")
    
    # 准备完成，配置参数
    global fill_slice, path_items
    fill_slice = 'upload item'
    
    # 填入内容
    for i in path_items:
        while True:
            try:
                if fill_slice == 'finish':
                    print('Fill Done')
                    break
                Fill(i)  # 上传操作步骤
            except:
                print("fill_slice=", fill_slice, ", Fill Error")


    print('finish')