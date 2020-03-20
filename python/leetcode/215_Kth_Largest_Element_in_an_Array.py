# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)[-1::-1]

        return nums[k-1] if k-1 < len(nums) else nums[-1]



def main():
    s = Solution()


if __name__ == "__main__":
    main()
