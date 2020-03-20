# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        if s == s[::-1]:
            return 1
        return 2


def main():
    s = Solution()


if __name__ == "__main__":
    main()
