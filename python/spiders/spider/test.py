import urllib2
def main():
    url = "http://chuanbo.weiboyi.com/hwreservation/account/index/reservation_requirement_id/89581"

    headers = {
        "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
        "Cookie": "loginHistoryRecorded=0; TRACK_DETECTED=1.0.1; TRACK_BROWSER_ID=c5c76123fabfc4e60e3e7228486f7b3e; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22471157%22%2C%22%24device_id%22%3A%221661fd8c390139-0e80be7687b33a-5701732-1327104-1661fd8c3911c4%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221661fd8c390139-0e80be7687b33a-5701732-1327104-1661fd8c3911c4%22%7D; _gscu_867320846=38141836x0isoy19; Hm_lvt_29d7c655e7d1db886d67d7b9b3846aca=1538132499,1538141836,1538183884; Hm_lvt_b96f95878b55be2cf49fb3c099aea393=1538132523,1538141836,1538183885; _gscbrs_867320846=1; web_image_site=http%3A%2F%2Fimg.weiboyi.com; TY_SESSION_ID=f4f59eb0-0155-41af-bae7-3c4f95f6e746; TRACK_USER_ID=471157; Hm_lpvt_29d7c655e7d1db886d67d7b9b3846aca=1538188297; Hm_lpvt_b96f95878b55be2cf49fb3c099aea393=1538188297; Hm_lvt_5ff3a7941ce54a1ba102742f48f181ab=1538133033,1538141869,1538183964,1538188314; username=; rememberusername=; aLastLoginTime=1538204217; TRACK_IDENTIFY_AT=2018-09-29T06%3A57%3A49.359Z; TRACK_SESSION_ID=6d246fb2169ebb1f1120b1f1380e560f; Hm_lpvt_5ff3a7941ce54a1ba102742f48f181ab=1538205621; PHPSESSID=tvk3ckrsb7t3a0cadkopbkij95; _gscs_867320846=t38203193d2h4np15|pv:6"

    }
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read()
    with open("content.html", "w") as f:
        f.write(content)
    print("successed to download")

if __name__ == '__main__':
    main()
