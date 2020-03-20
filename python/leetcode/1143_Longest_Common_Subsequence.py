# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        length1 = len(text1)
        length2 = len(text2)
        dp = [[0 for j in range(length2)] for i in range(length1)]
        if text1[0] == text2[0]:
            dp[0][0] = 1

        for i in range(1, length1):
            dp[i][0] = max(dp[i-1][0], 1 if text1[i] == text2[0] else 0)

        for j in range(1, length2):
            dp[0][j] = max(dp[0][j-1], 1 if text2[j] == text1[0] else 0)

        for i in range(1, length1):
            for j in range(1, length2):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]


def main():
    s = Solution()
    print(s.longestCommonSubsequence("abc", "bc"))


if __name__ == "__main__":
    main()
