# /usr/bin/python3.6
# -*- coding:utf-8 -*-

# 代理使用，1. 构建Handler
#          2. 构建opener
#          3. 使用opener发送请求

# urllib2下的各种Handler:
#          ProxyHandler 用作ip代理需要一个字典参数
#          例子，urllib2.ProxyHandler({"http", "ip:port"})
#          code：main1()
#
#          HTTPPasswordMgrWithDefaultRealm 用于需要验证的密码管理器
#          ProxyBasicAuthHandler 用于账号密码验证的代理
#          code：main2()
#
#          CookieJar 用来处理cookie的信息，其内容存储在内存中
#          CookieJar->HttpCookieProcessor->opener
#          code: main3()
#
#          MozillaCookieJar 用来处理cookie的信息，其内容可存储在文件中
#          MozillaCookieJar->HttpCookieProcessor->opener
#          code: main4()
#
#          利用openner进行模拟登陆
#          code: main5()

import urllib2
import urllib
import hashlib


def main1():
    url = "http://www.baidu.com/"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    }
    handler = urllib2.HTTPHandler(debuglevel=1)
    request = urllib2.Request(url=url, headers=headers)
    opener = urllib2.build_opener(handler)
    response = opener.open(request)
    print(response.read())


def main2():
    # 此函数不能运行，缺少必要的高匿的代理的ip，port，username，password
    user = ""
    password = ""
    passmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passmgr.add_password(None,uri="ip:port", user=user, passwd=password)
    handler = urllib2.ProxyBasicAuthHandler(passmgr)
    opener = urllib2.build_opener(handler)
    url = "http://www.baidu.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    }
    request = urllib2.Request(url, headers)
    opener.open(request)


import cookielib


def main3():
    cj = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(handler)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    }
    request = urllib2.Request(url="http://www.baidu.com/", headers=headers)
    opener.open(request)
    cookie_str = ""
    for item in cj:
        cookie_str += item.name + "=" + item.value+";"
    print cookie_str[:-1]


def main4():
    filname = "cookie.txt"
    cookiejar = cookielib.MozillaCookieJar(filename=filname)
    handler = urllib2.HTTPCookieProcessor(cookiejar)
    opener = urllib2.build_opener(handler)
    response = opener.open("http://www.baidu.com")
    html_content = response.read()

    md5 = hashlib.md5()
    md5.update(html_content)
    print md5.hexdigest()

    cookiejar.save()


def main5():
    # 构建包含cookie对象的opener
    cookie = cookielib.MozillaCookieJar(filename="blog_cookie.txt")
    cookie_handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(cookie_handler)

    # 构建请求
    data = {
    "username" : "bobcao",
    "password" : "bobcao"
    }
    url = "http://hiiumaa.club:8088/admin/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
        "Connection": "keep-alive"
    }
    post_data = urllib.urlencode(data)
    request = urllib2.Request(url=url, data=post_data, headers=headers)

    response = opener.open(request)
    with open("blog.html", "w") as f:
        print("start to save html")
        f.write(response.read())
        print("success to save the file")
        md5 = hashlib.md5()
        md5.update(response.read())
        print("/n"+"the md5 code of the content of response is:")
        print(md5.hexdigest())
    cookie.save()

    url = "http://hiiumaa.club:8088/admin/change"
    request = urllib2.Request(url=url, headers=headers)
    response = opener.open(request)
    cookie.save("change_cookie.txt")

    with open("change.html", "wb") as f:
        f.write(response.read())
        print(get_md5_code(response.read()))


def get_md5_code(str = ""):
    md5 = hashlib.md5()
    md5.update(str)
    return md5.hexdigest()

if __name__ == "__main__":
    # main1()
    # main2()
    # main3()
    # main4()
    # main5()
    print get_md5_code("hello")
    print get_md5_code("what")











