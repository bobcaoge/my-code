# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        ret = 0
        while i < len(nums):
            ret += nums[i]
            i += 2
        return ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
