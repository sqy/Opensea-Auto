from selenium import webdriver  #加载selenium模块
import time

#启用带插件的浏览器
option = webdriver.ChromeOptions()
option.add_argument("--user-data-dir="+r"C:/Users/mayn/AppData/Local/Google/Chrome/User Data/") #加载Chrome全部插件
driver = webdriver.Chrome(chrome_options=option)  #更改Chrome默认选项
driver.get("https://opensea.io/collections")  #设置打开网页
driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/div/div[1]/div[2]/div/div').click()  #登录metamask钱包
time.sleep(3)
#切换窗口
def change_window(number):
    handles = driver.window_handles
    driver.switch_to.window(handles[number])
    
change_window(1)
driver.find_element_by_id("password").send_keys("elysion0922")  #输入密码
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/button/span').click()  #点确定
driver.close()
change_window(0)
#driver.switch_to.default_content()
driver.find_element_by_tag_name("Create").click()






#driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]').click()

#driver.find_element_by_xpath('').click()


#time.sleep(3)
#driver.quit()
