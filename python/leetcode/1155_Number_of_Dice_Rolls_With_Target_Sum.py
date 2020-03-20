# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        f = min(f, target)
        mod = 10**9+7
        dp = [[0 for j in range(target+1)] for i in range(d)]
        for i in range(1, f+1):
            dp[0][i] = 1
        for i in range(1, d):
            for j in range(1, target+1):
                dp[i][j] = sum([dp[i-1][j-diff] for diff in range(1, f+1) if j-diff > 0]) % mod
        return dp[-1][-1]


def main():
    s = Solution()
    print(s.numRollsToTarget(1,6,3))
    print(s.numRollsToTarget(2,6,7))
    print(s.numRollsToTarget(2,5,10))
    print(s.numRollsToTarget(1,2,3))
    print(s.numRollsToTarget(30,30,500))
    print(s.numRollsToTarget(2,12,8))
    print(s.numRollsToTarget(3,18,10))



if __name__ == "__main__":
    main()
