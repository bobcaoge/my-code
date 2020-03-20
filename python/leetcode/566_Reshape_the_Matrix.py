# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums or r*c != len(nums)*len(nums[0]):
            return nums
        buffer = []
        for num in nums:
            buffer.extend(num)
        nums = buffer
        ret = []
        end = c
        while end <= len(nums):
            ret.append(nums[end-c:end])
            end += c
        return ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
