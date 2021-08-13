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
driver.get(url)  # 设置打开网页

# 第二部分：获取数据
# 1.给根目录文件夹内的全部文件拼装绝对路径
def get_files(pics_path):
    listdir = os.listdir(pics_path)  # 定位文件夹位置
    filepath = os.getcwd()  # 当前工作目录
    allfile = []  # 定义为数组
    for file in listdir:
        allfile.append(filepath + '\\' + pics_path + '\\' + file)  # 拼装地址
    return allfile
# 2.获取图片信息
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
    number = []
    for i in range(ncols):
        if i == 0:
            number = table2.col_values(i)
        if i == 2:
            desc_part = table2.col_values(i)
    # 获取图片像素部分
    Image.MAX_IMAGE_PIXELS = 2300000000
    a = get_files('pic')
    desc_mix = []
    story = str(table3.col_values(2)[1])  # 故事位置
    global lockcontent
    lockcontent = str(table3.col_values(3)[1])  # 付费内容
    #for i,j in zip(a,desc_part):
    for i, j, k in zip(a, desc_part, number):
        desc_mix.append(str(j) + chr(int(int(k) + 19967)) + ' ' + '//' + ' ' + str(Image.open(i).size[0]) + '  x  ' + str(Image.open(i).size[1]) + '  px  \n\n' + story)
        #desc_mix.append(str(j) + ' ' + str(Image.open(i).size[0]) + '  x  ' + str(Image.open(i).size[1]) + '  px  \n\n' + story)
    # 拼装描述内容
    for i,j in zip(num_nrows,desc_mix):
        ws.write(i,2,j)  # 改变（0,0）的值
    wb.save('file_do.xls')   # 保存文件

# 第三部分：基础操作
# 1.切换页面
def change_window(number):
    handles = driver.window_handles  # 获取当前页面所有的句柄
    driver.switch_to.window(handles[number])
# 3.上架签名
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

# 第四部分：判定操作
# 1.收藏夹判定
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
                driver.find_element_by_xpath( opensea_path).click()  # 点击Opeasea
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
# 4.上架判定
def postlist(m):
    postlist_times = 0
    while True:
        try:
            driver.find_element_by_xpath(filcheck_path)
            break
        except:
            try:
                driver.find_element_by_xpath(price_path).send_keys(Keys.CONTROL + 'a')  # 全选
                driver.find_element_by_xpath(price_path).send_keys(Keys.DELETE)  # 删除，清空
                driver.find_element_by_xpath(price_path).send_keys(str(m))
                driver.find_element_by_xpath(plist_path).click()  # 点击post your listing\
                WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located((By.XPATH,listitem_path)))
                try:
                    driver.find_element_by_xpath(viewitem_path)
                    driver.refresh()
                except:
                    postlist_sign(30)
                    try:
                        check_plist = 0
                        WebDriverWait(driver, 60, 0.5).until(EC.presence_of_element_located((By.XPATH, viewitem_path)))
                        driver.find_element_by_xpath(viewitem_path).click()
                    except:
                        check_plist = 1
                        driver.refresh()
                    if check_plist == 0:
                        while True:
                            try:
                                WebDriverWait(driver, 60, 0.5).until(EC.presence_of_element_located((By.XPATH, filcheck_path)))
                                break
                            except:
                                try:
                                    driver.find_element_by_xpath(listitem_path)
                                    try:
                                        postlist_sign(180)
                                    except:
                                        pass
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
                postlist_times = postlist_times + 1
                time.sleep(1)
                if postlist_times == 30:
                    driver.refresh()
                    postlist_times = 0

