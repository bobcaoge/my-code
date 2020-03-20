# -*- coding:utf-8 -*-
# /usr/bin/python2.7
# IPython2 测试代码
import time
import codecs
# 打开文件时用
# 导入 webdriver
from selenium import webdriver

# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys


def main():
    # 调用环境变量指定的PhantomJS浏览器创建浏览器对象
    # driver = webdriver.PhantomJS()

    # 如果没有在环境变量指定PhantomJS位置
    driver = webdriver.PhantomJS(executable_path="D:/Project/phantomjs/bin/phantomjs")

    # get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
    driver.get("http://www.baidu.com/")
    # driver.get("http://www.kolstore.com/dynamic/")
    # time.sleep(2)
    print driver.page_source.encode("utf-8")

    # 获取页面名为 wrapper的id标签的文本内容
    data = driver.find_element_by_id("wrapper").text


    # 打印数据内容
    print data.encode("utf-8")

    driver.save_screenshot("test.png")


    # 关闭浏览器
    driver.quit()


if __name__ == "__main__":
    main()
