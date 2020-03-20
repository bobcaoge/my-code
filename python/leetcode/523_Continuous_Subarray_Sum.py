# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = set()
        cur_sum = 0
        pre = 0
        for num in nums:
            cur_sum += num
            mod = cur_sum % k if k != 0 else cur_sum
            if mod % k in s:
                return True
            s.add(pre)
            pre = mod
        return False

    def checkSubarraySum1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        memo = [0]*len(nums)
        old = 0
        for i in range(len(nums)):
            old += nums[i]
            memo[i] = old

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum_from_i_to_j = memo[j]- (memo[i-1] if i>0 else 0)
                if k == 0:
                    if sum_from_i_to_j == 0:
                        return True
                else:
                    if sum_from_i_to_j % k == 0:
                        return True
        return False



def main():
    s = Solution()
    # print(s.checkSubarraySum([23,2,4,6,7], 6))
    # print(s.checkSubarraySum([1,0], 6))
    print(s.checkSubarraySum([2,4], 6))


if __name__ == "__main__":
    main()
