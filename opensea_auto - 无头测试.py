from selenium import webdriver  # 引入selenium模块
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 启用带插件的浏览器
plug_path = r"C:/Users/Suqing/AppData/Local/Google/Chrome/User Data/"
#url = r"https://www.baidu.com/"
url = r"https://opensea.io/collections"
option = webdriver.ChromeOptions()
option.add_argument('--no-sandbox') #解决DevToolsActivePort文件不存在的报错
option.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
option.add_argument("--user-data-dir="+plug_path)  # 加载Chrome全部插件
option.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
option.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
#option.add_experimental_option('excludeSwitches',['enable-automation'])  # 把selenium程序伪装成一个正常的请求
#option.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
option.add_argument('--window-size=1920,1080')
#option.add_argument('--start-maximized')         # 全屏窗口
driver = webdriver.Chrome(chrome_options=option)  # 更改Chrome默认选项
driver.get(url)  # 设置打开网页
driver.save_screenshot('0.png')

# 切换页面
def change_window(number):
    handles = driver.window_handles  # 获取当前页面所有的句柄
    driver.switch_to.window(handles[number])
# 登录metamask钱包
def sign_in_metamask(password_metamask):
    while True:
        print('3')
        try:
            print('4')
            driver.save_screenshot('1.png')
            print('4-1')
            time.sleep(5)
            #WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div/div/div[3]/main/div/div/div/div[1]/div[2]/button')))
            print('5')
            driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/div[3]/main/div/div/div/div[1]/div[2]/button').click()  # 点击登录键
            #driver.find_element_by_xpath('//*[@id="kw"]').send_keys('123')
            driver.save_screenshot('2.png')
            print('6')
            break
        except:
            print('7')
            driver.refresh()
            print('8')
    while True:
        try:
            change_window(1)  # 切换至弹出页面
            driver.find_element_by_id("password").send_keys(password_metamask)  # 输入密码
            driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/button/span').click()  # 点确定
            change_window(0)  # 切换回主页面
            break
        except:
            time.sleep(1)

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
                try:
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
                    driver.refresh()  # 防收藏夹卡死
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

# 创建NFT
def add_item(coll_num):
    global coll
    coll = '//*[@id="__next"]/div[1]/div/div/div[3]/main/div/div/section/div/div/div[1]/div[' + str(coll_num) + ']/a/div[2]'
    check_coll()
    check_add()


if __name__ == "__main__":
    print('1')
    password_metamask = r"elysion0922"
    print('2')
    sign_in_metamask(password_metamask)
    add_item(1)
#'//*[@id="reload-button"]'重新加载
