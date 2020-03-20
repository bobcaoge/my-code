# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
