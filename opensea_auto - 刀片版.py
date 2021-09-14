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

# 第一部分：获取数据
# 1.给根目录文件夹内的全部文件拼装绝对路径
def get_files_path(pics_path):
    listdir = os.listdir(pics_path)  # 定位文件夹位置
    filepath = os.getcwd()  # 当前工作目录
    allfile = []  # 定义为数组
    for file in listdir:
        allfile.append(filepath + '\\' + pics_path + '\\' + file)  # 拼装地址
    return allfile
# 2.获取图片信息
def get_pics_info():
    # 表格参数部分
    global wb, ws
    global nft_name_temp, nft_desc_part1, nft_desc_part2, nft_price, nft_sensitive_switch, nft_coll, nft_number
    global password_metamask, user_name, plug_path
    global nft_prop_switch, nft_prop_type, nft_prop_name
    global nft_level_switch
    global nft_stats_switch
    global nft_lockcontent_switch, nft_lockcontent
    data = xlrd.open_workbook('file.xls', formatting_info=True)
    table = data.sheet_by_name(r'cover')
    wb = copy(data)  # 利用xlutils.copy下的copy函数复制
    ws = wb.get_sheet(0)  # 获取表单
    nft_name_temp = table.row_values(1)[0]
    nft_desc_part1 = table.row_values(1)[1]
    nft_desc_part2 = table.row_values(1)[2]
    nft_price = table.row_values(1)[3]
    nft_sensitive_switch = table.row_values(1)[4]
    nft_coll = table.row_values(1)[5]
    nft_number = table.row_values(1)[6]
    password_metamask = table.row_values(1)[7]
    user_name = table.row_values(1)[8]
    plug_path = table.row_values(1)[9]
    nft_prop_switch = table.row_values(2)[1]
    nft_prop_type = table.row_values(2)[2]
    nft_prop_name = table.row_values(3)[2]
    nft_level_switch = table.row_values(4)[1]
    nft_stats_switch = table.row_values(7)[1]
    nft_lockcontent_switch = table.row_values(10)[1]
    nft_lockcontent = table.row_values(10)[2]
    # 获取图片像素部分
    global nft_desc_pixels, files_path
    Image.MAX_IMAGE_PIXELS = 2300000000
    files_path = get_files_path(r"pic")
    nft_desc_pixels = []
    for i in files_path:
        nft_desc_pixels.append(str(Image.open(i).size[0]) + '  x  ' + str(Image.open(i).size[1]) + '  px')

# 第二部分：基础操作
# 1.切换页面
def change_window(number):
    handles = driver.window_handles  # 获取当前页面所有的句柄
    driver.switch_to.window(handles[number])

# 2.尝试签名
def try_sign(s):
    times = 0
    while times < s:
        times += 1
        try:
            change_window(1)
            driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]').click()  # 签名
            change_window(0)
            break
        except:
            time.sleep(1)

# 第三部分：判定操作
# 1.收藏夹判定
def check_coll():
    while True:
        print('检测收藏夹是否正确', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        try:
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, coll)))  # 框
            try:
                WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, user_name)))
                print('找到用户收藏夹')
                break
            except:
                try:
                    driver.find_element_by_xpath(opensea_path).click()  # 点击Opeasea
                except:
                    driver.get(url)
        except:
            driver.get(url)

# 第四部分：分步操作
# 1.登录
def sign_in():
    driver.get(url)  # 设置打开网页
    while True:
        try:
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, sign_in_button))).send_keys(Keys.CONTROL + '0')
            driver.find_element_by_xpath(sign_in_button).click()  # 点击登录键
            break
        except:
            driver.refresh()
    while True:
        try:
            change_window(1)  # 切换至弹出页面
            driver.find_element_by_id("password").send_keys(password_metamask)  # 输入密码
            driver.find_element_by_xpath(sign_in_unlock).click()  # 点确定
            change_window(0)  # 切换回主页面
            break
        except:
            time.sleep(1)
    # 获取收藏夹地址
    global coll
    coll = '//*[@id="__next"]/div[1]/main/div/div/section/div/div/div[1]/div[' + str(nft_coll) + ']/a'
    check_coll()
    global add_item_url
    coll_url = driver.find_elements_by_xpath(coll)
    for get_url in coll_url:
        add_item_url = str(get_url.get_attribute("href")) + '/assets/create'

