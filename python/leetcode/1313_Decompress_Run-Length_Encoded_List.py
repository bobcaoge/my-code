# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in range(0, len(nums), 2):
            a = nums[i]
            b = nums[i+1]
            ret.extend([b]*a)
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
