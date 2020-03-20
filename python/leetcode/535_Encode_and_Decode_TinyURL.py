# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Codec:

    urls = []
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.urls.append(longUrl)
        return "http://tinyurl.com/"+str(len(self.urls))



    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.urls[int(shortUrl.split("/")[-1])-1]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


def main():
    s = Solution()


if __name__ == "__main__":
    main()
