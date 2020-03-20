# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ret = 0
        m = {0:1}
        sum_of_left = 0
        for num in nums:
            sum_of_left += num
            ret += m.get(sum_of_left-k, 0)
            m[sum_of_left] = m.get(sum_of_left, 0) + 1
        return ret



def main():
    s = Solution()
    print(s.subarraySum([1,1,1],2))


if __name__ == "__main__":
    main()
