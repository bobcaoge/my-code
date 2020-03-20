# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [False]*len(s)
        ret = 0
        for i in range(len(s)-1, -1, -1):
            ret += 1
            buff = [False]*len(s)
            buff[i] = True
            for j in range(i+1, len(s)):
                if i+1 <= j-1 and dp[j-1] and s[i] == s[j] or i+1 > j-1 and s[i] == s[j]:
                    buff[j] = True
                    ret += 1
            dp = buff
        # print(dp)
        return ret

    def countSubstrings1(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[False]*len(s) for _ in range(len(s))]
        ret = 0
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = True
            ret += 1
            for j in range(i+1, len(s)):
                if i+1 <= j-1 and dp[i+1][j-1] and s[i] == s[j] or i+1 > j-1 and s[i] == s[j]:
                    dp[i][j] = True
                    ret += 1
        # print(dp)
        return ret



def main():
    s = Solution()
    print(s.countSubstrings("abc"))
    print(s.countSubstrings("aaa"))
    print(s.countSubstrings("abcaaabbbcccabccaaababcbabljflasdjfwioaeroqehgladjfgdlkajgdzlfjcmbakdjfalkhlfjsjg"))


if __name__ == "__main__":
    main()
