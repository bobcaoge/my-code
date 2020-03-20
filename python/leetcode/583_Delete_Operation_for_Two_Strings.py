# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[200000]*(len(word2)+1) for _ in range(len(word1)+1)]
        dp[0][0] = 0
        for i in range(1, len(word1)+1):
            dp[i][0] = i
        for j in range(1, len(word2)+1):
            dp[0][j] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[-1][-1]


def main():
    s = Solution()
    print(s.minDistance("sea", "eat"))


if __name__ == "__main__":
    main()
