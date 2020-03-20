# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        # 第i轮 尾数是j 且连续出现k次
        mod = 10**9+7
        dp = [[[0 for k in range(max(rollMax)+1)] for j in range(6)] for i in range(n)]

        for i in range(6):
            dp[0][i][1] = 1

        for i in range(1, n):
            for j in range(6):
                for k in range(1, max(rollMax)+1):
                    if k == 1:
                        dp[i][j][k] = sum([sum(dp[i-1][x]) for x in range(6) if x != j]) % mod
                    else:
                        dp[i][j][k] = dp[i-1][j][k-1] if k-1 < rollMax[j] else 0
        return sum([sum(dp[n-1][j]) for j in range(6)]) % mod


def main():
    s = Solution()
    print(s.dieSimulator(2, [1,1,2,2,2,3]))
    print(s.dieSimulator(n = 2, rollMax = [1,1,1,1,1,1]))
    print(s.dieSimulator( n = 3, rollMax = [1,1,1,2,2,3]))
    print(s.dieSimulator(2000,[10,10,10,10,10,10]))


if __name__ == "__main__":
    main()
