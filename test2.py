from selenium import webdriver  # 引入selenium模块
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from PIL import Image
import xlrd   # 引入Excel读取模块
from xlutils.copy import copy        #导入copy模块
import time
import os

# 启用带插件的浏览器

plug_path = r"C:/Users/Suqing/AppData/Local/Google/Chrome/User Data/"
url = r"https://opensea.io/collections"
option = webdriver.ChromeOptions()
option.add_argument("--user-data-dir="+plug_path)  # 加载Chrome全部插件
option.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
option.add_argument('--start-maximized')         # 全屏窗口
driver = webdriver.Chrome(chrome_options=option)  # 更改Chrome默认选项
driver.get(url)  # 设置打开网页

# 切换页面
def change_window(number):
    handles = driver.window_handles  # 获取当前页面所有的句柄
    driver.switch_to.window(handles[number])
# 登录metamask钱包
def sign_in_metamask(password_metamask):
    while True:
        try:
            print('等待登录')
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/main/div/div/div/div[1]/div[2]/button')))
            print('找到登录键')
            driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/div/div[1]/div[2]/button').click()  # 点击登录键
            print('点击登录键')
            break
        except:
            driver.refresh()
    while True:
        try:
            change_window(1)  # 切换至弹出页面
            driver.find_element_by_id("password").send_keys(password_metamask)  # 输入密码
            driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/button/span').click()  # 点确定
            change_window(0)  # 切换回主页面
            break
        except:
            time.sleep(1)
# 给根目录文件夹内的全部文件拼装绝对路径
def get_files(pics_path):
    listdir = os.listdir(pics_path)  # 定位文件夹位置
    filepath = os.getcwd()  # 当前工作目录
    allfile = []  # 定义为数组
    for file in listdir:
        allfile.append(filepath + '\\' + pics_path + '\\' + file)  # 拼装地址
    return allfile
# 获取图片信息
def get_pt():
    # 提取excel有多少行，并做成数组
    data = xlrd.open_workbook('file.xls', formatting_info=True)  # 打开xls文件,不修改原有样式
    table = data.sheets()[1]
    wb = copy(data)  # 利用xlutils.copy下的copy函数复制
    ws = wb.get_sheet(1)  # 获取表单
    num_nrows = []
    for i in range(int(table.nrows)):
        num_nrows.append(i)
    #提取部分desc做成数组
    table2 = data.sheet_by_name(r'item')  # 表格内工作表
    ncols = table2.ncols  # 定义列数
    table3 = data.sheet_by_name(r'cover')  # 表格内工作表
    desc_part = []
    for i in range(ncols):
        if i == 2:
            desc_part = table2.col_values(i)
    # 获取图片像素部分
    Image.MAX_IMAGE_PIXELS = 2300000000
    a = get_files('pic')
    desc_mix = []
    story = str(table3.col_values(2)[1])  # 故事位置
    global lockcontent
    lockcontent = str(table3.col_values(3)[1])  # 付费内容
    for i,j in zip(a,desc_part):
        desc_mix.append(str(j) + ' ' + str(Image.open(i).size[0]) + '  x  ' + str(Image.open(i).size[1]) + '  px  \n\n' + story)
    # 拼装描述内容
    for i,j in zip(num_nrows,desc_mix):
        ws.write(i,2,j)  # 改变（0,0）的值
    wb.save('file_do.xls')   # 保存文件