# 2.循环全流程
class Fill:
    def __init__(self, i, j):
        try_sign(1)
        if nft_slice == 1:
            self.item(i)
        if nft_slice == 2:
            self.name()
        if nft_slice == 3:
            self.desc(j)
        if nft_slice == 4:
            self.prop()
        if nft_slice == 5:
            self.level()
        if nft_slice == 6:
            self.stats()
        if nft_slice == 7:
            self.lockcontent()
        if nft_slice == 8:
            self.sensitive()
        if nft_slice == 9:
            self.create()
        if nft_slice == 10:
            self.close()
        if nft_slice == 11:
            self.sell()
        if nft_slice == 12:
            self.price()
        if nft_slice == 13:
            self.plist()
        if nft_slice == 14:
            self.view_item()
        if nft_slice == 15:
            self.lower_price()
    # step 1:Item.send
    def item(self, i):
        driver.find_element_by_xpath(inputpic_path).send_keys(i)  # 上传图片

    # step 2:Name.send
    def name(self):
        nft_name = nft_name_temp + ' #' + str(int(nft_number))
        driver.find_element_by_xpath(names_path).send_keys(nft_name)  # 图片名称

    # step 3:Description.send
    def desc(self, j):
        nft_desc = nft_desc_part1 + '\n\nID:' + str(int(nft_number)) + ' // ' + j + '\n\n' + nft_desc_part2
        driver.find_element_by_xpath(descs_path).send_keys(nft_desc)  # 描述

    # step 4:Properties
    def prop(self):
        if nft_prop_switch == '启动':
            while True:
                try:
                    driver.find_element_by_xpath(prop_switch_path).click()  # 增加Properties
                    break
                except:
                    driver.execute_script("window.scrollTo(0,200);")  # 拖滚动条下移，防止界面找不到元素
            while True:
                try:
                    WebDriverWait(driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, prop_type_path)))
                    driver.find_element_by_xpath(prop_type_path).send_keys(nft_prop_type)  # 输入Prop_type
                    driver.find_element_by_xpath(prop_name_path).send_keys(nft_prop_name)  # 增加Prop_name
                    driver.find_element_by_xpath(prop_save_path).click()  # 点击Save_prop
                    break
                except:
                    pass
                ActionChains(driver).move_by_offset(800, 100).click().perform()
                driver.find_element_by_xpath(prop_switch_path).click()  # 增加Properties

    # step 5:Levels
    def level(self):
        if nft_level_switch == '启动':
            pass

    # step 6:Stats
    def stats(self):
        if nft_stats_switch == '启动':
            pass

    # step 7:Unlockable Content
    def lockcontent(self):
        if nft_lockcontent_switch == '启动':
            while True:
                try:
                    driver.find_element_by_xpath(lockcontent_switch_path).click()  # Unlockable Content
                    break
                except:
                    driver.execute_script("window.scrollTo(0,1000);")  # 拖滚动条下移，防止界面找不到元素
            driver.find_element_by_xpath(lockcontent_path).send_keys(nft_lockcontent)

    # step 8:Explicit & Sensitive
    def sensitive(self):
        if nft_sensitive_switch == '启动':
            pass

    # step 9:Create
    def create(self):
        driver.execute_script("window.scrollTo(0,10000);")  # 拖滚动条下移，防止界面找不到元素
        driver.find_element_by_xpath(create_path).click()  # 点Create

    # step 10:Close
    def close(self):
        driver.find_element_by_xpath(created_close_path).click()

    # step 11:Sell
    def sell(self):
        WebDriverWait(driver, 15, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, sellbutton_text))).click()

    # step 12:Price
    def price(self):
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, price_path)))
        driver.find_element_by_xpath(price_path).send_keys(Keys.CONTROL + 'a')  # 全选
        driver.find_element_by_xpath(price_path).send_keys(Keys.DELETE)  # 删除，清空
        driver.find_element_by_xpath(price_path).send_keys(str(nft_price))

    # step 13:Post list
    def plist(self):
        driver.find_element_by_xpath(plist_path).click()  # 点击post your listing

    # step 14:View item
    def view_item(self):
        global viewitem_condition
        viewitem_condition = 1
        change_window(0)  # 未知原因上架签名后，窗口没有切回来
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, viewitem_path))).click()

    # step 15：Lower price
    def lower_price(self):
        WebDriverWait(driver, 60, 0.5).until(EC.presence_of_element_located((By.XPATH, lowerprice_path)))

