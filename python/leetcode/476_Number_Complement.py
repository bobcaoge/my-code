# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ret = 0
        base = 0
        while num != 0:
            ret += 2 ** base * abs(num % 2 - 1)
            num = int(num / 2)
            base += 1
        return ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
