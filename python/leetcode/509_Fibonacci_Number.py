# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def fib1(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib(N - 1) + self.fib(N - 2)
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        a = 0
        b = 1
        for i in range(N-1):
            a, b = b, a+b
        return b


def main():
    s = Solution()
    print(s.fib(3))


if __name__ == "__main__":
    main()
