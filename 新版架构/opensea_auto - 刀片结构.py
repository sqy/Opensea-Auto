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
    if nft_prop_switch == '启动':
        nft_prop_type = table.row_values(2)[2]
        nft_prop_name = table.row_values(3)[2]
    nft_level_switch = table.row_values(4)[1]
    nft_stats_switch = table.row_values(7)[1]
    nft_lockcontent_switch = table.row_values(10)[1]
    if nft_lockcontent_switch == '启动':
        nft_lockcontent = table.row_values(10)[2]
    # 获取图片像素部分
    global nft_desc_pixels
    Image.MAX_IMAGE_PIXELS = 2300000000
    files_path = get_files_path('pic')
    nft_desc_pixels = []
    for i in files_path:
        nft_desc_pixels.append(str(Image.open(i).size[0]) + '  x  ' + str(Image.open(i).size[1]) + '  px')

def append_pic_name():
    mix_name = nft_name_temp + ' #' + nft_number
    return mix_name

def append_pic_desc():
    mix_desc = nft_desc_part1 + '\n\nID:' + nft_number + ' // ' + + nft_desc_part2

def nft():
    pics = get_files_path(r"pic")  # 完成第一个数组（图片）
    for i in pics:





if __name__ == "__main__":
    global password_metamask, lockcontent_do
    password_metamask = r"elysion0922"
