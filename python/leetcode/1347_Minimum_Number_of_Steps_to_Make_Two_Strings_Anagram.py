# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = [0]*26
        for i, c in enumerate(s):
            m[ord(c)-97] += 1
            m[ord(t[i])-97] -= 1
        return sum([abs(x) for x in m])//2


def main():
    s = Solution()
    print(s.minSteps('bab', 'aab'))
    print(s.minSteps("leetcode", "practice"))


if __name__ == "__main__":
    main()