def error_check():
    global create_times, nft_slice, click_viewitem_times
    print('error step ' + str(nft_slice))
    try:
        url_check = driver.current_url
        if '404' in url_check:
            driver.back()
        elif nft_slice == 15:
            driver.refresh()
        else:
            if nft_slice < 10:
                driver.get(add_item_url)
                create_times = 0
                nft_slice = 1
            else:
                try:
                    WebDriverWait(driver, 15, 0.5).until(EC.presence_of_element_located((By.XPATH, lowerprice_path)))
                    nft_slice = 16
                except:
                    try:
                        driver.find_element_by_xpath(created_close_path)
                        nft_slice = 10
                    except:
                        try:
                            driver.find_element_by_link_text(sellbutton_text)
                            nft_slice = 11
                        except:
                            try:
                                change_window(0)  # 未知原因上架签名后，窗口没有切回来
                                driver.find_element_by_link_text(viewitem_path).click()
                                click_viewitem_times = click_viewitem_times + 1
                                if click_viewitem_times > 10:
                                    temp_url = driver.find_elements_by_xpath(viewitem_path)
                                    for get_url in temp_url:
                                        finish_url = str(get_url.get_attribute("href"))
                                    driver.get(finish_url)
                            except:
                                if viewitem_condition == 1:
                                    driver.refresh()
                                else:
                                    try:
                                        driver.find_element_by_xpath(price_path)
                                        nft_slice = 12
                                    except:
                                        try:
                                            driver.find_element_by_xpath(inputpic_path)
                                            driver.back()
                                        except:
                                            driver.refresh()
    except:
        print('error pass')


def step_check():
    global nft_slice, create_times
    # 加特殊情况if判定
    # Create按键是否成功及Sell界面判定
    if nft_slice == 9:
        try:
            print('检测创建是否成功')
            WebDriverWait(driver, 15, 0.5).until(EC.presence_of_element_located((By.XPATH, created_close_path)))
            print('创建成功，Close键存在', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            nft_slice = 10
        except:
            try:
                driver.find_element_by_link_text(sellbutton_text)
                nft_slice = 11
            except:
                print('再次点Create')
                try:
                    create_times = create_times + 1
                    driver.find_element_by_xpath(create_path).click()  # 点Create
                    try_sign(1)
                except:
                    try_sign(1)
        if create_times == 10:
            create_times = 0
            driver.refresh()
            try_times = 0
            while True:
                try:
                    WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located((By.XPATH, inputpic_path)))
                    nft_slice = 1
                    break
                except:
                    try:
                        WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, sellbutton_text)))
                        nft_slice = 11
                        break
                    except:
                        try_times = try_times + 1
                        if try_times == 60:
                            try_times = 0
                            driver.refresh()
    elif nft_slice == 11:
        try:
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, price_path)))  # 输价
            nft_slice = 12
        except:
            driver.refresh()
            print('step_check 11 refresh')
    elif nft_slice == 12:
        try:
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, plist_path)))
            nft_slice = 13
        except:
            driver.refresh()
            print('step_check 12 refresh')
    elif nft_slice == 13:
        try:
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, listitem_path)))
            sign_times = 0
            while True:
                try:
                    driver.find_element_by_xpath(viewitem_path)
                    driver.refresh()
                    print('step_check 13 refresh,no sign,return 12')
                    nft_slice = 12
                    break
                except:
                    try:
                        change_window(1)
                        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]').click()  # 签名
                        change_window(0)
                        nft_slice = 14
                        break
                    except:
                        time.sleep(1)
                sign_times = sign_times + 1
                if sign_times == 180:
                    driver.refresh()
                    print('step_check 13 refresh,sign_times == 180,return 12')
                    nft_slice = 12
                    break
        except:
            driver.refresh()
            print('step_check 13 refresh,no list item,return 12')
            nft_slice = 12

    # 正常情况
    else:
        nft_slice = nft_slice + 1


