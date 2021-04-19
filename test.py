from selenium import webdriver
import time
 
option = webdriver.ChromeOptions()
option.add_argument("--user-data-dir="+r"C:\Users\mayn\AppData\Local\Google\Chrome\User Data") #加载Chrome全部插件
driver = webdriver.Chrome(chrome_options=option)  #更改Chrome默认选项
driver.get("https://opensea.io/collections")  #设置打开网页

