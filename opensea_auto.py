from selenium import webdriver  # 引入selenium模块
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import xlrd   # 引入Excel读取模块
from xlutils.copy import copy        #导入copy模块
import time
import os

# 启用带插件的浏览器
plug_path = r"C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/"
url = r"https://opensea.io/collections"
option = webdriver.ChromeOptions()
option.add_argument("--user-data-dir="+plug_path)  # 加载Chrome全部插件
option.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
option.add_argument('--start-maximized')         # 全屏窗口
driver = webdriver.Chrome(chrome_options=option)  # 更改Chrome默认选项
#driver.implicitly_wait(30)  # 设置等待9999秒钟
driver.get(url)  # 设置打开网页

# 切换页面
def change_window(number):
    handles = driver.window_handles  # 获取当前页面所有的句柄
    driver.switch_to.window(handles[number])
# 登录metamask钱包
def sign_in_metamask(password_metamask):
    WebDriverWait(driver, 99999, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div/div/main/div/div/div/div[1]/div[2]/button')))
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/div/div[1]/div[2]/button').click()  # 点击登录键
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
def check_coll(coll, k_path, additem_path, opensea_path, homecreate_path, inputpic_path):
    while True:
        print('检测收藏夹是否正确', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        try:
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, k_path)))  # 框
            try:
                driver.find_element_by_link_text("[Coser]Beautiful Girls")
                print('找到用户收藏夹')
                driver.find_element_by_xpath(coll).click()  # 点击指定收藏夹
                print('完成点击')
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
                driver.find_element_by_link_text("Pixel V2")
                print('找到默认收藏夹')
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
    while True:
        try:
            driver.find_element_by_xpath(additem_path).click()  # 点击"Add New Item"
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, inputpic_path)))  # 传图
            break
        except:
            driver.refresh()

# 创建NFT
def add_item(coll_num, k_path, additem_path, opensea_path, homecreate_path, inputpic_path, names_path, descs_path, addprop_path, proptype_path, propname_path, saveprop_path, create_path, visit_path, sellbutton_path, price_path, plist_path, filcheck_path):
    a = 0
    get_pt()
    coll_num += 1
    coll = '//*[@id="__next"]/div[1]/div/div/main/div/div/section[2]/div/div/div[1]/div['+str(coll_num)+']/a/div/a/div'
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
    for i, j, k, l, n, m, o in zip(pics, names, descs, prop_type, prop_name, table.col_values(5), file_num):  # 图片地址、NFT命名、NFT描述、prop分类、prop命名、上架价格、NFT序号
        check_coll(coll, k_path, additem_path, opensea_path, homecreate_path, inputpic_path)
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
                print('propsend出错')
                ActionChains(driver).move_by_offset(1400, 100).click().perform()
                driver.find_element_by_xpath(addprop_path).click()  # 增加Properties
        driver.execute_script("window.scrollTo(0,10000);")  # 拖滚动条下移，防止界面找不到元素
        driver.find_element_by_xpath(create_path).click()  # 点Create
        print('完成Create点击')
        while True:
            print('检测创建是否成功')
            try:
                WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, visit_path)))
                print('创建成功，Visit键存在', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
                break
            except:
                print('再次点Create')
                try:
                    driver.find_element_by_xpath(create_path).click()  # 点Create
                except:
                    pass
        #测试后决定Visit是否加循环，默认成功率100%
        driver.find_element_by_xpath(visit_path).click()  # Visit
        while True:
            try:
                WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located((By.XPATH, sellbutton_path)))  # sell
                driver.find_element_by_xpath(sellbutton_path).click()  # sell
                WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, price_path)))  # 输价
                break
            except:
                try:
                    driver.find_element_by_xpath(price_path)
                    break
                except:
                    driver.refresh()
        driver.find_element_by_xpath(price_path).send_keys(str(m))  # 输入价格 #输入框只能输入数字
        print('输入价格')
        while True:
            while True:
                driver.find_element_by_xpath(plist_path).click()  # 点击post your listing
                try:
                    WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/header/h1')))
                    break
                except:
                    driver.refresh()
            times = 0
            while times < 999:
                times += 1
                try:
                    change_window(1)
                    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]').click()  # 签名
                    change_window(0)
                    print("完成签名")
                    while True:
                        try:
                            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, filcheck_path)))
                            break
                        except:
                            try:
                                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/header/h1')
                            except:
                                driver.refresh()
                    break
                except:
                    try:
                        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/header/h1')
                    except:
                        print("未签名，上架不成功")
                        break
                    time.sleep(1)
            try:
                driver.find_element_by_xpath(filcheck_path)
                break
            except:
                pass

        a += 1
        print("图片序号:{}，本次上传第{}张".format(int(o), int(a)), time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))  # 输出图片序号
        os.remove(i)  # 删除已上传图片
        driver.get(url)  # 跳转到收藏夹
        print('跳转收藏夹')

if __name__ == "__main__":
    password_metamask = r"elysion0922"
    sign_in_metamask(password_metamask)
    k_path = '//*[@id="__next"]/div[1]/div/div/main/div/div/section[2]/div/div/div[1]/div[2]/a/div/a/div'
    additem_path = '//*[@id="__next"]/div[1]/div/div/div/main/div/div/section[2]/div[2]/div[3]/section/div/a'
    opensea_path = '//*[@id="__next"]/div[1]/div/div/div[1]/nav/div[1]/a/span'
    homecreate_path = '//*[@id="__next"]/div[1]/div/div/main/div/div/div[1]/div[2]/div[1]/div[2]/a'
    inputpic_path = '//*[@id="__next"]/div[1]/div/div/main/div/div/section/div[2]/div/form/div[1]/div/div/div/input'
    names_path =  '//*[@id="__next"]/div[1]/div/div/main/div/div/section/div[2]/div/form/div[2]/div/div[1]/input'
    descs_path = '//*[@id="__next"]/div[1]/div/div/main/div/div/section/div[2]/div/form/div[4]/textarea'
    addprop_path = '//*[@id="__next"]/div[1]/div/div/main/div/div/section/div[2]/div/form/div[5]/div/div[2]/button'
    proptype_path = '/html/body/div[3]/div/div/div/section/table/tbody/tr/td[1]/div/div/input'
    propname_path = '/html/body/div[3]/div/div/div/section/table/tbody/tr/td[2]/div/div/input'
    saveprop_path = '/html/body/div[3]/div/div/div/footer/button'
    create_path = '//*[@id="__next"]/div[1]/div/div/main/div/div/section/div[2]/div/form/div[12]/div[1]/span/button'
    visit_path = '//*[@id="__next"]/div[1]/div/div/main/div/div/section/div[2]/div/div/div[2]/a[1]'
    sellbutton_path = '//*[@id="__next"]/div[1]/div/div/main/div/div/div[1]/div/a[2]'
    price_path = '//*[@id="__next"]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/div/div/input'
    plist_path = '//*[@id="__next"]/div[1]/div/div/main/div/div/div[2]/div/div[2]/div/div[3]/button'
    filcheck_path = '//*[@id="__next"]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[2]/section[1]/div/div[2]/div/div/span[2]/button/i'
    add_item(1, k_path, additem_path, opensea_path, homecreate_path, inputpic_path, names_path, descs_path, addprop_path, proptype_path, propname_path, saveprop_path, create_path, visit_path, sellbutton_path, price_path, plist_path, filcheck_path)
