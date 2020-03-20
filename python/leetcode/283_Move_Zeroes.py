# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        zero = [0]*length
        cur = 0
        for index, num in enumerate(nums):
            if num == 0:
                cur += 1
            else:
                zero[index] = cur

        for index, num in enumerate(nums):
            if num != 0:
                num[index-zero[index]] = num
        for i in range(cur):
            nums[length-i] = 0
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        cur = 0
        for index, num in enumerate(nums):
            if num == 0:
                cur += 1
            else:
                nums[index-cur] = num

        for i in range(cur):
            nums[length-i-1] = 0



def main():
    s = Solution()


if __name__ == "__main__":
    main()
