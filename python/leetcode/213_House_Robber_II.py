# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # rob the first house
        last_robbed = nums[0]
        last_not_robbed = 0
        for money in nums[1:len(nums)-1]:
            cur_robed = max(last_not_robbed+money, last_robbed)
            cur_not_robbed = max(last_robbed, last_not_robbed)
            last_not_robbed = cur_not_robbed
            last_robbed = cur_robed
        ret = max(last_not_robbed, last_robbed)
        # do not rob the first house
        last_robbed = 0
        last_not_robbed = 0
        for money in nums[1:]:
            cur_robed = max(last_not_robbed+money, last_robbed)
            cur_not_robbed = max(last_robbed, last_not_robbed)
            last_not_robbed = cur_not_robbed
            last_robbed = cur_robed
        ret = max(last_not_robbed, last_robbed, ret)
        return ret


def main():
    s = Solution()
    print(s.rob([1,2,3]))
    print(s.rob([3,1,2,3]))
    print(s.rob([1,1,2,3]))
    print(s.rob([1,2,3,1]))
    print(s.rob([2,3,2]))


if __name__ == "__main__":
    main()
