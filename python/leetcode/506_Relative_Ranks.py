# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import copy

class Solution(object):
    def findRelativeRanks1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        # print(nums)
        first = [-1, 0]
        second =[-1, 0]
        third = [-1, 0]
        for index, num in enumerate(nums):
            # num = int(num)
            if num > first[0]:
                third = second
                second = first
                first = [num, index]
            elif num > second[0]:
                third = second
                second = [num, index]
            elif num > third[0]:
                third = [num, index]
        length = len(nums)
        # print(first, second, third)
        buffer = copy.deepcopy(nums)
        buffer = [[x, index] for index, x in enumerate(buffer)]
        try:
            buffer.remove(first)
            buffer.remove(second)
            buffer.remove(third)
        except:
            pass
        buffer.sort()
        print(buffer)
        length_buffer = len(buffer)
        for index in range(length_buffer):
            item = buffer[length_buffer-1-index]
            nums[item[1]] = str(4+index)

        if length >= 1:
            nums[first[1]] = "Gold Medal"
        if length >= 2:
            nums[second[1]] = "Silver Medal"
        if length >= 3:
            nums[third[1]] = "Bronze Medal"
        print(nums)
        return nums
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        buffer = [[num, index] for index, num in enumerate(nums)]
        buffer.sort()
        length = len(buffer)
        try:
            nums[buffer[-1][1]] = "Gold Medal"
            nums[buffer[-2][1]] = "Silver Medal"
            nums[buffer[-3][1]] = "Bronze Medal"
        except:
            pass
        for i in range(length-3):
            item = buffer[length - 4 - i]
            nums[item[1]] = str(4 + i)
        print(nums)
        return nums


def main():
    s = Solution()
    s.findRelativeRanks([5,4,3,2,1])
    s.findRelativeRanks([])
    s.findRelativeRanks([10, 3,  4])


if __name__ == "__main__":
    main()
