#! /usr/bin/python3.6
#-*- coding:utf-8 -*-
import requests
from lxml import etree
def get_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    return requests.get(url, headers=headers)
def main():
    url = "http://www.36dm.club/search.php?keyword=%E8%BF%9B%E5%87%BB%E7%9A%84%E5%B7%A8%E4%BA%BA%E7%AC%AC%E4%B8%80%E5%AD%A3"
    html = get_page(url)
    info = etree.HTML(html.content)
    url_head = "http://www.36dm.club/"
    url_tails = info.xpath('//td/a[@target="_blank"]/@href')
    ret = []
    for url in url_tails:
        ret.append(get_magnet(url_head+url))
        print ret[-1][1] +" "
    ret.sort()
    for i in ret:
        print i[0]

def get_magnet(url):
    html = get_page(url)
    info = etree.HTML(html.content)
    title = info.xpath('//title')
    magnet = info.xpath('//a[@id="magnet"]/@href')
    ret = magnet[0] if len(magnet) > 0 else ""
    ret = ret.split("&")[0] if ret else ""
    return title[0].text if title else "", ret




if __name__ == "__main__":
    main()