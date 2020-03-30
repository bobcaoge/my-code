# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import functools


class Solution(object):
    def findGoodStrings(self, n, s1, s2, evil):
        """
        :type n: int
        :type s1: str
        :type s2: str
        :type evil: str
        :rtype: int
        """
        def kmp(s):
            next_arr = [0]*len(s)
            next_arr[0] = -1
            cn = 0
            pos = 2
            while pos < len(s):
                if s[pos-1] == s[cn]:
                    next_arr[pos] = cn+1
                    cn += 1
                    pos += 1
                elif cn > 0:
                    cn = next_arr[cn]
                else:
                    next_arr[pos] = 0
                    pos += 1
            return next_arr
        next_arr = kmp(evil)
        mod = 10**9+7

        memo = {}
        @functools.lru_cache(None)
        def dfs(s, same_length):
            flag1 = s == s1[:len(s)]
            flag2 = s == s2[:len(s)]
            if not memo.get((flag1, flag2, same_length, len(s)), None):
                if same_length == len(evil):
                    return 0
                if s.endswith(evil):
                    print(s)
                if len(s) == n:
                    return 1
                ret = 0
                for i in range(26):
                    next_s = s+str(chr(i+97))
                    if s1[:len(next_s)] <= next_s <= s2[:len(next_s)]:
                        n_same_length = same_length
                        while n_same_length > 0 and evil[n_same_length] != chr(i+97):
                            n_same_length = next_arr[n_same_length]
                        ret += dfs(next_s, n_same_length if evil[n_same_length] != chr(i+97) else n_same_length+ 1)
                ret =ret % mod
                memo[(flag1, flag2, same_length, len(s))] = ret
            return memo[(flag1, flag2, same_length, len(s))]
        return dfs('', 0)






def main():
    s = Solution()
    # print(s.findGoodStrings(n = 2, s1 = "aa", s2 = "da", evil = "b"))
    # print(s.findGoodStrings(n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"))
    # print(s.findGoodStrings(n = 2, s1 = "gx", s2 = "gz", evil = "x"))
    print(s.findGoodStrings(3,"aaa","zzz","ab"))
    print(s.findGoodStrings(9,"aaaaaaaaa","zzzzzzzzz","ab"))

if __name__ == "__main__":
    main()
