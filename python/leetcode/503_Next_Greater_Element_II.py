# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        stack = []
        ret = [-1]*len(nums)

        for index, num in enumerate(nums):
            while stack and stack[-1][0] < num:
                ret[stack[-1][1]] = num
                stack.pop()
            stack.append([num, index])

        for num in nums:
            while stack and stack[-1][0] < num:
                ret[stack[-1][1]] = num
                stack.pop()
            if not stack:
                break
        return ret



def main():
    s = Solution()
    print(s.nextGreaterElements([100,1,11,1,120,111,123,1,-1,-100]))
    print(s.nextGreaterElements([1,2,1,3,4,2,8,3,7,4,8,4,4]))
    print(s.nextGreaterElements([5,4,3,2,1]))
    print(s.nextGreaterElements([1,2,3,2,1]))


if __name__ == "__main__":
    main()
