# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(t)+1)] for __ in range(len(s)+1)]
        dp[0][0] = 1
        for i in range(len(s)):
            dp[i+1][0] = 1

        for i in range(len(s)):
            for j in range(len(t)):

                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
                else:
                    dp[i+1][j+1] = dp[i][j+1]
        return dp[-1][-1]


def main():
    s = Solution()
    print(s.numDistinct("rabbbit", "rabbit"))
    print(s.numDistinct("babgbag", "bag"))
    print(s.numDistinct("ababababaababababababab",
                        "aba"))


if __name__ == "__main__":
    main()
