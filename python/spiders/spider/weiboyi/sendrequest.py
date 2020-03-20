# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import requests
import json
import urllib2


def get_capture_photo(url):
    headers= {
        "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    }
    json_string = requests.get(url, headers=headers).text
    li = dict(eval(json_string))
    capture_photo_url = li["url"].replace("\\","")
    print(capture_photo_url)
    request = urllib2.Request(capture_photo_url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read()
    with open("capture.png", "wb") as f:
        f.write(content)
    # print(content)


def main():
    url = "http://chuanbo.weiboyi.com/hwauth/index/captcha?web_csrf_token=undefined"
    get_capture_photo(url)

if __name__ == "__main__":
    main()
