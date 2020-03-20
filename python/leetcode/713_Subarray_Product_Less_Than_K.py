# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        end = 0
        product = 1
        ret = 0
        while end < len(nums):

            product *= nums[end]
            while product >= k and start <= end:
                product /= nums[start]
                start += 1
            end += 1
            ret += end-start
        return ret


def main():
    s = Solution()
    print(s.numSubarrayProductLessThanK([10,5,2,6], 100))
    print(s.numSubarrayProductLessThanK([10,5,100,2,6], 100))


if __name__ == "__main__":
    main()
