# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for c in s:
            ret = ret * 26+ (ord(c) - 64)
        return ret



def main():
    s = Solution()
    print(s.titleToNumber('A'))
    print(s.titleToNumber('AB'))
    print(s.titleToNumber('ZY'))


if __name__ == "__main__":
    main()
