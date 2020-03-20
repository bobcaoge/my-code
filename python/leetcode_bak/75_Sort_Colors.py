# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def change_nums(self, nums, start, end, num):
        while start < end:
            if nums[start] != num and nums[end] == num:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            if nums[start] == num:
                start += 1
            if nums[end] != num:
                end -= 1
        # print(nums)
        return start

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # set ret which is represented as num
        start = 0
        length = len(nums)
        end = length - 1
        start = self.change_nums(nums, start, end, 0)
        end = length - 1
        if nums[start] == 0:
            start += 1
        self.change_nums(nums,start, end, 1)
        print(nums)





def main():
    s = Solution()
    s.sortColors([2,0,2,1,1,0])
    s.sortColors([0,0,1])
    s.sortColors([2, 1, 2])
    s.sortColors([0,2,2,0])


if __name__ == "__main__":
    main()
