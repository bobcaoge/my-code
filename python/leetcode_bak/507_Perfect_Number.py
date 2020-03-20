# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import math


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        buf = 1
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                # print(i)
                buf += i + num / i
        # print(buf)
        if num == int(buf):
            return True
        return False

    def checkPerfectNumber1(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num in (6, 28, 496, 8128, 33550336)


def main():
    s = Solution()
    print(s.checkPerfectNumber(6))


if __name__ == "__main__":
    main()
