# /usr/bin/python3.6
# -*- coding:utf-8 -*-

# requests下发送post请求，这和urllib和urllib2下发送的post请求略有不同
#       在urllib2下发送post请求需要将要发送的数据进行网络编码，以便于适合发送
#       在requests下只需要将数据传送给post函数即可
import requests


def main():
    data = {
        "username": "bobcao",
        "password": "bobcao"
    }
    url = "http://hiiumaa.club:8088/admin/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    }
    response = requests.post(url,data=data, headers=headers)
    with open("temp.html", "w") as f:
        f.write(response.content)


if __name__ == "__main__":
    main()
