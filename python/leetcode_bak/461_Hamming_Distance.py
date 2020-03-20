# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def hammingDistance1(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count("1")
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        num = x ^ y
        ret = 0
        while num != 0:
            ret += 1
            num &= num-1
        return ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
