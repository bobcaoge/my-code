# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        length = len(nums)
        while index < length:
            # 判断是否相等
            # 相等
            if nums[index] == target:
                return index
            # 判断是否符合位置
            else:
                if index == 0:
                    if target < nums[index]:
                        return 0
                else:
                    if nums[index-1] <= target <= nums[index]:
                        return index
                index += 1
        if index == length:
            if target > nums[length-1]:
                return length
        return -1




def main():
    s = Solution()
    # print(s.searchInsert([1,3,5,6],5))
    # print(s.searchInsert([1,3,5,6],2))
    print(s.searchInsert([1,3,5,6],7))
    # print(s.searchInsert([1,3,5,6],0))


if __name__ == "__main__":
    main()
