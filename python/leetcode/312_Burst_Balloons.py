# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(len(nums))] for __ in range(len(nums))]
        for i in range(len(nums)-1,-1, -1):
            for j in range(i, len(nums)):
                for k in range(i, j+1):
                    left = nums[i-1] if i > 0 else 1
                    right = nums[j+1] if j+1 < len(nums) else 1
                    dp[i][j] = max(dp[i][j], dp[i][k-1]+left*nums[k]*right+(dp[k+1][j] if k+1 <=j else 0))
        return dp[0][-1]


def main():
    s = Solution()
    print(s.maxCoins([3,1,5,8]))
    print(s.maxCoins([1]))
    print(s.maxCoins([3,1,5,8,3,1,5,8,3,1,5,8,3,1,5,8,3,1,5,8,3,1]))


if __name__ == "__main__":
    main()
