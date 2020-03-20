# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [-2**32]+nums + [-2**32]
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
                return i-1



def main():
    s = Solution()


if __name__ == "__main__":
    main()
