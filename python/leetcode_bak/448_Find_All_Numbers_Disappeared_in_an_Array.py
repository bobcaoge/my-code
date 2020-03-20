# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


def main():
    s = Solution()


if __name__ == "__main__":
    main()
