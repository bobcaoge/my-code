# coding: utf-8
import urllib2
import threading
from multiprocessing import Pool
import requests
import os
import time
import re
import Queue
from lxml import etree


class HomePage(object):
    def __init__(self, url):
        self.urls_of_pictures = None  # 用于存放获取的照片链接
        self.html = ""
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        self.son_urls = []
        self.url = url

    def get_html_of_home(self):
        """
        获取主页的html文档
        :param url_of_home:
        :return:
        """
        response = requests.get(self.url, headers=self.headers)
        self.html =response.content

    def get_urls_of_son(self):
        pattern = "//tbody//span//a[contains(class, xst)]//@href"
        html = etree.HTML(self.html)
        self.son_urls = html.xpath(pattern)
        self.url_manger()

    def url_manger(self):
        real_urls = []
        for url in self.son_urls:
            real_url = "http://www.58reniao.com/" + url
            real_urls.append(real_url)
        self.son_urls = real_urls


class EveryonePage(object):

    def __init__(self, url):
        self.picture_links = []
        self.url = url
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        self.file_number = 0
        self.html = ""
        self.title = ''

    def get_title(self):
        pattern = "//title"
        html = etree.HTML(self.html)
        self.title = html.xpath(pattern)[0].text

    def download_pictures(self):
        self.get_title()
        print self.title
        if not os.path.exists(self.title):
            os.mkdir(self.title)
        else:
            return 0
        for link in self.picture_links:
            time.sleep(0.5)
            print("正在下载", link)
            request = urllib2.Request(link, headers=self.headers )
            response = urllib2.urlopen(request)
            # response = requests.get(link, headers=self.headers)
            # html = response.content
            html = response.read()
            with open(self.title+"/"+"%d.jpg"%self.file_number, "wb") as f:
                self.file_number += 1
                f.write(html)
            print("下载成功")

    def get_html(self):
        response = requests.get(self.url, headers=self.headers)
        self.html = response.content
        # print self.html

    def get_links_of_pictures(self):
        # pattern = "//tbody/tr//td[contains(class, t_msgfont)]//img[contains(onload, th)]//@src"
        pattern = 'img src="(.*jpg)" onload="thumb'
        # html = etree.HTML(self.html)
        pattern = re.compile(pattern)
        # self.picture_links = html.xpath(pattern)
        self.picture_links = pattern.findall(self.html)
        print self.picture_links, "图片链接"


class ThreadManager(threading.Thread):
    def __init__(self):
        super(ThreadManager, self).__init__()
        self.number = 0

    def run(self):
        if len(queue) > 0:
            url = queue.pop()


queue = []


def son_page(url):
    print("正在下载", url)
    everyone_page = EveryonePage(url)
    everyone_page.get_html()
    everyone_page.get_links_of_pictures()
    everyone_page.download_pictures()
    print("此页下载完成")

def main():
    url = "http://www.58reniao.com/forum-47-3.html"
    home_page = HomePage(url)
    home_page.get_html_of_home()
    # print(home_page.html)
    # print(type(home_page.html))
    home_page.get_urls_of_son()
    # print(home_page.son_urls)
    # print(len(home_page.son_urls))
    count = 0
    po = Pool(3)
    for son_url in home_page.son_urls:
        try:
            # print("正在下载", son_url, count)
            # everyone_page = EveryonePage(son_url)
            # everyone_page.get_html()
            # everyone_page.get_links_of_pictures()
            # everyone_page.download_pictures()
            # print("此页下载完成")
            po.apply_async(son_page, (son_url, ))

        except Exception:
           print "一个异常"
    # url = "http://www.58reniao.com/thread-1566669-1-2.html"
    # everyone_page = EveryonePage(url)
    # everyone_page.get_html()
    # # print everyone_page.html
    # everyone_page.get_links_of_pictures()
    # # print everyone_page.picture_links
    # everyone_page.download_pictures()
    po.close()
    po.join()



if __name__ == '__main__':
    main()