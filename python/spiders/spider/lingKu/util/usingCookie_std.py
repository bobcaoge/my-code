# /usr/bin/python2.7
# -*- coding:utf-8 -*-
import urllib2
import urllib


def crawl():
    headers_with_cookie = {
    "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    "Cookie": "acw_tc=65c86a0a15431239517478840ec4ef8764abc5268c2601066d0f306f6038dc; UM_distinctid=167495b2dff3ee-096e39a4472396-5701732-144000-167495b2e0129; PHPSESSID=tv1qrnbahq6jh92pgabtvnaqu0; Mobile=18716039760; isAlterCom=25561; UserId=25561; UserName=xiyouyan; Type=1; code=428dbb260873bedb81d8; Hm_lvt_fea2280e19fa5e87d45b28fee3aaf1f9=1543123972,1543133768; Hm_lpvt_fea2280e19fa5e87d45b28fee3aaf1f9=1543133786; CNZZDATA1257125375=1027233657-1543123969-https%253A%252F%252Fwww.baidu.com%252F%7C1543133784"
  }


    headers_without_cookie = {
    "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
}
    url_to_get_json = "http://www.kolstore.com/interface/company/weixin.php"
    page = 1
    form_data = {
        "page": page,
        "userType": 0,
        "priceType": "SingnalPicPrice",
        "accountType": 2
    }
    data = urllib.urlencode(form_data)
    request = urllib2.Request(url=url_to_get_json, data=data, headers=headers_with_cookie)
    handler = urllib2.HTTPHandler()
    openner = urllib2.build_opener(handler)
    response = openner.open(request)
    print response.read()


def main():
    crawl()


if __name__ == "__main__":
    main()
