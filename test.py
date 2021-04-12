from selenium import webdriver  #加载selenium模块
import time

#启用带插件的浏览器
option = webdriver.ChromeOptions()
option.add_argument("--user-data-dir="+r"C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/") #加载Chrome全部插件
driver = webdriver.Chrome(chrome_options=option)  #更改Chrome默认选项
driver.get("https://opensea.io/account/settings")  #设置打开网页

driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/main/div/div/div/div[1]/div[2]/div/div').click()

#time.sleep(3)
#driver.quit()
