# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        keep = nums[0]
        record = 0
        i = 1
        while i < len(nums):
            if keep == nums[i]:
                record += 1
                i += 1
            else:
                if record == 0:
                    keep = nums[i+1]
                    i += 2
                else:
                    record -= 1
                    i += 1

        return  keep


def main():
    s = Solution()


if __name__ == "__main__":
    main()
