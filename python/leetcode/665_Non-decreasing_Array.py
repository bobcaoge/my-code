# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = [-2**32] + nums + [2**32]
        record = 0
        i = 1
        old = nums[0]
        while i < len(nums) and record <= 1:
            # print(old, nums[i], i, record)
            if old > nums[i]:
                record += 1
                if nums[i-2] <= nums[i]:
                    old = nums[i-2]
                if nums[i] < nums[i-2]:
                    i += 1
            else:
                old = nums[i]
                i += 1
        return record <= 1


def main():
    s = Solution()
    print(s.checkPossibility([4,2,1]))
    print(s.checkPossibility([4,2,3]))
    print(s.checkPossibility([-1, 4,2,3]))
    print(s.checkPossibility([2,3,3,3,2,4]))


if __name__ == "__main__":
    main()
