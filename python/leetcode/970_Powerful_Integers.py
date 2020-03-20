# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import math

class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        ret = set()
        for i in range(18):
            before = x ** i
            for j in range(18):
                num = before + y**j
                if num <= bound:
                    ret.add(num)
        return list(ret)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
