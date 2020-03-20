# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import json
import urllib2
import urllib


def temp():
    with open("D:/data.json", "r") as f:
        content = f.read()
        print(len(content))
    js = json.loads(content, )
    datas = js['data']['rows']
    print datas
    datalist = list(datas)
    print(datalist)
    print(len(datalist))


def get_json_data(start, limit):
    headers = {
        "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
        "Cookie": "_gscu_867320846=48743558qvmo6v12; loginHistoryRecorded=0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22471157%22%2C%22%24device_id%22%3A%22168984f4edd71-0d827ef7199aac-b781636-1327104-168984f4ede106%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22168984f4edd71-0d827ef7199aac-b781636-1327104-168984f4ede106%22%7D; TRACK_DETECTED=1.0.1; TRACK_BROWSER_ID=4f2abecf3cfe9af3fb05d460cdd92061; _gscbrs_867320846=1; Hm_lvt_29d7c655e7d1db886d67d7b9b3846aca=1548743558,1548816636; Hm_lpvt_29d7c655e7d1db886d67d7b9b3846aca=1548816636; PHPSESSID=c52dl6n1bducrcsbpdc38g40a3; Hm_lvt_b96f95878b55be2cf49fb3c099aea393=1548743558,1548816637; Hm_lpvt_b96f95878b55be2cf49fb3c099aea393=1548816637; aLastLoginTime=1548816641; web_image_site=http%3A%2F%2Fimg.weiboyi.com; TY_SESSION_ID=6a9449d1-81e4-4d8f-ac40-dc2245afde3f; Hm_lvt_5ff3a7941ce54a1ba102742f48f181ab=1548743567,1548816646; TRACK_USER_ID=471157; TRACK_IDENTIFY_AT=2019-01-30T02%3A50%3A46.094Z; TRACK_SESSION_ID=818d2a40e2219e137d5be94e66a5e436; Hm_lpvt_5ff3a7941ce54a1ba102742f48f181ab=1548816674; _gscs_867320846=4881663626tvci12|pv:4"
  }
    # url ="http://chuanbo.weiboyi.com/hwreservation/account/list/requirement_id/89581"
    url = "http://chuanbo.weiboyi.com/hworder/moments/filterlist/source/all"
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
    return ret


def main():
    limit = 20
    start = 0
    for i in range(0, 350):
        json_data = get_json_data(start, limit)
        filename = "./pengyouquan1/json_data_" + str(i)+".json"
        with open(filename, "w") as f:
            f.write(json_data)
        start += limit



if __name__ == "__main__":
    main()
