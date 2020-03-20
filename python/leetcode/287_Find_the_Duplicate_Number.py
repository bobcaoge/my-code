# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        second = nums[nums[first]]
        while first != second:
            first = nums[first]
            second = nums[nums[second]]

        p1 = nums[0]
        p2 = first
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1


def main():
    s = Solution()
    print(s.findDuplicate([1,2,3,4,2]))


if __name__ == "__main__":
    main()