def nft():
    get_pics_info()

    # 启用带插件的浏览器
    global url, driver
    url = r"https://opensea.io/collections"
    option = webdriver.ChromeOptions()
    option.add_argument("--user-data-dir=" + plug_path)  # 加载Chrome全部插件
    option.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    option.add_argument('--start-maximized')  # 全屏窗口
    driver = webdriver.Chrome(chrome_options=option)  # 更改Chrome默认选项
    # 登录
    sign_in()
    global nft_slice, nft_number, create_times, click_viewitem_times, viewitem_condition
    this_times = 0
    # NFT创建上架
    for i, j in zip(files_path, nft_desc_pixels):
        driver.get(add_item_url)
        create_times = 0
        click_viewitem_times = 0
        viewitem_condition = 0
        nft_slice = 1
        while nft_slice < 16:
            try:
                error_condition = 0
                Fill(i, j)
            except:
                error_condition = 1
                error_check()
            finally:
                if error_condition == 0:
                    step_check()

        this_times += 1
        print("图片序号:{}，本次上传第{}张".format(int(nft_number), int(this_times)), time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))  # 输出图片序号
        os.remove(i)  # 删除已上传图片
        nft_number = nft_number + 1
        ws.write(1, 6, nft_number)  # 改变（0,0）的值
        wb.save('file.xls')
        driver.get(add_item_url)  # 跳转additem
        print('跳转additem')


if __name__ == "__main__":
    global sign_in_button, sign_in_unlock, opensea_path
    sign_in_button = '//*[@id="__next"]/div[1]/main/div/div/div/div[1]/div[2]/button'
    sign_in_unlock = '//*[@id="app-content"]/div/div[3]/div/div/button/span'
    opensea_path = '//*[@id="__next"]/div[1]/div[1]/nav/div[1]/a'
    global inputpic_path, names_path, descs_path, prop_switch_path, prop_type_path, prop_name_path, prop_save_path, lockcontent_switch_path, lockcontent_path, create_path
    inputpic_path = '//*[@id="media"]'
    names_path = '//*[@id="name"]'
    descs_path = '//*[@id="description"]'
    prop_switch_path = '//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/section[6]/div[1]/div/div[2]/button'
    prop_type_path = '/html/body/div[2]/div/div/div/section/table/tbody/tr/td[1]/div/div/input'
    prop_name_path = '/html/body/div[2]/div/div/div/section/table/tbody/tr/td[2]/div/div/input'
    prop_save_path = '/html/body/div[2]/div/div/div/footer/button'
    lockcontent_switch_path = '//*[@id="unlockable-content-toggle"]'
    lockcontent_path = '//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/section[6]/div[4]/div[2]/textarea'
    create_path = '//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/div/div[1]/span/button'
    global created_close_path, sellbutton_text, lowerprice_path
    created_close_path = '/html/body/div[6]/div/div/div/div[2]/button/i'  # 确定用link_text 'close' 无效
    sellbutton_text = 'Sell'
    lowerprice_path = '//*[@id="__next"]/div[1]/main/div/div/div[1]/div/button[2]'
    global price_path, plist_path, listitem_path, viewitem_path
    price_path = '//*[@id="__next"]/div[1]/main/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/div/div/input'
    plist_path = '//*[@id="__next"]/div[1]/main/div/div/div[2]/div/div[2]/div/div[3]/button'
    listitem_path = '/html/body/div[4]/div/div/div/header/h4'
    viewitem_path = '/html/body/div[4]/div/div/div/footer/a'

    nft()
