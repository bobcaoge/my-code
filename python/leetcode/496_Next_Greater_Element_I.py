# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        table = {}
        for num in nums:
            if stack.__len__() == 0:
                stack.append(num)
            while len(stack) > 0 and  num > stack[-1]:
                table[stack.pop()] = num
            stack.append(num)
        ret = []
        for num in findNums:
            ret.append(table.get(num, -1))
        return ret






def main():
    s = Solution()
    print(s.nextGreaterElement([4,1,2], [1,3,4,2]))
    # print(s.nextGreaterElement([4,1,2], [9,8,7,6,5,10,1,2,3]))


if __name__ == "__main__":
    main()
