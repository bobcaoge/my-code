# /usr/bin/python2.7
# -*- coding:utf-8 -*-
import requests
from constant import headers, username, password


def get_vcode(sess):
    url = "http://www.kolstore.com/interface/vcode.php"
    response = sess.post(url=url, headers=headers)
    with open("vcode.png", "wb") as f:
        f.write(response.content)
    vcode = raw_input("please input the vcode:")
    return vcode


def register(sess):
    login_url = "http://www.kolstore.com/interface/login.php"
    vcode = get_vcode(sess)
    form_data = {
        "act": "company",
        "userName": username,
        "passWord": password,
        "vcode": vcode,
        "autoLogin": "0"
    }
    response = sess.post(url=login_url, data=form_data, headers=headers)
    print response.content

    # test_url = "http://www.kolstore.com/interface/company/weixin.php"
    # test_form_data = {
    #     "page": "1",
    #     "userType":"0",
    #     "priceType":"SingnalPicPrice",
    #     "accountType":"2"
    # }
    # response = sess.post(url=test_url, data=test_form_data, headers=headers)
    # print response.content
    # with open("weixin.html", "wb") as f:
    #     f.write(response.content)


def main():
    sess = requests.session()
    register(sess)


if __name__ == "__main__":
    main()
