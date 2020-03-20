# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0])+"/"+str(nums[1])
        ret = str(nums[0])+"/("
        for i in range(1, len(nums)):
            ret += str(nums[i])+"/"
        return ret[:-1]+")"



def main():
    s = Solution()


if __name__ == "__main__":
    main()