# 第五部分：页面操作
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
# 2.填item信息
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
            try:
                WebDriverWait(driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/section/table/tbody/tr/td[1]/div/div/input')))
                driver.find_element_by_xpath('/html/body/div[2]/div/div/div/section/table/tbody/tr/td[1]/div/div/input').send_keys(l)  # 输入Prop_type
                driver.find_element_by_xpath('/html/body/div[2]/div/div/div/section/table/tbody/tr/td[2]/div/div/input').send_keys(n)  # 增加Prop_name
                driver.find_element_by_xpath('/html/body/div[2]/div/div/div/footer/button').click()  # 点击Save_prop
                break
            except:
                pass
        ActionChains(driver).move_by_offset(800, 100).click().perform()
        driver.find_element_by_xpath(addprop_path).click()  # 增加Properties
    if lockcontent_do == 1:
        while True:
            try:
                driver.find_element_by_xpath(lock_path).click()  # Unlockable Content
                break
            except:
                driver.execute_script("window.scrollTo(0,1000);")  # 拖滚动条下移，防止界面找不到元素
        driver.find_element_by_xpath(lockcontent_path).send_keys(lockcontent)


# 创建NFT
def add_item(coll_num):
    a = 0
    get_pt()
    global coll
    coll = '//*[@id="__next"]/div[1]/main/div/div/section/div/div/div[1]/div[' + str(coll_num) + ']/a'
    pics = get_files(r"pic")  # 完成第一个数组（图片）
    datafile_path = r'file_do.xls'  # 表格位置
    data = xlrd.open_workbook(datafile_path)  # 获取数据
    table = data.sheet_by_name(r'item')  # 表格内工作表
    ncols = table.ncols  # 定义列数
    file_num = []
    names = []
    descs = []
    prop_type = []
    prop_name = []
    for i in range(ncols):
        if i == 0:
            file_num = table.col_values(i)  # 序号
        if i == 1:
            names = table.col_values(i)  # NFT命名
        if i == 2:
            descs = table.col_values(i)  # NFT描述
        if i == 3:
            prop_type = table.col_values(i)  # NFT中prop项分类
        if i == 4:
            prop_name = table.col_values(i)  # NFT中prop项命名
    check_coll()
    coll_url = driver.find_elements_by_xpath(coll)
    for get_url in coll_url:
        add_item_url = str(get_url.get_attribute("href")) + '/assets/create'
    for i, j, k, l, n, m, o in zip(pics, names, descs, prop_type, prop_name, table.col_values(5), file_num):  # 图片地址、NFT命名、NFT描述、prop分类、prop命名、上架价格、NFT序号
        driver.get(add_item_url)
        if a == 0:
            waittimes = 0
            while True:
                try:
                    WebDriverWait(driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, inputpic_path)))
                    try:
                        change_window(1)
                        driver.find_element_by_xpath(
                            '//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]').click()  # 签名
                        change_window(0)
                        break
                    except:
                        pass
                except:
                    try:
                        change_window(1)
                        driver.find_element_by_xpath(
                            '//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]').click()  # 签名
                        change_window(0)
                        break
                    except:
                        pass
                waittimes = waittimes + 1
                if waittimes > 5:
                    break
                time.sleep(1)
        try:
            change_window(1)
            driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]').click()  # 签名
            change_window(0)
        except:
            pass
        fill_info(i, j, k, l, n)
        driver.execute_script("window.scrollTo(0,10000);")  # 拖滚动条下移，防止界面找不到元素
        driver.find_element_by_xpath(create_path).click()  # 点Create
        print('完成Create点击')
        create_times = 0
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
                        driver.find_element_by_xpath(create_path).click()  # 点Create
                        create_times = create_times + 1
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
        #time.sleep(60)
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, sellbutton_path)))
        driver.find_element_by_xpath(sellbutton_path).click()
        while True:
            try:
                WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, price_path)))  # 输价
                break
            except:
                driver.refresh()
                try:
                    driver.find_element_by_xpath(sellbutton_path).click()
                except:
                    pass

        print('输入价格')
        postlist(m)

        a += 1
        print("图片序号:{}，本次上传第{}张".format(int(o), int(a)),
              time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))  # 输出图片序号
        os.remove(i)  # 删除已上传图片
        driver.get(add_item_url)  # 跳转additem
        print('跳转additem')

if __name__ == "__main__":
    global sign_in_button, sign_in_unlock, opensea_path, homecreate_path, inputpic_path, names_path, descs_path, addprop_path, proptype_path, propname_path, saveprop_path, lock_path, lockcontent_path, \
        create_path, created_close_path, visit_path, sellbutton_path, lowerprice_path, price_path, plist_path, listitem_path, viewitem_path, filcheck_path
    sign_in_button = '//*[@id="__next"]/div[1]/main/div/div/div/div[1]/div[2]/button'
    sign_in_unlock = '//*[@id="app-content"]/div/div[3]/div/div/button/span'
    opensea_path = '//*[@id="__next"]/div[1]/div[1]/nav/div[1]/a'
    homecreate_path = '//*[@id="__next"]/div[1]/main/div/div/div[1]/div[2]/div[1]/div[1]/a'
    inputpic_path = '//*[@id="media"]'
    names_path = '//*[@id="name"]'
    descs_path = '//*[@id="description"]'
    addprop_path = '//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/section[6]/div[1]/div/div[2]/button'
    proptype_path = '/html/body/div[2]/div/div/div/section/table/tbody/tr/td[1]/div/div/input'
    propname_path = '/html/body/div[2]/div/div/div/section/table/tbody/tr/td[2]/div/div/input'
    saveprop_path = '/html/body/div[2]/div/div/div/footer/button'
    lock_path = '//*[@id="unlockable-content-toggle"]'
    lockcontent_path = '//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/section[6]/div[4]/div[2]/textarea'
    create_path = '//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/div/div[1]/span/button'
    created_close_path = '/html/body/div[5]/div/div/div/div[2]/button/i'
    visit_path = '//*[@id="__next"]/div[1]/main/div/div/section/div[2]/div/div/div[2]/a[1]'
    sellbutton_path = '//*[@id="__next"]/div[1]/main/div/div/div[1]/div/a[2]'
    lowerprice_path = '//*[@id="__next"]/div[1]/main/div/div/div[1]/div/button[2]'
    price_path = '//*[@id="__next"]/div[1]/main/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/div/div/input'
    plist_path = '//*[@id="__next"]/div[1]/main/div/div/div[2]/div/div[2]/div/div[2]/button'
    listitem_path = '/html/body/div[2]/div/div/div/header/h4'
    viewitem_path = '/html/body/div[2]/div/div/div/footer/a'
    filcheck_path = '//*[@id="__next"]/div[1]/main/div/div/div[2]/div[1]/div/div[1]/div[2]/section[1]/div/div[2]/div/div/span/button/i'

    global password_metamask, lockcontent_do
    password_metamask = r"elysion0922"
    lockcontent_do = 0

    sign_in_metamask()
    add_item(1)
#'//*[@id="reload-button"]'重新加载
