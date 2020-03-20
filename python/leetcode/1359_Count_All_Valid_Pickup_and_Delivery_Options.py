# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9+7
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]*(2*i-1)*i % mod
        return dp[n]


def main():
    s = Solution()
    print(s.countOrders(2))
    print(s.countOrders(3))


if __name__ == "__main__":
    main()