# 上架签名
def postlist_sign(s):
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
# 收藏夹判定
def check_coll():
    while True:
        print('检测收藏夹是否正确', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        try:
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, coll)))  # 框
            try:
                driver.find_element_by_link_text("Suqingyan")
                print('找到用户收藏夹')
                driver.find_element_by_xpath(coll).click()  # 点击指定收藏夹
                print('完成点击')
                WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, manage_path)))
                driver.find_element_by_xpath(manage_path).click()
                try:
                    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, additem_path)))  # "Add New Item"
                    break
                except:
                    driver.refresh()
                    try:
                        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, additem_path)))  # "Add New Item"
                        break
                    except:
                        driver.get(url)
            except:
                #driver.find_element_by_link_text("Pixel V2")
                print('非用户收藏夹')
                driver.find_element_by_xpath( opensea_path).click()  # 点击Opeasea
                print('跳转首页')
                try:
                    WebDriverWait(driver, 60, 0.5).until(EC.presence_of_element_located((By.XPATH, homecreate_path)))
                    driver.find_element_by_xpath(homecreate_path).click()  # 点击首页Create
                    print('跳转收藏夹', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
                except:
                    driver.get(url)
                    print('再次跳转首页')
        except:
            driver.get(url)
    print('检测完成')
# 404收藏夹判定
def check_coll404():
    while True:
        print('检测收藏夹是否正确', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        try:
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, coll)))  # 框
            try:
                driver.find_element_by_link_text("Suqingyan")
                print('找到用户收藏夹')
                driver.find_element_by_xpath(coll).click()  # 点击指定收藏夹
                print('完成点击')
                WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, view_path)))
                driver.find_element_by_xpath(view_path).click()
                try:
                    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, sortby_path)))  # 第一个框
                    break
                except:
                    driver.get(url)
            except:
                #driver.find_element_by_link_text("Pixel V2")
                print('非用户收藏夹')
                driver.find_element_by_xpath( opensea_path).click()  # 点击Opeasea
                print('跳转首页')
                try:
                    WebDriverWait(driver, 60, 0.5).until(EC.presence_of_element_located((By.XPATH, homecreate_path)))
                    driver.find_element_by_xpath(homecreate_path).click()  # 点击首页Create
                    print('跳转收藏夹', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
                except:
                    driver.get(url)
                    print('再次跳转首页')
        except:
            driver.get(url)
    print('检测完成')
# 重新选择最新Item
def item_again():
    try:
        driver.get(url)
        check_coll404()
        driver.find_element_by_xpath(sortby_path).click()  # Sort by
        driver.find_element_by_xpath(recentcreate_path).click()  # Recently Created
        time.sleep(3)
        driver.refresh()
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, firstkuang_path)))
        driver.find_element_by_xpath(firstkuang_path).click()
    except:
        pass
# Additem键判定
def check_add():
    while True:
        try:
            driver.find_element_by_xpath(additem_path).click()  # 点击"Add New Item"
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, inputpic_path)))  # 传图
            break
        except:
            try:
                WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, inputpic_path))) # 传图
                break
            except:
                try:
                    change_window(1)
                    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]').click()  # 签名
                    change_window(0)
                except:
                    driver.refresh()
# 填item信息
def fill_info(i, j, k, l, n):
    driver.find_element_by_xpath(inputpic_path).send_keys(i)  # 上传图片
    driver.find_element_by_xpath(names_path).send_keys(j)  # 图片名称
    driver.find_element_by_xpath(descs_path).send_keys(k)  # 描述
    while True:
        try:
            driver.find_element_by_xpath(addprop_path).click()  # 增加Properties
            break
        except:
            driver.execute_script("window.scrollTo(0,200);")  # 拖滚动条下移，防止界面找不到元素
    while True:
        try:
            WebDriverWait(driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, proptype_path)))
            driver.find_element_by_xpath(proptype_path).send_keys(l)  # 输入Prop_type
            driver.find_element_by_xpath(propname_path).send_keys(n)  # 增加Prop_name
            driver.find_element_by_xpath(saveprop_path).click()  # 点击Save_prop
            break
        except:
            pass
        ActionChains(driver).move_by_offset(1400, 100).click().perform()
        driver.find_element_by_xpath(addprop_path).click()  # 增加Properties
    while True:
        try:
            driver.find_element_by_xpath(lock_path).click()  # Unlockable Content
            break
        except:
            driver.execute_script("window.scrollTo(0,1000);")  # 拖滚动条下移，防止界面找不到元素
    driver.find_element_by_xpath(lockcontent_path).send_keys(lockcontent)
# 上架判定
def postlist():
    while True:
        try:
            driver.find_element_by_xpath(filcheck_path)
            break
        except:
            try:
                driver.find_element_by_xpath(plist_path).click()  # 点击post your listing\
                WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH,listitem_path)))
                postlist_sign(180)
                while True:
                    try:
                        WebDriverWait(driver, 60, 0.5).until(EC.presence_of_element_located((By.XPATH, filcheck_path)))
                        break
                    except:
                        try:
                            driver.find_element_by_xpath(listitem_path)
                        except:
                            break
                try:
                    driver.find_element_by_xpath(filcheck_path)
                    break
                except:
                    try:
                        driver.find_element_by_xpath(plist_path)
                    except:
                        driver.refresh()
            except:
                pass

