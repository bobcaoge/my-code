# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        product = [0]*length
        last = 1
        for index, num in enumerate(nums):
            last *= num
            product[index] = last

        last = 1
        for index in range(length-1, 0, -1):
            product[index] = product[index-1]*last
            last *= nums[index]
        product[0] = last
        return product

    def productExceptSelf1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product_from_left_to_right = []
        last = 1
        for index, num in enumerate(nums):
            last *= num
            product_from_left_to_right.append(last)
        product_from_right_to_left = []
        last = 1
        for index in range(len(nums)-1, -1, -1):
            last *= nums[index]
            product_from_right_to_left.append(last)
        product_from_right_to_left = product_from_right_to_left[-1::-1]

        ret = [1]*len(nums)
        ret[0] = product_from_right_to_left[1]
        ret[-1] = product_from_left_to_right[-2]
        for i in range(1, len(nums)-1):
            ret[i] = product_from_left_to_right[i-1]*product_from_right_to_left[i+1]
        return ret


def main():
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))
    print(s.productExceptSelf([0,0]))


if __name__ == "__main__":
    main()
