# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(word2)+1)] for __ in range(len(word1)+1)]
        for i in range(len(word1)):
            dp[i+1][0] = i+1
        for j in range(len(word2)):
            dp[0][j+1] = j+1

        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j])+1
        return dp[-1][-1]


def main():
    s = Solution()
    print(s.minDistance("word1", "word2"))


if __name__ == "__main__":
    main()
