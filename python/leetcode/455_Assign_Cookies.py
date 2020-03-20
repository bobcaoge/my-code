# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        s.sort()
        g.sort()
        i = 0
        j = 0
        ret = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                ret += 1
                i += 1

            j += 1
        return ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
