# python2中使用urllib和urllib2进行网络请求发送和接收
# urllib主要用来对form表单的内容进行处理（处理成适合网络url发送的形式）
# urllib2主要用来发送url，可直接发送，也可加各种处理（例如，封装到Request中，或者加各种Handler，例如代理等）

# python3中将urllib和urllib2封装成urllib，urllib3是python3下的第三方类库

# urllib3主要使用连接池进行网络请求的访问
# 一下所有代码均使用python2.7的环境
# urllib urllib2 下的爬虫
# version 1.0
# 仅使用urllib2的urlopen()函数，这也只是一个最简单的get请求, 而且没有添加 headers 请求头
import urllib2
def main():
    url = "http://www.baidu.com/"
    response = urllib2.urlopen(url)
    print(response.read())
    pass

if __name__ == "__main__":
    main()
# version 2.0
# 这个版本升级的内容有点多，
# 1.发送post请求(需要用到urllib库的urlencoder()函数) 添加headers
# 2.动态数据的获取, 动态数据的加载是通过ajax等加载的数据，获取动态的数据不需要获取完整的网页（人在浏览器打开看到的内容）
#   只需要获取后台传输的Json数据即可，此时需要通过网络抓包，查找到底是哪个url的发送获得了json加载的数据
import urllib2
import urllib
def main(start=0, limit=20):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    "Cookie": "loginHistoryRecorded=0; TRACK_DETECTED=1.0.1; TRACK_BROWSER_ID=c5c76123fabfc4e60e3e7228486f7b3e; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22471157%22%2C%22%24device_id%22%3A%221661fd8c390139-0e80be7687b33a-5701732-1327104-1661fd8c3911c4%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221661fd8c390139-0e80be7687b33a-5701732-1327104-1661fd8c3911c4%22%7D; _gscu_867320846=38141836x0isoy19; Hm_lvt_29d7c655e7d1db886d67d7b9b3846aca=1538132499,1538141836,1538183884; Hm_lvt_b96f95878b55be2cf49fb3c099aea393=1538132523,1538141836,1538183885; _gscbrs_867320846=1; web_image_site=http%3A%2F%2Fimg.weiboyi.com; TY_SESSION_ID=f4f59eb0-0155-41af-bae7-3c4f95f6e746; TRACK_USER_ID=471157; Hm_lpvt_29d7c655e7d1db886d67d7b9b3846aca=1538188297; Hm_lpvt_b96f95878b55be2cf49fb3c099aea393=1538188297; Hm_lvt_5ff3a7941ce54a1ba102742f48f181ab=1538133033,1538141869,1538183964,1538188314; username=; rememberusername=; Hm_lvt_28390dde54d52b2842a44c05fcdb31f7=1538266194; Hm_lpvt_28390dde54d52b2842a44c05fcdb31f7=1538266194; PHPSESSID=e7kl2ibrlig7anqqlmn3q9qnu3; aLastLoginTime=1538272340; TRACK_IDENTIFY_AT=2018-09-30T01%3A53%3A14.700Z; TRACK_SESSION_ID=bc69f9c208edf1ea49f3509b9e5a7aec; Hm_lpvt_5ff3a7941ce54a1ba102742f48f181ab=1538272436; _gscs_867320846=t382723481azr4k20|pv:6"
    }
    url ="http://chuanbo.weiboyi.com/hwreservation/account/list/requirement_id/89639"
    formdata = {
    "web_csrf_token" : "5bb02c54d9786",
    "price_list" :"tweet,retweet",
    "snbt_exponent_sort":"DESC",
    "start": str(start),
    "limit": str(limit)
    }
    # 对要发送的数据进行封装处理
    data = urllib.urlencode(formdata)
    # 将url，封装好的data防到请求中，一边发送请求
    request = urllib2.Request(url, data=data, headers=headers)
    # 发送请求, 获取响应内容
    response = urllib2.urlopen(request)
    ret = response.read()
    print ret


if __name__ == "__main__":
    main()
# requests 库下的爬虫 首先需要安装对应的第三方库requests pip install requests
# requests比urllib2发送请求更方便一下，requests只需要通过get() 和post()函数分别发送get和post()请求，
# 在发送post请求时只需要将字典形式的数据传入post()函数即可，而不需要对数据进行封装。
import requests

def main():
    url = "http://www.baidu.com"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    }
    response = requests.get(url=url, headers=headers)
    print response.content # 此处与urllib2中的response不同
    pass

if __name__ == "__main__":
    main()



