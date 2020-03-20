# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0]*len(s)
        for i, c in enumerate(s):
            if s[:i+1] == s[:i+1][::-1]:
                continue
            dp[i] = i+1
            for j in range(1, i+1):
                if s[j:i+1] == s[j:i+1][::-1]:
                    dp[i] = min(dp[i], dp[j-1]+1)
        return dp[-1]



def main():
    s = Solution()
    print(s.minCut("aab"))
    print(s.minCut("abaaabsdkfsdlfj"))


if __name__ == "__main__":
    main()
