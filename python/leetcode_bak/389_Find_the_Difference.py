# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        m1 = [0]*26

        for c in t:
            m1[ord(c)-97] += 1
        for c in s:
            m1[ord(c) - 97] -= 1

        for index, value in enumerate(m1):
            if value == 1:
                return str(chr(index+97))


def main():
    s = Solution()


if __name__ == "__main__":
    main()
