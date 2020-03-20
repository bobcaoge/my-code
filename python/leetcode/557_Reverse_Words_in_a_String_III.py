# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(x[-1::-1] for x in s.split(" "))


def main():
    s = Solution()


if __name__ == "__main__":
    main()
