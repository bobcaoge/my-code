# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            if s[i] == "*":
                dp[i][i] = True
            for j in range(i+1, len(s)):
                if j-i == 1:
                    if s[i] in ("(", "*") and s[j] in (")", "*"):
                        dp[i][j] = True
                    continue
                if s[i] in ("(", "*") and s[j] in (")", "*"):
                    dp[i][j] = dp[i+1][j-1]
                for k in range(i, j):
                    if dp[i][j]:
                        break
                    dp[i][j] = dp[i][k] and dp[k+1][j]
                # print(s[i:j], dp[i][j])
        return dp[0][-1]



def main():
    s = Solution()
    print(s.checkValidString("(*)"))
    print(s.checkValidString("(()*"))
    print(s.checkValidString("(*)**)"))



if __name__ == "__main__":
    main()
