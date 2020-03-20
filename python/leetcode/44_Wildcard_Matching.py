# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        num = 0
        for j in range(len(p)):
            num += 1 if p[j] == "*" else 0
            dp[0][j+1] = num == j+1

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == "?":
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == "*":
                    dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1]
                else:
                    dp[i+1][j+1] = dp[i][j] if p[j] == s[i] else False
        return dp[-1][-1]


def main():
    s = Solution()
    print(s.isMatch("ab", "a?"))
    print(s.isMatch("aaa", "*"))
    print(s.isMatch("cb", "?a"))
    print(s.isMatch("", "*"))
    print(s.isMatch("aaabababaaabaababbbaaaabbbbbbabbbbabbbabbaabbababab",
                    "*ab***ba**b*b*aaab*b"))
    print(s.isMatch("aa", "a"))
    print(s.isMatch("adceb", "a*c?b"))


if __name__ == "__main__":
    main()
