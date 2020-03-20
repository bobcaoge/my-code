# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        while start < end:
            # if s[start] != s[end]:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


def main():
    s = Solution()


if __name__ == "__main__":
    main()
