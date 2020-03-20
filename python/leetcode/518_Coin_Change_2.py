# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0:
            return 1
        if not coins or amount < 0:
            return 0
        dp = [[0]*(amount+1) for _ in range(len(coins))]
        # print(dp)
        for i in range(len(coins)):
            dp[i][0] = 1
        pos = 0
        while pos*coins[0] <= amount:
            dp[0][pos*coins[0]] = 1
            pos += 1

        for i in range(1, len(coins)):
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j]
                dp[i][j] += dp[i][j-coins[i]] if j-coins[i] >= 0 else 0
        return dp[-1][-1]


def main():
    s = Solution()
    print(s.change(2000, [1,2,5]))


if __name__ == "__main__":
    main()
