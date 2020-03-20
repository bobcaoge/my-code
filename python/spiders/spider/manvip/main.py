# coding:utf-8
import requests
import urllib2
import webbrowser
from lxml import etree


class  Manvip(object):
    def __init__(self, url):
        self.url = url
        self.fanhao_list = []
        self.html = ''
        self.real_urls_of_every_fanhao = []
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    def get_html(self):
        response = requests.get(self.url, headers=self.headers)
        self.html = response.content

    def get_fanhao_list(self):
        pattern = '//li//div//span//date/a'
        html = etree.HTML(self.html)
        fanhao_list = html.xpath(pattern)
        for fanhao in  fanhao_list:
            self.fanhao_list.append(fanhao[0].text)

    def get_real_url_of_every_fanhao(self):
        url_of_search_page = 'http://cnbtkitty.net/'
        fanhao = self.fanhao_list[0]
        formdata = {'keyword': fanhao}
        response = requests.post(url_of_search_page, data=formdata, headers=self.headers)
        real_url = response.url
        # print(fanhao)
        # print(real_url)
        self.real_urls_of_every_fanhao.append(real_url)
        webbrowser.open(real_url)

    def open_url_in_browser(self):
        pass


def main():
    url = 'http://nanrenvip.org/shiyuanlinai/index_2.html'
    manvip = Manvip(url)
    manvip.get_html()
    # print manvip.html
    manvip.get_fanhao_list()
    print manvip.fanhao_list
    manvip.get_real_url_of_every_fanhao()



if __name__ == '__main__':
    main()