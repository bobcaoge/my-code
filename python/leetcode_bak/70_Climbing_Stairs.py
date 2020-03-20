# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a = 1
            b = 2
            for i in range(n-2):
                a, b = b, a+b
            return b


def main():
    s = Solution()
    for i in range(1, 10):
        print( s.climbStairs(i))


if __name__ == "__main__":
    main()
