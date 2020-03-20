# /usr/bin/python3.6
# -*- coding:utf-8 -*-

import heapq
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        if len(prices)/2 <= k:
            return sum([max(0, prices[i]-prices[i-1]) for i in range(1, len(prices))])

        dp = [[[-1<<31, -1<<31] for _ in range(k+1)] for __ in range(len(prices))]
        dp[0][0][0] = -prices[0]
        dp[0][0][1] = 0
        for i in range(1, len(prices)):
            for j in range(k+1):
                if dp[i-1][j][0]  != -1<<31:
                    dp[i][j][0] = max(dp[i][j][0], dp[i-1][j][0])
                if dp[i-1][j][1] != -1<<31:
                    dp[i][j][0] = max(dp[i][j][0], dp[i-1][j][1]-prices[i])
                    dp[i][j][1] = max(dp[i][j][1], dp[i-1][j][1])
                if j-1>=0 and dp[i-1][j-1][0] != -1<<31:
                    dp[i][j][1] = max(dp[i][j][1], dp[i-1][j-1][0]+prices[i])
        return max([dp[-1][j][1] for j in range(k+1)])




def main():
    s = Solution()
    # print(s.maxProfit(prices=[2,4,1], k = 2))
    print(s.maxProfit(prices=[3,2,6,5,0,3], k = 2))


if __name__ == "__main__":
    main()
