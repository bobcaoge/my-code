# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        stack = [-1]
        ret = 0
        for i, num in enumerate(nums):
            if num % 2 == 1:
                stack.append(i)
            if len(stack) > k:
                ret += stack[-k] - stack[-k-1]
        return ret
def main():
    s = Solution()
    print(s.numberOfSubarrays([1,1,2,1,1], 3))
    print(s.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2],
    2))


if __name__ == "__main__":
    main()
