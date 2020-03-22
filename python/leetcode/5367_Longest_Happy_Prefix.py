# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """

        for i in range(len(s)-1, 0, -1):
            if s.endswith(s[:i]):
                return s[:i]
        return ''


def main():
    s = Solution()
    print(s.longestPrefix('level'))


if __name__ == "__main__":
    main()
