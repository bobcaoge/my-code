# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = ["Q", "W", "E", "R"]
        balanced_num = len(s)/4
        m = {}

        for char in chars:
            num = s.count(char)
            m[char] = max(num-balanced_num, 0)

        if max([value for key, value in m.items()]) == 0:
            return 0

        j = 0
        ret = 1<<31
        cur = collections.Counter()
        for i in range(len(s)):
            cur[s[i]] += 1

            while all([m[key] <= cur[key] for key in m]) and j <= i:
                ret = min(ret, i - j+1)
                cur[s[j]] -= 1
                j += 1
        return ret



def main():
    s = Solution()
    print(s.balancedString("QQQQ"))
    print(s.balancedString("QWER"))
    print(s.balancedString("QQER"))
    print(s.balancedString("WWEQERQWQWWRWWERQWEQ"))
    print(s.balancedString("QQQW"))


if __name__ == "__main__":
    main()
