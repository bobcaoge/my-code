# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length % 2 == 0:
            sum_ = length / 2 * (1 + length)
        else:
            sum_ = (length + 1) / 2 * length

        return sum_ - sum(nums)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
