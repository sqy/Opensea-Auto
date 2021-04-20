from selenium import webdriver  #加载selenium模块
import time

#启动带插件的浏览器
plug_path = r"C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/"
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

def create_coll(pic_path,pic_name,pic_desc):
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/section[2]/div/div/div[1]/div[1]/div/div[1]/div').click()
    driver.find_element_by_xpath('//*[@id="image"]').send_keys(pic_path)
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/section[2]/div/div/div[5]/div/div/div/form/div[2]/div/div[1]/input').send_keys(pic_name)
    #加名字重复情况处理
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/section[2]/div/div/div[5]/div/div/div/form/div[3]/textarea').send_keys(pic_desc)
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/section[2]/div/div/div[5]/div/div/div/form/div[4]/div').click()

if __name__ == "__main__":
    password_metamask = r"elysion0922"
    sign_in_metamask(password_metamask)
    pic_path = r"E:\Opensea-Auto\图片.jpg"
    pic_name = r"123"
    pic_desc = r"123"
    create_coll(pic_path,pic_name,pic_desc)
