# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import math


class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        g = math.gcd(p, q)
        p = (p/g)%2
        q = (q/g)%2
        return 1 if p and q else 0 if p == 0 else 2



def main():
    s = Solution()


if __name__ == "__main__":
    main()
