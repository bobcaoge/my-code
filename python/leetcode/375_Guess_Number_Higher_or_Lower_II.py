# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for x in range(n+1)]
        for j in range(2, n+1):
            for i in range(j-1, 0, -1):
                if j - i == 1:
                    dp[i][j] = i
                else:
                    cur = 2**31
                    for k in range(i+1, j):
                        local = k + max(dp[i][k-1], dp[k+1][j])
                        cur = min(local, cur)
                    dp[i][j] = cur

        return dp[1][n]


def main():
    s = Solution()
    print(s.getMoneyAmount(10))



if __name__ == "__main__":
    main()
