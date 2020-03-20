# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import requests
import sendrequest

# POST请求的目标URL
def main1():
    url = "http://chuanbo.weiboyi.com/hwreservation/account/index/reservation_requirement_id/89581"
    url_login = "http://chuanbo.weiboyi.com/"

    headers = {
        "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    }

    request = urllib2.Request(url, headers=headers)
    login_response = urllib2.urlopen(request)
    login_html = login_response.read()
    with open("login.html", "w") as f:
        print("start to save login.html")
        f.write(login_html)
        print("successed to save login.html")

    capture_url = "http://chuanbo.weiboyi.com/hwauth/index/captcha?web_csrf_token=undefined"
    sendrequest.get_capture_photo(capture_url)
    print "capture photo has been downloaded"
    piccode = raw_input("please input the capture:")
    formdata = {
       "web_csrf_token": "undefined",
       "mode": "1",
       "typelogin": "1/",
       "piccode": piccode,
       "username": "xiyouyan",
       "password": "xiyouyan123456"
    }

    data = urllib.urlencode(formdata)
    request = urllib2.Request(url_login, data = data, headers = headers)
    response = urllib2.urlopen(request)
    print response.read()


def main():
    main1()

if __name__ == '__main__':
    main()