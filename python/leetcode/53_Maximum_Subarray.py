# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]
        cur_num = nums[0]
        ret_num = cur_num
        index = 1
        while index < length:
            # print(cur_num, ret_num)
            if nums[index] >= 0:
                if cur_num > 0:
                    cur_num += nums[index]
                else:
                    cur_num = nums[index]
                    if cur_num > ret_num:
                        ret_num = cur_num
            else:
                # 更新ret_num
                if cur_num > ret_num:
                    ret_num = cur_num
                # 更新cur_num
                if cur_num + nums[index] <= 0:
                    cur_num = nums[index]
                else:
                    cur_num += nums[index]
            index += 1
        if cur_num > ret_num:
            ret_num = cur_num
        if nums[-1] > ret_num:
            ret_num = nums[-1]
        return ret_num


def main():
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(s.maxSubArray([-2, -1]))
    print(s.maxSubArray([-2, 1]))


if __name__ == "__main__":
    main()
