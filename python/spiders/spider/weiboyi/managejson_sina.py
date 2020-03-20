# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import json
import urllib2
import urllib




def get_json_data(start, limit):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
        "Cookie": "loginHistoryRecorded=0; TRACK_DETECTED=1.0.1; TRACK_BROWSER_ID=c5c76123fabfc4e60e3e7228486f7b3e; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22471157%22%2C%22%24device_id%22%3A%221661fd8c390139-0e80be7687b33a-5701732-1327104-1661fd8c3911c4%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221661fd8c390139-0e80be7687b33a-5701732-1327104-1661fd8c3911c4%22%7D; _gscu_867320846=38141836x0isoy19; Hm_lvt_29d7c655e7d1db886d67d7b9b3846aca=1538132499,1538141836,1538183884; Hm_lvt_b96f95878b55be2cf49fb3c099aea393=1538132523,1538141836,1538183885; _gscbrs_867320846=1; web_image_site=http%3A%2F%2Fimg.weiboyi.com; TY_SESSION_ID=f4f59eb0-0155-41af-bae7-3c4f95f6e746; TRACK_USER_ID=471157; Hm_lpvt_29d7c655e7d1db886d67d7b9b3846aca=1538188297; Hm_lpvt_b96f95878b55be2cf49fb3c099aea393=1538188297; Hm_lvt_5ff3a7941ce54a1ba102742f48f181ab=1538133033,1538141869,1538183964,1538188314; username=; rememberusername=; Hm_lvt_28390dde54d52b2842a44c05fcdb31f7=1538266194; Hm_lpvt_28390dde54d52b2842a44c05fcdb31f7=1538266194; PHPSESSID=e7kl2ibrlig7anqqlmn3q9qnu3; aLastLoginTime=1538272340; TRACK_IDENTIFY_AT=2018-09-30T01%3A53%3A14.700Z; TRACK_SESSION_ID=bc69f9c208edf1ea49f3509b9e5a7aec; Hm_lpvt_5ff3a7941ce54a1ba102742f48f181ab=1538272436; _gscs_867320846=t382723481azr4k20|pv:6"
    }
    # url ="http://chuanbo.weiboyi.com/hwreservation/account/list/requirement_id/89581"
    url ="http://chuanbo.weiboyi.com/hwreservation/account/list/requirement_id/89639"
    formdata = {
        "web_csrf_token" : "5bb02c54d9786",
        "price_list" :"tweet,retweet",
        "snbt_exponent_sort":"DESC",
        "start": str(start),
        "limit": str(limit)
    }
    data = urllib.urlencode(formdata)
    request = urllib2.Request(url, data=data, headers=headers)
    response = urllib2.urlopen(request)
    ret = response.read()
    print ret
    return ret


def main():
    limit = 20
    start = 1460
    for i in range(37, 316):
        json_data = get_json_data(start, limit)
        filename = "./sina/json_data_" + str(i)+".json"
        with open(filename, "w") as f:
            f.write(json_data)
        start += limit


if __name__ == "__main__":
    main()
