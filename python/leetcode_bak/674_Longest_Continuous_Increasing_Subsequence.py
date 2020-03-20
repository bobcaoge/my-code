# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findLengthOfLCIS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_length = 0
        cur = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                cur += 1
            else:
                max_length = cur if cur > max_length else max_length
                cur = 1
        return max_length if cur < max_length else cur

    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_length = 0
        cur = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                cur += 1
            else:
                max_length = max(cur, max_length)
                cur = 1
        return max(cur, max_length)



def main():
    s = Solution()


if __name__ == "__main__":
    main()
