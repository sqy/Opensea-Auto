from selenium import webdriver  #加载selenium模块
import time
import os

#启动带插件的浏览器
plug_path = r"C:/Users/mayn/AppData/Local/Google/Chrome/User Data/"
url = r"https://opensea.io/collections"
option = webdriver.ChromeOptions()
option.add_argument("--user-data-dir="+plug_path)  #加载Chrome全部插件
driver = webdriver.Chrome(chrome_options=option)  #更改Chrome默认选项
driver.implicitly_wait(20)  #设置等待20秒钟
driver.get(url)  #设置打开网页
#切换页面
def change_window(number):
    handles = driver.window_handles  #获取当前页面所有的句柄
    driver.switch_to.window(handles[number])
#登录metamask钱包
def sign_in_metamask(password_metamask):
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/div/div[1]/div[2]/div/div').click()  #点击登录键
    time.sleep(3)
    change_window(1)  #切换至弹出页面
    driver.find_element_by_id("password").send_keys(password_metamask)  #输入密码
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/button/span').click()  #点确定
    change_window(0)  #切换回主页面
#创建收藏夹（未完成）
def create_coll(pic_name,pic_desc):
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/section[2]/div/div/div[1]/div[1]/div/div[1]/div').click()
    driver.find_element_by_xpath('//*[@id="image"]').send_keys(r"D:\\Opensea-Auto\\u=2461535694,430498167&fm=26&gp=0.jpg")
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/section[2]/div/div/div[5]/div/div/div/form/div[2]/div/div[1]/input').send_keys(pic_name)
    #加名字重复情况处理
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/section[2]/div/div/div[5]/div/div/div/form/div[3]/textarea').send_keys(pic_desc)
    #driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/section[2]/div/div/div[5]/div/div/div/form/div[4]/div').click()
#获取根目录文件夹内照片绝对路径地址
def get_files(pics_path):
    listdir = os.listdir(pics_path)
    filepath = os.getcwd()
    allfile = []
    for file in listdir:
        allfile.append(filepath + '\\' + file)
    return allfile

#def add_item():


if __name__ == "__main__":
    password_metamask = r"elysion0922"
    sign_in_metamask(password_metamask)
    pic_path = get_files('pic')[0]
    pic_name = r"123"
    pic_desc = r"123"
    create_coll(pic_name,pic_desc)