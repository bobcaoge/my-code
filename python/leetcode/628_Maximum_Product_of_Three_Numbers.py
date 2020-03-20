# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maximumProduct1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-3]*nums[-2]*nums[-1])

    def maximumProduct(self, nums):

        minus_min1 = 2**32
        minus_min2 = 2**32
        plus_max1 = -2**32
        plus_max2 = -2**32
        plus_max3 = -2**32
        for num in nums:
            if num > plus_max1:
                plus_max3 = plus_max2
                plus_max2 = plus_max1
                plus_max1 = num
            elif num > plus_max2:
                plus_max3 = plus_max2
                plus_max2 = num
            elif num > plus_max3:
                plus_max3 = num

            if num < minus_min1:
                minus_min2 = minus_min1
                minus_min1 = num
            elif num < minus_min2:
                minus_min2 = num
        print(minus_min1, minus_min2, plus_max3, plus_max2, plus_max1)
        return max(minus_min2*minus_min1*plus_max1, plus_max3*plus_max2*plus_max1)


def main():
    s = Solution()
    # print(s.maximumProduct([-1,-2,-3]))
    print(s.maximumProduct([-1000,-1000,-1000]))


if __name__ == "__main__":
    main()
