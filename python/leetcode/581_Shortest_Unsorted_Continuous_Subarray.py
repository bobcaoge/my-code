# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findUnsortedSubarray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index_of_max = 0
        length = len(nums)
        r_edge = 0
        # 找出需要更改部分最大值的索引以及需要更改的右边界
        for i in range(1, length):
            # 小于最大值，更新边界
            if nums[i] < nums[index_of_max]:
                r_edge = i
            # 不符合升序，更新边界
            if nums[i] < nums[i-1]:
                r_edge = i
                # 判断是否需要更新最大值索引
                if nums[index_of_max] < nums[i-1]:
                    index_of_max = i-1

        print(index_of_max, r_edge)
        l_edge = 0
        index_of_min = length-1
        # 找出需要更改部分最小值的索引以及需要更改的右边界
        for i in range(length-2, -1, -1):
            if nums[i] > nums[index_of_min]:
                l_edge = i
            if nums[i] > nums[i+1]:
                l_edge = i
                if nums[index_of_min] > nums[i+1]:
                    index_of_min = i+1
        print(index_of_min, l_edge)
        return r_edge - l_edge + 1 if r_edge != l_edge else 0
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted([num for num in nums])
        l_edge = 0
        for i in range(len(nums)):
            if sorted_nums[i] != nums[i]:
                l_edge = i
                break
        r_edge = 0
        for i in range(len(nums)-1, -1, -1):
            if sorted_nums[i] != nums[i]:
                r_edge = i
                break
        return r_edge - l_edge + 1 if r_edge != l_edge else 0





def main():
    s = Solution()
    print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))


if __name__ == "__main__":
    main()
