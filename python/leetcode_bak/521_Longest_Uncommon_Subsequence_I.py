# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return max(len(a), len(b))


def main():
    s = Solution()


if __name__ == "__main__":
    main()
