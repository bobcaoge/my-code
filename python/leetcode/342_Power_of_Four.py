# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        while num %4 == 0:
            num /= 4
        return num == 1


def main():
    s = Solution()


if __name__ == "__main__":
    main()
