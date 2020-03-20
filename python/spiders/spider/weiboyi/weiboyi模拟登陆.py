# /usr/bin/python3.6
# -*- coding:utf-8 -*-
"""
面向过程的代码，可以运行
"""
import requests
import time
import re


def get_linux_time_of_str():
    linux_time= time.time()
    return str(int(linux_time*1000))


def get_the_url_of_capture_from_response(content):
    pattern = re.compile(r"http:.*.png")
    result = pattern.findall(content)
    return result[0].replace("\\", "").replace(" ", "")


def get_the_url_of_capcha(sess, headers):
    url_of_getting_capture = "http://chuanbo.weiboyi.com/hwauth/index/captcha?web_csrf_token=undefined"
    response = sess.get(url=url_of_getting_capture, headers=headers)
    url_of_capture = get_the_url_of_capture_from_response(response.content)
    return url_of_capture


def get_the_photo_of_capcha(sess, headers, url_of_capture):
    response = sess.get(url_of_capture, headers=headers)
    # print(response.content)
    with open("capture.png", "wb") as f:
        f.write(response.content)


def login(sess, headers):
    data = {
        "pvid":"   6e6448e8-2244-45f3-81fc-288e98f5f72a",
        "ref ":"http://chuanbo.weiboyi.com/",
        "referrer":"    http://chuanbo.weiboyi.com/",
        "key":" ilUGEioG6wY",
        "v":"   1.7.5",
        "av ":" 1.7.5",
        "did ":"efd85911-fded-4fdd-8307-0557ded4383d",
        "sid ":"e5f624f6-06ff-4e39-934b-4642ee3c5926",
        "__r ":get_linux_time_of_str()
    }
    url = "http://beacon.tingyun.com/xhr1"
    sess.post(url=url, data=data, headers=headers)

    # 模拟登陆
    capture = raw_input("please input the capture:")
    print("capture", capture)
    data = {
        "web_csrf_token": "undefined",
        "mode": "1",
        "typelogin":"1/",
        "piccode":capture,
        "username":"xiyouyan",
        "password":"xiyouyan123456"
    }
    url_to_login = "http://chuanbo.weiboyi.com/"
    response = sess.post(url=url_to_login, data=data, headers=headers)
    print response.content
    response = sess.get("http://chuanbo.weiboyi.com/")
    with open("index_temp.html", "w") as f:
        f.write(response.content)


def main():
    sess = requests.session()
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    # 获取index
    url = "http://www.weiboyi.com/"
    sess.get(url,headers=headers)

    # 获取验证码连接
    url_of_capture = get_the_url_of_capcha(sess, headers)

    # 获去验证码图片
    get_the_photo_of_capcha(sess, headers, url_of_capture)
    #
    login(sess, headers)


if __name__ == "__main__":
    main()

