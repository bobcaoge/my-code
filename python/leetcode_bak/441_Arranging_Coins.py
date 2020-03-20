# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import math

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        before = int(math.sqrt(2*n))
        if before*(before+1) <= 2*n < (before+1)*(before+2):
            return before
        else:
            return before-1


def main():
    s = Solution()
    print(s.arrangeCoins(1))
    print(s.arrangeCoins(5))
    print(s.arrangeCoins(8))


if __name__ == "__main__":
    main()
