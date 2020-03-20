# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import requests
import random
import time

login_headers = {
    "Host": "www.kolstore.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Origin": "http://www.kolstore.com",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "http//www.kolstore.com/dynamic/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
}
json_headers={
"Host": "www.kolstore.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Origin": "http://www.kolstore.com",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "http://www.kolstore.com/company/choose_opinionLeaders.php?olt=weixin",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
}

username = "xiyouyan"
password = "xiyouyan"


def get_random_int():
    return random.randint(10000, 99999).__str__()


def get_vcode(sess):
    url = "http://www.kolstore.com/interface/vcode.php?_="
    url += get_random_int()
    print url
    response = sess.get(url=url, headers=headers)
    with open("vcode.png", "wb") as f:
        f.write(response.content)
    vcode = raw_input("please input the vcode:")
    return vcode


def register(sess):
    index_url = "http://www.kolstore.com/dynamic/"
    print sess.get(index_url, headers=headers).content
    # return 0
    vcode = get_vcode(sess)

    login_form_data = {
        "act": "company",
        "userName": username,
        "passWord": password,
        "vcode": vcode,
        "autoLogin": "0"
    }
    login_url = "http://www.kolstore.com/interface/login.php"
    response = sess.post(url=login_url, data=login_form_data, headers=login_headers)
    print response.content
    return sess

def crawl(sess, page):
    json_url = "http://www.kolstore.com/interface/company/weixin.php"
    form_data={
        "page": page,
        "userType": "0",
        "priceType": "SingnalPicPrice",
        "accountType": "2"
    }
    response = sess.post(url=json_url, data=form_data, headers=json_headers)
    return response.content

def save_json(filname, content):
    with open(filname, "w") as f:
        print("start to save json")
        f.write(content)
        print("success to save json")

def main():
    sess = requests.session()
    sess = register(sess)
    for page in range(1, 3713):
        content = crawl(sess, page)
        time.sleep(random.randint(1, 5))

        print content
        filename = "./new_json/weixin_json_"+str(page)+".json"
        save_json(filename, content)



if __name__ == "__main__":
    main()