# 创建NFT
def add_item(coll_num):

    global coll
    coll = '//*[@id="__next"]/div[1]/main/div/div/section/div/div/div[1]/div[' + str(coll_num) + ']/a'
    WebDriverWait(driver, 60, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/main/div/div/section/div/div/div[1]/div[1]/a')))
    urls = driver.find_elements_by_xpath('//*[@id="__next"]/div[1]/main/div/div/section/div/div/div[1]/div[1]/a')
    #url = urls[0].get_attribute("href")
    print(urls)
    for url in urls:
        print(url.get_attribute("href"))
        https: // opensea.io / collection / worda - chinese - characters / assets / create
        #print(urls.get_attribute("href"))


if __name__ == "__main__":
    password_metamask = r"elysion0922"
    sign_in_metamask(password_metamask)
    global manage_path, additem_path, opensea_path, homecreate_path, inputpic_path, names_path, descs_path, addprop_path, proptype_path, propname_path, saveprop_path, lock_path, lockcontent_path, \
        create_path, view_path, visit_path, sortby_path, recentcreate_path, firstkuang_path, sellbutton_path, price_path, plist_path, listitem_path, filcheck_path
    manage_path = '//*[@id="__next"]/div[1]/main/div/div/div[1]/div[2]/div[2]/div[2]/div/a/div/div/i'
    additem_path = '//*[@id="__next"]/div[1]/div/main/div/div/section/div[2]/div[3]/section/div/a'
    opensea_path = '//*[@id="__next"]/div[1]/div[1]/nav/div[1]/a'
    homecreate_path = '//*[@id="__next"]/div[1]/main/div/div/div[1]/div[2]/div[1]/div[1]/a'
    inputpic_path = '//*[@id="media"]'
    names_path = '//*[@id="name"]'
    descs_path = '//*[@id="description"]'
    addprop_path = '//*[@id="__next"]/div[1]/main/div/div/section/div[2]/div/form/section[6]/div[1]/div/div[2]/button'
    proptype_path = '/html/body/div[3]/div/div/div/section/table/tbody/tr/td[1]/div/div/input'
    propname_path = '/html/body/div[3]/div/div/div/section/table/tbody/tr/td[2]/div/div/input'
    saveprop_path = '/html/body/div[3]/div/div/div/footer/button'
    lock_path = '//*[@id="unlockable-content-toggle"]'
    lockcontent_path = '//*[@id="__next"]/div[1]/main/div/div/section/div[2]/div/form/section[6]/div[4]/div[2]/textarea'
    create_path = '//*[@id="__next"]/div[1]/main/div/div/section/div[2]/div/form/div/div[1]/span/button'
    visit_path = '//*[@id="__next"]/div[1]/main/div/div/section/div[2]/div/div/div[2]/a[1]'
    view_path = '//*[@id="__next"]/div[1]/main/div/div/div[2]/section[1]/div[1]/div[2]/span/a/p'
    sortby_path = '//*[@id="__next"]/div[1]/div/div/main/div/div/div[2]/div[1]/div[2]/div[2]/input'
    recentcreate_path = "//*[contains(@id,'tippy-')]/div/div/div/ul/li[2]/button"
    firstkuang_path = '//*[@id="__next"]/div[1]/div/div/main/div/div/div[2]/div[2]/div/div[1]/article/a/div[2]'
    sellbutton_path = '//*[@id="__next"]/div[1]/main/div/div/div[1]/div/a[2]'
    price_path = '//*[@id="__next"]/div[1]/main/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/div/div/input'
    plist_path = '//*[@id="__next"]/div[1]/main/div/div/div[2]/div/div[2]/div/div[2]/button'
    listitem_path = '/html/body/div[2]/div/div/div/header/h4'
    filcheck_path = '//*[@id="__next"]/div[1]/main/div/div/div[2]/div[1]/div/div[1]/div[2]/section[1]/div/div[2]/div/div/span/button/i'
    add_item(1)
#'//*[@id="reload-button"]'重新加载
