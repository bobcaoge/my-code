# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        def manager(length):
            m = collections.Counter()
            r = collections.Counter(s[:length-1])
            for i in range(length, len(s)+1):
                r[s[i-1]] += 1
                if i-length-1 >= 0:
                    r[s[i-length-1]] -= 1
                    if r[s[i-length-1]] == 0:
                        del r[s[i-length-1]]
                if len(r) <= maxLetters:
                    m[s[i-length:i]] += 1
            if not m:
                return 0
            return max([x for _, x in m.items()])
        for i in range(minSize, maxSize+1):
            ret = manager(i)
            if ret > 0:
                return ret
        return 0


def main():
    s = Solution()
    print(s.maxFreq(s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4))
    print(s.maxFreq(s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3))
    print(s.maxFreq( s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3))
    print(s.maxFreq(s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3))


if __name__ == "__main__":
    main()
