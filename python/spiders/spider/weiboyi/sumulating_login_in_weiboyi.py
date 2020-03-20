# -*- coding:utf-8 -*-
import requests
import time
import re

username = "xiyouyan"
password = "xiyouyan123456"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

login_headers = {
    "Host": "chuanbo.weiboyi.com",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    "Accept":"*/*",
    "Referer":"http://www.weiboyi.com/",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
}


def get_linux_time_of_str():
    linux_time= time.time()
    return str(int(linux_time*1000))


def get_the_url_of_capture_from_response(content):
    pattern = re.compile(r"http:.*.png")
    result = pattern.findall(content)
    return result[0].replace("\\", "").replace(" ", "")


def get_the_photo_of_capcha(sess, headers, url_of_capture):
    response = sess.get(url_of_capture, headers=headers)
    # print(response.content)
    with open("capture.png", "wb") as f:
        f.write(response.content)


def get_json_contain_info_of_url_capture(sess):
    url ="http://chuanbo.weiboyi.com/hwauth/index/captchaajax"
    form_data = {
        "callback": "jQuery182022545751717313833_1543378930324",
        "_": get_linux_time_of_str()
    }
    response = sess.get(url=url, data=form_data, headers=headers)
    print response.content
    return response.content


def register(sess, captchar):
    # data = {
    #     "pvid": "   6e6448e8-2244-45f3-81fc-288e98f5f72a",
    #     "ref ": "http://chuanbo.weiboyi.com/",
    #     "referrer": "    http://chuanbo.weiboyi.com/",
    #     "key": " ilUGEioG6wY",
    #     "v": "   1.7.5",
    #     "av ": " 1.7.5",
    #     "did ": "efd85911-fded-4fdd-8307-0557ded4383d",
    #     "sid ": "e5f624f6-06ff-4e39-934b-4642ee3c5926",
    #     "__r ": get_linux_time_of_str()
    # }
    # url = "http://beacon.tingyun.com/xhr1"
    # sess.post(url=url, data=data, headers=headers)
    url = "http://chuanbo.weiboyi.com/"
    form_data = {
        "web_csrf_token": "undefined",
        "mode": "1",
        "typelogin":"1/",
        "piccode":captchar,
        "username":"xiyouyan",
        "password":"xiyouyan123456"
    }
    response = sess.post(url=url, data=form_data, headers=login_headers)
    print response.content


def main():
    sess = requests.session()
    content = get_json_contain_info_of_url_capture(sess)
    url_of_captcha = get_the_url_of_capture_from_response(content)
    print url_of_captcha
    get_the_photo_of_capcha(sess,headers,url_of_captcha)
    captcha = raw_input("please input the captcha:")
    register(sess, captcha)



if __name__ == "__main__":
    main()
