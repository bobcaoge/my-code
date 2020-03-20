# /usr/bin/python2.7
# -*- coding:utf-8 -*-
#requests下代理比较简单
#               1. 不需要用户名密码的ip代理
#                   配置proxies参数，proxies={"http":"ip:port"}
#                   code: main1
#               2. 需要用户名密码的高匿IP代理
#                   配置proxies参数，proxies={"http": "username:password@ip:port
#                   code: main2
#               3. web验证代理
#                   配置auth参数，auth=('username', 'password')
#                   code: main3
# cookie 处理
#       通过response.cookies返回cookiejar对象
#       通过requests.utils.dict_from_cookiejar()返回字典形式的cookie
import requests
url = "http://www.baidu.com"
headers = ""


def main1():
    proxies={
        "http": "http://112.126.65.26:12345",
    }
    response = requests.get(url=url, headers=headers, proxies=proxies)
    print response.content


def main2():
    # 此代码无法执行，缺少代理
    proxies={
        "http": "username:password@ip:port",
    }
    response = requests.get(url=url, headers=headers, proxies=proxies)
    print response.content


def main3():
    # 此代码无法运行，缺少需要web验证的网页
    auth=('username', 'password')
    response = requests.get(url=url, headers=headers, auth=auth)
    print response.content


if __name__ == "__main__":
    main1()
    # main2()
    # main3()
