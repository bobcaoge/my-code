# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import math


class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ab = a*b//math.gcd(a, b)
        ac = a*c//math.gcd(a, c)
        bc = b*c//math.gcd(b, c)
        abc = c*ab/ math.gcd(c, ab)

        def calc_n(x):
            return x // a + x // b + x // c - x // ab - x // ac - x // bc + x // abc

        start = 1
        end = 2*10**9
        mid = (end+start)//2
        while start <= end:
            pos = calc_n(mid)
            if pos == n:
                return max(a*(mid//a), b*(mid//b), c*(mid//c))
            elif pos < n:
                start = mid + 1
            else:
                end = mid - 1
            mid = (end+start)//2


def main():
    s = Solution()
    print(s.nthUglyNumber(3, 2,3,4))
    print(s.nthUglyNumber(3, 2,3,5))
    print(s.nthUglyNumber(4, 2,3,4))
    print(s.nthUglyNumber(5,2,11,13))
    print(s.nthUglyNumber(n = 1000000000, a = 2, b = 217983653, c = 336916467))


if __name__ == "__main__":
    main()
