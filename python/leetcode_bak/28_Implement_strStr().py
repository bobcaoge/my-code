# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        index_of_hay = 0
        index_of_nee = 0
        while index_of_hay < len(haystack) and index_of_nee < len(needle):
            if haystack[index_of_hay] == needle[index_of_nee]:
                index_of_hay += 1
                index_of_nee += 1
            else:
                index_of_hay = index_of_hay - index_of_nee + 1
                index_of_nee = 0
        if index_of_nee > 0 and index_of_nee >= len(needle):
            return index_of_hay - index_of_nee
        else:
            return -1


def main():
    s = Solution()
    print(s.strStr("hello", "ll"))
    print(s.strStr("aaaaa", "bba"))
    print(s.strStr("", "bba"))
    print(s.strStr("aaa", "aaaa"))


if __name__ == "__main__":
    main()
