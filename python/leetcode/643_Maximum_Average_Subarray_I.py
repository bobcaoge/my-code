# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_sum = sum(nums[:k])
        cur_sum = max_sum
        for i in range(k, len(nums)):
            cur_sum = cur_sum - nums[i-k] + nums[i]
            max_sum = cur_sum if cur_sum > max_sum else  max_sum
        return max_sum*1.0/k


def main():
    s = Solution()


if __name__ == "__main__":
    main()
