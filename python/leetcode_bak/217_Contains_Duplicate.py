# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = nums[0]
        for index in range(1, len(nums)):

            if a^nums[index] == (a - nums[index])^nums[index]:
                return False
            a = a+nums[index]
        return True




def main():
    s = Solution()
    print(s.containsDuplicate([1,2,3,1]))
    print(s.containsDuplicate([1,1]))
    print(s.containsDuplicate([3,3]))


if __name__ == "__main__":
    main()
