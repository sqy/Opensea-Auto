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

# 第一部分：浏览器参数
# 1.启用带插件的浏览器
#plug_path = r"C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/"
plug_path = r"C:/Users/Suqing/AppData/Local/Google/Chrome/User Data/"
#plug_path = r"C:/Users/mayn/AppData/Local/Google/Chrome/User Data/"
url = r"https://opensea.io/collections"
option = webdriver.ChromeOptions()
option.add_argument("--user-data-dir="+plug_path)  # 加载Chrome全部插件
option.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
option.add_argument('--start-maximized')         # 全屏窗口
driver = webdriver.Chrome(chrome_options=option)  # 更改Chrome默认选项

# 第二部分：获取数据
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
    global nft_name_temp, nft_desc_part1, nft_desc_part2, nft_price, nft_sensitive_switch, nft_number
    global nft_prop_switch, nft_prop_type, nft_prop_name
    global nft_level_switch
    global nft_stats_switch
    global nft_lockcontent_switch, nft_lockcontent
    data = xlrd.open_workbook('file.xls', formatting_info=True)
    table = data.sheet_by_name(r'cover')
    nft_name_temp = table.row_values(1)[0]
    nft_desc_part1 = table.row_values(1)[1]
    nft_desc_part2 = table.row_values(1)[2]
    nft_price = table.row_values(1)[3]
    nft_sensitive_switch = table.row_values(1)[4]
    nft_number = table.row_values(1)[5]
    nft_prop_switch = table.row_values(2)[1]
    nft_prop_type = table.row_values(2)[2]
    nft_prop_name = table.row_values(3)[2]
    nft_level_switch = table.row_values(4)[1]
    nft_stats_switch = table.row_values(7)[1]
    nft_lockcontent_switch = table.row_values(10)[1]
    nft_lockcontent = table.row_values(10)[2]
    # 获取图片像素部分
    global nft_desc_pixels
    Image.MAX_IMAGE_PIXELS = 2300000000
    files_path = get_files_path('pic')
    nft_desc_pixels = []
    for i in files_path:
        nft_desc_pixels.append(str(Image.open(i).size[0]) + '  x  ' + str(Image.open(i).size[1]) + '  px')

# 第三部分：判定操作
# 1.切换页面
def change_window(number):
    handles = driver.window_handles  # 获取当前页面所有的句柄
    driver.switch_to.window(handles[number])

# 2.收藏夹判定
def check_coll():
    while True:
        print('检测收藏夹是否正确', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        try:
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, coll)))  # 框
            try:
                driver.find_element_by_link_text("Suqingyan")
                print('找到用户收藏夹')
                break
            except:
                print('非用户收藏夹')
                driver.find_element_by_xpath(opensea_path).click()  # 点击Opeasea
                print('跳转首页')
                try:
                    WebDriverWait(driver, 60, 0.5).until(EC.presence_of_element_located((By.XPATH, homecreate_path)))
                    driver.find_element_by_xpath(homecreate_path).click()  # 点击首页Create
                    print('跳转收藏夹')
                except:
                    driver.get(url)
                    print('再次跳转首页')
        except:
            driver.get(url)
    print('检测完成')

# 第四部分：分项操作
# 1.登录metamask钱包
def sign_in_metamask():
    while True:
        try:
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, sign_in_button)))
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

# 第五部分：分部操作
# 1.登录
def sign_in(coll_num):
    driver.get(url)  # 设置打开网页
    sign_in_metamask()
    check_coll()
    global add_item_url
    coll = '//*[@id="__next"]/div[1]/main/div/div/section/div/div/div[1]/div[' + str(coll_num) + ']/a'
    coll_url = driver.find_elements_by_xpath(coll)
    for get_url in coll_url:
        add_item_url = str(get_url.get_attribute("href")) + '/assets/create'

# 2.Create界面
def fill_info(i, j):
    ## 此处应加签名判定操作
    # step 1:Item.send
    driver.find_element_by_xpath(inputpic_path).send_keys(i)  # 上传图片
    # step 2:Name.send
    nft_name = nft_name_temp + ' #' + nft_number
    driver.find_element_by_xpath(names_path).send_keys(nft_name)  # 图片名称
    # step 3:Description.send
    nft_desc = nft_desc_part1 + '\n\nID:' + nft_number + ' // ' + j + '\n\n' + nft_desc_part2
    driver.find_element_by_xpath(descs_path).send_keys(nft_desc)  # 描述
    # step 4:Properties
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
    if nft_level_switch == '启动':
        pass
    # step 6:Stats
    if nft_stats_switch == '启动':
        pass
    # step 7:Unlockable Content
    if nft_lockcontent_switch == '启动':
        while True:
            try:
                driver.find_element_by_xpath(lockcontent_switch_path).click()  # Unlockable Content
                break
            except:
                driver.execute_script("window.scrollTo(0,1000);")  # 拖滚动条下移，防止界面找不到元素
        driver.find_element_by_xpath(lockcontent_path).send_keys(nft_lockcontent)

# 3.第一次Item界面
def nft_sell():
    while True:
        print('检测创建是否成功')
        try:
            WebDriverWait(driver, 15, 0.5).until(EC.presence_of_element_located((By.XPATH, created_close_path)))
            print('创建成功，Close键存在', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            driver.find_element_by_xpath(created_close_path).click()
            break
        except:
            try:
                driver.find_element_by_xpath(sellbutton_path)
                break
            except:
                print('再次点Create')
                try:
                    create_times = create_times + 1
                    driver.find_element_by_xpath(create_path).click()  # 点Create
                    try:
                        change_window(1)
                        driver.find_element_by_xpath(
                            '//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]').click()  # 签名
                        change_window(0)
                    except:
                        pass
                except:
                    try:
                        change_window(1)
                        driver.find_element_by_xpath(
                            '//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]').click()  # 签名
                        change_window(0)
                    except:
                        pass
                if create_times == 10:
                    create_times = 0
                    driver.refresh()
                    while True:
                        try:
                            WebDriverWait(driver, 30, 0.5).until(
                                EC.presence_of_element_located((By.XPATH, inputpic_path)))
                            break
                        except:
                            driver.refresh()
                    fill_info(i, j, k, l, n)
                    driver.execute_script("window.scrollTo(0,10000);")  # 拖滚动条下移，防止界面找不到元素
                    driver.find_element_by_xpath(create_path).click()  # 点Create
                    print('完成刷新后Create点击')

# 4.上架界面
def nft_plist():


def nft(coll_num):
    global nft_slice
    nft_slice = 0
    sign_in(coll_num)
    pics = get_files_path(r"pic")  # 完成第一个数组（图片）
    get_pics_info()
    for i, j in zip(pics, nft_desc_pixels):
        driver.get(add_item_url)
        fill_info(i, j)
        nft_sell()
        nft_plist()




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

    nft(1)
