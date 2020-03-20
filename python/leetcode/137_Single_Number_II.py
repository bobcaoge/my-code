# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = 0
        for num in nums:
            b = b ^ num & ~a
            a = a ^ num & ~b
        return a|b


def main():
    s = Solution()


if __name__ == "__main__":
    main()
