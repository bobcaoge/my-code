# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_list = []
        t_list = []
        for c in s:
            s_list.append(c)
        for c in t:
            t_list.append(c)
        s_list.sort()
        t_list.sort()
        for index, c in enumerate(s_list):
            if c != t_list[index]:
                return False
        return True


def main():
    s = Solution()
    s.isAnagram("hello", "world")

if __name__ == "__main__":
    main()
