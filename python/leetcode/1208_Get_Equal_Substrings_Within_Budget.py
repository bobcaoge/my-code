# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        cur_cost = 0
        j = 0
        ret = 0
        for i in range(len(s)):
            cur_cost += abs(ord(s[i]) - ord(t[i]))
            while cur_cost > maxCost:
                cur_cost -= abs(ord(s[j]) - ord(t[j]))
                j += 1
            ret = max(ret, i - j + 1)
        return ret




def main():
    s = Solution()
    print(s.equalSubstring("abcd", "cdef", 3))
    print(s.equalSubstring("abcd", "bcde", 3))


if __name__ == "__main__":
    main()
