# /usr/bin/python3.6
# -*- coding:utf-8 -*-
# session对象代表一次用户会话：从客户端浏览器连接服务器开始，到客户端浏览器与服务器断开。
# 可以用来存放cookie
import requests


def main():
    url = "http://www.renren.com/PLogin.do"
    data = {
        "email": "378082326@qq.com",
        "password": "..m..m..m"
    }
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    sess = requests.session()
    # 模拟登陆
    sess.post(url=url, data=data, headers=headers)
    # 获得其他页面内容
    url_another = "http://www.renren.com/privacyhome.do"
    response = sess.get(url=url_another)
    with open("temp.html", "w") as f:
        f.write(response.content)


if __name__ == "__main__":
    main()
