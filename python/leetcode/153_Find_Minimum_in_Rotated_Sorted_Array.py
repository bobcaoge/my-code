# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        mid = (start+end)/2
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
            if nums[mid] >= nums[start]:
                start = mid+1
            else:
                end = mid
            mid = (start+end)/2
        return nums[start]


def main():
    s = Solution()
    print(s.findMin([2,1]))


if __name__ == "__main__":
    main()
