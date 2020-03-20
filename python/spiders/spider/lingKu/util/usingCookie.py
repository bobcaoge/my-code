# /usr/bin/python2.7
# -*- coding:utf-8 -*-
import requests


def crawl():
    headers_with_cookie = {
    "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    "Cookie": "acw_tc=65c86a0a15431239517478840ec4ef8764abc5268c2601066d0f306f6038dc; UM_distinctid=167495b2dff3ee-096e39a4472396-5701732-144000-167495b2e0129; Hm_lvt_fea2280e19fa5e87d45b28fee3aaf1f9=1543123972; PHPSESSID=tv1qrnbahq6jh92pgabtvnaqu0; Mobile=18716039760; isAlterCom=25561; UserId=25561; UserName=xiyouyan; Type=1; code=428dbb260873bedb81d8; CNZZDATA1257125375=1027233657-1543123969-https%253A%252F%252Fwww.baidu.com%252F%7C1543132593; Hm_lpvt_fea2280e19fa5e87d45b28fee3aaf1f9=1543132595"
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
    sess = requests.session()
    response = sess.post(url=url_to_get_json, headers = headers_with_cookie, data=form_data)
    print response.content
    print "*"*100
    form_data["page"] = 2
    response = sess.post(url=url_to_get_json, headers = headers_without_cookie, data=form_data)
    print response.content


def main():
    crawl()


if __name__ == "__main__":
    main()
