# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while nums[i] != i+1 and len(nums) >= nums[i] > 0 and nums[nums[i]-1] != nums[i]:
                y = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = y
        for i, num in enumerate(nums):
            if i+1 != num:
                return i+1
        return len(nums)+1


def main():
    s = Solution()
    print(s.firstMissingPositive([1, 2, 0]))
    print(s.firstMissingPositive([0, 1, 2]))
    print(s.firstMissingPositive([1,4,3,0]))


if __name__ == "__main__":
    main()
