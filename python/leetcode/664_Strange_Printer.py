# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):

    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [[]]*len(s)
        m = collections.defaultdict(list)
        for i in range(len(s)-1, -1, -1):
            dp[i] = m[s[i]]
            m[s[i]].append(i)
        memo = {}
        def dfs(begin, end, cur_char):
            if begin > end:
                return 0
            flag = False
            if cur_char == s[begin]:
                flag = True
            if memo.get((begin, end, flag), None) is None:
                if s[begin] == cur_char:
                    ret = dfs(begin+1, end, cur_char)
                else:
                    ret = dfs(begin+1, end, s[begin])+1
                    for mid in dp[begin-1]:
                        ret = min(ret,
                               dfs(begin+1, mid-1, s[begin])+1+dfs(max(mid+1, begin+1), end, cur_char))
                memo[(begin, end, flag)] = ret
            return memo[(begin, end, flag)]
        ret = dfs(0, len(s)-1, s[0])+1
        return ret



def main():
    s = Solution()
    print(s.strangePrinter('abcdabcddcbadcba'))
    print(s.strangePrinter('ababab'))
    print(s.strangePrinter("dddccbdbababaddcbcaabdbdddcccddbbaabddb"))
    print(s.strangePrinter('abbbaa'))
    print(s.strangePrinter('aaabbb'))
    print(s.strangePrinter('aba'))
    print(s.strangePrinter('aasdlfjdkdfvsgdfgkdjfbxcbsdjgf'))
    print(s.strangePrinter("iwxryyidulizkmblonwtzkkcvayqectpariyrqdldmmnynaoawjaivedwcwcgrrgibhbtkmwwyjwnjnohyqsuuxqwvufnmlxnszh"))


if __name__ == "__main__":
    main()
