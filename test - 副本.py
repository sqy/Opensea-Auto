from selenium import webdriver  # 引入selenium模块
import os
import pickle
import test2

#获取数据
fileread = open('dataFile.txt', 'rb')  # 打开数据文件
datalist_rb = pickle.load(fileread)  # 读取数据
plug_path = datalist_rb[2]
metamask_password = datalist_rb[3]
metamask_password_choice = datalist_rb[4]
first_choice = datalist_rb[12]

# 启用带插件的浏览器
url_coll = "https://opensea.io/collections"
option = webdriver.ChromeOptions()
option.add_argument("--user-data-dir=" + plug_path)  # 加载Chrome全部插件
option.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
option.add_argument('--start-maximized')  # 全屏窗口
driver = webdriver.Chrome(chrome_options=option)  # 更改Chrome默认选项
print('1')
test2.fuck()
print('2')