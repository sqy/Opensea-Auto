from selenium import webdriver  # 引入selenium模块
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
driver = webdriver.Chrome(chrome_options=option)  # 更改Chrome默认选项
driver.implicitly_wait(9999)  # 设置等待9999秒钟
driver.get(r'https://opensea.io/wallet/locked?referrer=%2Faccount')  # 设置打开网页

# 切换页面
def change_window(number):
    handles = driver.window_handles  # 获取当前页面所有的句柄
    driver.switch_to.window(handles[number])
# 登录metamask钱包
def sign_in_metamask(password_metamask):
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/div/div[1]/div[2]/div/div').click()  # 点击登录键
    while True:
        try:
            time.sleep(1)
            change_window(1)  # 切换至弹出页面
            driver.find_element_by_id("password").send_keys(password_metamask)  # 输入密码
            driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/button/span').click()  # 点确定
            change_window(0)  # 切换回主页面
            break
        except:
            pass
# 创建收藏夹（未完成）
def create_coll(pic_name,pic_desc):
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/section[2]/div/div/div[1]/div[1]/div/div[1]/div').click()
    driver.find_element_by_xpath('//*[@id="image"]').send_keys(get_files(r"cover")[0])
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/section[2]/div/div/div[5]/div/div/div/form/div[2]/div/div[1]/input').send_keys(pic_name)
    # 加名字重复情况处理
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/section[2]/div/div/div[5]/div/div/div/form/div[3]/textarea').send_keys(pic_desc)
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/section[2]/div/div/div[5]/div/div/div/form/div[4]/div').click()
    # 创建后还有一步操作
# 给根目录文件夹内的全部文件拼装绝对路径
def get_files(pics_path):
    listdir = os.listdir(pics_path)  # 定位文件夹位置
    filepath = os.getcwd()  # 当前工作目录
    allfile = []  # 定义为数组
    for file in listdir:
        allfile.append(filepath + '\\' + pics_path + '\\' + file)  # 拼装地址
    return allfile
# 定义浮点转字符函数
def float_to_str(float_value):
    try:
        float_value = int(float_value)    #尝试转换为整数
    except ValueError as e:    #文本或文本含数字情况赋值失败
        return float_value     #即无需转换，直接返回
    else:
        if (float_value == int(float_value)):  #如果值为整数
            return str(int(float_value))       #值转换为整数后转换为字符
        else :                                 #如果值为浮点数
            return str(float_value)            #值转换为字符
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
    desc_part = []
    for i in range(ncols):
        if i == 2:
            desc_part = table2.col_values(i)
    # 获取图片像素部分
    Image.MAX_IMAGE_PIXELS = 2300000000
    a = get_files('pic')
    desc_mix = []
    story = str(table2.col_values(8)[0])
    for i,j in zip(a,desc_part):
        desc_mix.append(str(j) + ' ' + str(Image.open(i).size[0]) + '  x  ' + str(Image.open(i).size[1]) + '  px  \n\n' + story)
    # 拼装描述内容
    for i,j in zip(num_nrows,desc_mix):
        ws.write(i,2,j)  # 改变（0,0）的值
    wb.save('file_do.xls')   # 保存文件
# 创建NFT
def add_item():
    get_pt()
    coll = '//*[@id="__next"]/div[1]/div/div/main/div/div/section[2]/div/div/div[1]/div[2]/a/div/a/div'
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
            file_num = table.col_values(i)
        if i == 1:
            names = table.col_values(i)
        if i == 2:
            descs = table.col_values(i)
        if i == 3:
            prop_type = table.col_values(i)
        if i == 4:
            prop_name = table.col_values(i)
    for i,j,k,l,n,m,o in zip(pics,names,descs,prop_type,prop_name,table.col_values(5),file_num):
        driver.find_element_by_xpath(coll).click()
        driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/div/main/div/div/section[2]/div[2]/div[3]/section/a/div').click()  # 点击"Add New Item"
        driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/section/div[2]/div/form/div[1]/div/div/div/input').send_keys(i)  # 上传图片
        driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/section/div[2]/div/form/div[2]/div/div[1]/input').send_keys(j)  # 图片名称
        driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/section/div[2]/div/form/div[4]/textarea').send_keys(k)  # 描述
        while True:
            try:
                driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/section/div[2]/div/form/div[5]/div/div[2]/div/div').click()  # 增加Properties
                break
            except:
                driver.execute_script("window.scrollTo(0,200);")
        driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[1]/div/div/div[2]/div/table/tbody/tr/td[1]/div/div/input').send_keys(l)  # 输入Prop_type
        driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[1]/div/div/div[2]/div/table/tbody/tr/td[2]/div/div/input').send_keys(n)  # 增加Prop_name
        driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div').click()  # 点击Save_prop
        driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/section/div[2]/div/form/div[10]/div[1]/div').click()  # 创建
        driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/section/div[2]/div/div[1]/div[2]/a[2]/div').click()  # sell
        driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/div[1]/div[1]/a/div').click()  # sell
        driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/div[3]/div/div[1]/div/div[3]/div[1]/div[2]/div/div/input').send_keys(str(m))  # 输入价格 #输入框只能输入数字
        driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/div[3]/div/div[2]/div/div[3]/div').click()  # 点击post your listing
        while True:
            try:
                time.sleep(1)
                change_window(1)
                driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]').click()  # 签名
                change_window(0)
                break
            except:
                pass
        time.sleep(3)
        print("pic number:{}".format(int(o)))
        driver.get(url)  # 跳转到收藏夹

if __name__ == "__main__":
    password_metamask = r"elysion0922"
    sign_in_metamask(password_metamask)
    driver.get(url)  # 跳转到收藏夹
    add_item()