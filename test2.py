from selenium import webdriver
import unittest


class Test1（unittest.TestCase）:
    #	一、准备浏览器驱动、网站地址
    #		setUp在每个测试函数运行前运行，注意大小写；self不能省略
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.baseurl = "https://www.baidu.com"

        #	二、打开浏览器，发送请求
        函数名必须以test开头

    def test_01(self):
        browser = self.driver
        browser.get(self.baseurl)
        #	四、调用方法，判断元素是否存在
        flag = Test1.isElementExist（self，“input”）
        if flag：
        print（“该元素存在”）
        else ：
        print（“该元素不存在”）

        #	三、判断元素是否存在的方法
        def isElementExist（

            self）：
        flag = True
        browser = self.driver
        try:
            browser.find_element_by_css_selector(element)
            return flag
        except:
            flag = False
            return flag

 #	五、运行所有以test开头的测试方法
if __name__ == "__main__":
    unittest.main()
