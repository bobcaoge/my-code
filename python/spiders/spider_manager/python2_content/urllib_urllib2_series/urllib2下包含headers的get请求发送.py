# /usr/bin/python2.7
# -*- coding:utf-8 -*-
import urllib2


# urllib2最简单的爬虫.py中使用的urlopen()是最简单的get请求，其中并没有对请求头处理
# 下面的程序加了请求头处理，以防止在user-agent上的反爬虫
def main():
    url = "http://www.baidu.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    }
    # 构建请求
    request = urllib2.Request(url, headers=headers)
    # 发送请求
    response = urllib2.urlopen(request)
    print response.read()


if __name__ == "__main__":
    main()
