# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        stack = []
        for i in range(k):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            stack.append(i)
        ret = []
        ret.append(nums[stack[0]])
        for i in range(k, len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            stack.append(i)
            while stack and stack[0] < i-k+1:
                stack.pop(0)
            ret.append(nums[stack[0]])
        return ret


def main():
    s = Solution()
    print(s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7],  k = 3))


if __name__ == "__main__":
    main()
