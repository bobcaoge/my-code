# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import heapq

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        heap = []
        heapq.heappush(heap, [0, 0])
        target = len(nums)-1
        end = 0
        while heap:
            i, step = heapq.heappop(heap)
            if i + nums[i] >= target:
                return step+1
            for j in range(end+1, i+nums[i]+1):
                    heapq.heappush(heap, [j, step+1])
            end = max(end, i+nums[i])


def main():
    s = Solution()
    print(s.jump([2,3,1,1,4]))


if __name__ == "__main__":
    main()
