# /usr/bin/python2.7
# -*- coding:utf-8 -*-


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        mid = (end + start) / 2
        while start <= end:
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
                mid = (end + start) / 2
            else:
                start = mid + 1
                mid = (end + start) / 2
        return -1



def main():
    s = Solution()


if __name__ == "__main__":
    main()
