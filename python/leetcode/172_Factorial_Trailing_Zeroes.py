# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        base = 5

        buffer = int(n/base)
        while buffer > 0:
            ret += buffer
            base *= 5
            buffer = int(n/base)
        return ret






def main():
    s = Solution()
    print(s.trailingZeroes(30))
    print(s.trailingZeroes(5))
    print(s.trailingZeroes(10))


if __name__ == "__main__":
    main()
