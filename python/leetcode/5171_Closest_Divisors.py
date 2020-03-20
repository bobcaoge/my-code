# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import math


class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def manager(x):
            end = int(math.sqrt(x))
            for k in range(end, 0, -1):
                if x % k == 0:
                    start = x // k
                    return [min(start, k), max(k, start)], abs(k-start)
        res1, diff1 = manager(num+1)
        res2, diff2 = manager(num+2)
        if diff1 <= diff2:
            return res1
        else:
            return res2



def main():
    s = Solution()
    print(s.closestDivisors(1))
    print(s.closestDivisors(999))
    print(s.closestDivisors(100000000))


if __name__ == "__main__":
    main()
