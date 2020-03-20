# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import math
class Solution(object):
    def isPowerOfTwo1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        n = math.log2(n)
        if n == int(n):
            return True
        return False

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return not n & (n - 1)
def main():
    s = Solution()


if __name__ == "__main__":
    main()
