# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = collections.defaultdict(int)
        before = 0
        ret = 0
        for i, c in enumerate(s):
            m[c] += 1
            if len(m) == 3:
                while len(m) == 3:
                    ret += len(s)-i
                    m[s[before]] -= 1
                    if m[s[before]] == 0:
                        del m[s[before]]
                    before += 1
        return ret




def main():
    s = Solution()
    print(s.numberOfSubstrings('abcabc'))


if __name__ == "__main__":
    main()
