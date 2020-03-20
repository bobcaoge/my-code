# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        memo = {1:[1]}

        def f(n):
            if n not in memo:
                odd = f((n+1)//2)
                even = f(n//2)
                memo[n] = [2*x-1 for x in odd] + [2*x for x in even]
            return memo[n]
        return f(N)


def main():
    s = Solution()
    print(s.beautifulArray(3))


if __name__ == "__main__":
    main()
