# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import urllib2
def main():
    url = "http://www.baidu.com/"
    response = urllib2.urlopen(url)
    print(response.read())
    pass

if __name__ == "__main__":
    main()
