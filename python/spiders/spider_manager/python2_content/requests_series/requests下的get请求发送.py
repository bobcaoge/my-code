# /usr/bin/python2.7
# -*- coding:utf-8 -*-
# 使用第三库requests发送请求
# eg. requests.get(url,key=value) or requests.request("get", url)
# response 有如下属性
#         查看响应内容，response.text 返回的是Unicode格式的数据
#         response.text
#         查看响应内容，response.content返回的字节流数据
#         respones.content
#         查看完整url地址
#         response.url
#         查看响应头部字符编码
#         print response.encoding
#         查看响应码
#         response.status_code
import requests


def main():
    url = "http://www.baidu.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    }
    response = requests.get(url=url, headers=headers)
    print response.text.encode("utf-8")
    # print response.content


if __name__ == "__main__":
    main()
