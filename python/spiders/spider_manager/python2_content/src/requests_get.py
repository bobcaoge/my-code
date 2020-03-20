# coding: utf-8
import requests


# 仅使用urllib2的urlopen()函数，这也只是一个最简单的get请求, 而且没有添加 headers 请求头
def main():
    url = "http://www.baidu.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    }
    response = requests.get(url=url, headers=headers)
    print response.text.encode("utf-8")


if __name__ == "__main__":
    main()
