# coding: utf-8
import requests
from multiprocessing import  Process
num = 1
from log import log
from sendEmail import send_email
def test(username , password , log_file):
    
    url = "http://passport.weibo.cn/sso/login"
    headers = {
    "Host": "passport.weibo.cn",
    "Connection": "keep-alive",
    "Origin": "https://passport.weibo.cn",
    "Referer": "https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    another_headers = {
    "Host": "passport.weibo.cn",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    data =   {
            "username": username,
            "password": password,
            "savestate":"1",
            "r":"https://weibo.cn",
            "ec":"0",
            "pagerefer":"https://weibo.cn/pub/?vt=",    
            "entry":"mweibo",
            "wentry":"",    
            "loginfrom":"", 
            "client_id":"", 
            "code":"",  
            "qq":"",    
            "mainpageflag":"1",
            "hff":"",   
            "hfp":""    
        }
    sess = requests.Session()  
    try:
        # 用户登录
        sess.post(url = url, headers = headers, data=data)
        log(log_file = log_file, message="succeeded to login weibo")
        log(log_file=log_file, message="started a new session")
    except Exception:
        log(log_file = log_file, message="failed to login weibo")
        send_email(content="failed to login weibo", subject="An exception occured")
        raise Exception()
    home_url = "http://weibo.cn/"
    # response = sess.get(url, verify=False)
    panda_url = "http://weibo.cn/u/5406698634?page=4"
    panda_header = {
        "Host": "weibo.cn",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Referer": "https://weibo.cn/u/5406698634?page=3",
    }
    another_panda_header = {
        "Host": "weibo.cn",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Referer": "https://weibo.cn/u/5406698634?page=2",
    }
    another_panda_url = "http://weibo.cn/u/5406698634"
    while True:
        time.sleep(random.random())
        try:
            # sess.get(url = panda_url  , headers=panda_header, verify=False)
            sess.get(url = another_panda_url  , headers=another_panda_header, verify=False)
            log(log_file = log_file, message="succeeded to get the web_page whose url is {0}".format(panda_url))
        except Exception:
            log(log_file = log_file, message="failed to get the web_page whose url is {0}".format(panda_url))
            send_email(content="failed to get the web_page whose url is {0}".format(panda_url), subject="An exception occured")
            raise Exception()
        print("get panda_url")

        try:
            sess.get(url = home_url, verify=False)
            log(log_file = log_file, message="succeeded to get the web_page whose url is {0}".format(home_url))
        except Exception:
            log(log_file = log_file, message="failed to get the web_page whose url is {0}".format(home_url))
            send_email(content="failed to get the web_page whose url is {0}".format(home_url), subject="AN exception occured")
            raise Exception()
        print("get home")
        # time.sleep(random.random())
        # response = sess.get(url = another_panda_url, headers=another_panda_header, verify=False)
        global num
        global loop
        print(num, loop, num+(loop-1)*3000)
        log(log_file=log_file, message="the current num of this batch is {0}, loop is {1}, total num is {2}".format(num, loop, num+(loop-1)*3000))
        num = num+1
        # if num > 3:
            # raise Exception()
        if num > 3000:
            loop += 1
            num = 0
            log(log_file=log_file, message="end this session, the num is placed with 0, a new session will be created")
            break

loop = 1
import time
import random
my_username = "bobcaoge@outlook.com"
my_password = "..m..m..m"
my_log_file = "D:/Project/python/modules/weiboLog.txt"

another_username = "15588545913"
another_password = "xc1998"
another_log_file = "D:/Project/python/modules/weiboLog1.txt"

def go(username, password, log_file):
    while True:
        # try:
            test(username, password, log_file)
        # except Exception:
            # pass

if __name__ == "__main__":
    # p = Process(target=go, args=(my_username, my_password, my_log_file))
    p1 = Process(target=go, args=(another_username, another_password, another_log_file))
    # go(my_username, my_password, my_log_file))
    # p.start()
    # p.join()
    p1.start()
    p1.join()
