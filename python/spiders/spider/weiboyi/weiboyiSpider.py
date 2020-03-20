# -*- coding:utf-8 -*-
"""
面向对象的代码，可以运行，但是爬取功能未实现，session中的cookie信息不够完善
"""
import requests
import time
import re
import setting
import os
import random
import urllib2
import urllib


class WeiboyiSpider(object):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
    login_headers = {
        "Host": "chuanbo.weiboyi.com",
        "Connection":"keep-alive",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
        "Accept":"*/*",
        "Referer":"http://www.weiboyi.com/",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
    }
    filename_of_data_from_sina = "./sina/json_data.json"
    sina_total = 0

    def __init__(self, sess, username="", password=""):
        # 如果没有传入账户和密码信息将自动从配置文件setting.py中导入
        if username == "":
            self.username = setting.USERNAME
        if password == "":
            self.password = setting.PASSWORD
        self.sess = sess

    @staticmethod
    def get_the_url_of_capture_from_response(content):
        """
        从content中获取验证码的url
        :param content: 包含验证码的字符串
        :return:验证码的url
        """
        pattern = re.compile(r"http:.*.png")
        result = pattern.findall(content)
        return result[0].replace("\\", "").replace(" ", "")

    def get_the_photo_of_captcha(self, headers, url_of_capture):
        """
        下载验证码的图片并保存在本地的./capture.png下
        :param headers: 请求头
        :param url_of_capture: 验证码图片的url
        :return:
        """
        response = self.sess.get(url_of_capture, headers=headers)
        # print(response.content)
        with open("capture.png", "wb") as f:
            f.write(response.content)

    def get_json_contains_the_info_of_url_of_capture(self):
        """
        通过发送请求获得包含验证码的url的json
        :return: 返回包含验证码的url的json
        """
        url = "http://chuanbo.weiboyi.com/hwauth/index/captcha?web_csrf_token=undefined"
        response = self.sess.get(url=url, headers=self.headers)
        print response.content
        return response.content

    def login(self):
        """
        模拟登陆
        :return:
        """
        content = self.get_json_contains_the_info_of_url_of_capture()
        url_of_captcha = self.get_the_url_of_capture_from_response(content)

        print url_of_captcha

        self.get_the_photo_of_captcha(self.headers, url_of_captcha)
        captcha = raw_input("please input the captcha:")

        url_of_login = "http://chuanbo.weiboyi.com/"
        form_data_of_login = {
            "web_csrf_token": "undefined",
            "mode": "1",
            "typelogin": "1/",
            "piccode": captcha,
            "username": "xiyouyan",
            "password": "xiyouyan123456"
        }
        response = self.sess.post(url=url_of_login, data=form_data_of_login, headers=self.login_headers)
        print response.content
        cookiejar = response.cookies

        # 8. 将CookieJar转为字典：
        cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

        print cookiejar
        print cookiedict

    def get_json_data(self, headers, url, form_data):
        response = self.sess.get(url=url, data=form_data, headers=headers)
        return response.content

    @staticmethod
    def create_dictionary(filename):
        if not os.path.exists(filename):
            with open(filename, "w"):
                pass

    @staticmethod
    def get_total_number_of_sina(json_data):
        pattern = re.compile(r'"total":(\d+)')
        total = 0
        try:
            total = pattern.findall(json_data)[0]
        except Exception,e:
            print(e.message)
        return total

    def craw_sina(self):





        headers = {
        # "Host": "chuanbo.weiboyi.com",
        # "Connection": "keep-alive",
        # "Origin": "http: // chuanbo.weiboyi.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
        # "Referer": "http://chuanbo.weiboyi.com/hworder/sina/index?price_list=tweet%2Cretweet&snbt_exponent_sort=DESC&start=0&limit=20",
        # "X-Tingyun-Id": "y5zrBHz_BzQ;r=766889865"

        }

        url = "http://chuanbo.weiboyi.com/hworder/moments/filterlist/source/all"

        limit = 20
        start = 20
        formdata = {
                "web_csrf_token": "5c511101338e3",
                "price_list": "tweet_hard,reservation",
                "snbt_exponent_sort": "DESC",
                "start": str(start),
                "limit": str(limit)
            }
        data = urllib.urlencode(formdata)
        request = urllib2.Request(url, data=data, headers=headers)
        response = urllib2.urlopen(request)
        ret = response.read()
        print ret
        # self.create_dictionary(self.filename_of_data_from_sina)
        # response = self.sess.Request(url=url, data=formdata, headers=headers)
        # json_data = response.content
        # print json_data
        # json_data = self.get_json_data(url=url, form_data=formdata, headers=headers)
        # self.sina_total = self.get_total_number_of_sina(json_data)
        # print "json_data"
        # print json_data
        # with open("temp.html", "w") as f:
        #     f.write(json_data)

        # while start > self.sina_total:
        #     time.sleep(random.random())
        #     formdata["start"] = str(start)
        #     formdata["limit"] = str(limit)
        #     print(formdata)
        #     # json_data = self.get_json_data(url=url, form_data=formdata, headers=headers)
        #     # print start, self.sina_total, json_data
        #     # with open(self.filename_of_data_from_sina, "a") as f:
        #     #     f.write(json_data+"\n")
        #     start += limit


def main():
    sess = requests.session()
    spider = WeiboyiSpider(sess)
    # 模拟登陆
    spider.login()
    # spider.craw_sina()


if __name__ == "__main__":
    main()
