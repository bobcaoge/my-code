# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import math


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 0
        while a <= math.sqrt(c/2):
            b = math.sqrt(c - a**2)
            if b == int(b):
                return True
            a += 2
        a = 1
        while a <= math.sqrt(c/2):
            b = math.sqrt(c - a**2)
            if b == int(b):
                return True
            a += 2

        return False


def main():
    s = Solution()
    print(s.judgeSquareSum(2))


if __name__ == "__main__":
    main()
