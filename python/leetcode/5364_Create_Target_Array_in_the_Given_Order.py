# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target



def main():
    s = Solution()


if __name__ == "__main__":
    main()
