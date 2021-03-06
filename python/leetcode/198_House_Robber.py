# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution:
    def buffer(self,nums, adjoin):
        """
        递归，方法效率太低
        :param nums:
        :param adjoin:
        :return:
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if adjoin == 2:
            return nums[0] + self.buffer(nums[2:], 0)
        else:
            first = nums[0] + self.buffer(nums[2:], 0)
            second = self.buffer(nums[1:], adjoin+1)
            return first if first >second else second

    def rob11(self, nums):
        return self.buffer(nums, 0)

    def rob1(self, nums):
        not_robbed_previous = 0
        robbed_previous = 0
        for num in nums:
            current_robbed = not_robbed_previous + num
            current_not_robbed = max(not_robbed_previous, robbed_previous)
            not_robbed_previous = current_not_robbed
            robbed_previous = current_robbed
        return max(robbed_previous, not_robbed_previous)

    def rob(self, nums):
        not_robbed_previous = [0]
        robbed_previous = [0]
        current_robbed = [0]
        current_not_robbed = [0]
        for num in nums:
            current_robbed[0] = not_robbed_previous[0] + num
            current_not_robbed[0] = max(not_robbed_previous[0], robbed_previous[0])
            not_robbed_previous[0] = current_not_robbed[0]
            robbed_previous[0] = current_robbed[0]
        return max(robbed_previous[0], not_robbed_previous[0])



def main():
    s = Solution()
    print(s.rob([3,6,2,7,8,1,9,9,10,2]))
    print(s.rob([6,7,7,6,5,6,8,7,6,5,9,10,0,10,20,6,7,6,6]))


if __name__ == "__main__":
    main()
