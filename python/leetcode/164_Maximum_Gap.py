# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import heapq

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        heapq.heapify(nums)
        last = heapq.heappop(nums)
        ret = 0
        while nums:
            cur = heapq.heappop(nums)
            ret = max(ret, cur-last)
            last = cur
        return ret



    def maximumGap_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums.sort()
        return min([nums[i]-nums[i-1] for i in range(1, len(nums))])




def main():
    s = Solution()


if __name__ == "__main__":
    main()
