# /usr/bin/python2.7
# -*- coding:utf-8 -*-
# 失败
import requests
import random

headers = {
    "Host": "m.kolstore.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Origin": "https://m.kolstore.com",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; MI 6 Build/OPR1.170623.027) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "https://m.kolstore.com/login",
    "Accept-Language": "zh-CN,en-US;q=0.8",
}
homepage_headers = {
    "Host": "m.kolstore.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; MI 6 Build/OPR1.170623.027) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Language": "zh-CN,en-US;q=0.8",
}
username = "xiyouyan"
password = "xiyouyan"


def get_random_int():
    return random.randint(10000, 99999).__str__()


def get_vcode(sess):
    url = "https://m.kolstore.com/vcode?_="
    url += get_random_int()
    print url
    response = sess.get(url=url, headers=homepage_headers, verify=False)
    with open("vcode.png", "wb") as f:
        f.write(response.content)
    vcode = raw_input("please input the vcode:")
    return vcode

def register(sess):
    index_url = "http://m.kolstore.com/"
    print sess.get(index_url, headers=homepage_headers, verify=False).content
    # return 0
    vcode = get_vcode(sess)

    login_form_data = {
        "userName": username,
        "passWord": password,
        "vcode": vcode,
    }
    login_url = "http://m.kolstore.com/user/company/login"
    response = sess.post(url=login_url, data=login_form_data, headers=headers, verify=False)
    print response.content


def main():
    sess = requests.session()
    register(sess)


if __name__ == "__main__":
    main()
