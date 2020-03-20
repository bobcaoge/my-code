# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def recursion(self, nums, start, end, turn):
        if start == end:
            return turn * nums[start]
        a = turn*nums[start] + self.recursion(nums, start+1, end, -turn)
        b = turn*nums[end] + self.recursion(nums, start, end-1, -turn)
        return max(a*turn, b*turn)*turn

    def PredictTheWinner2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.recursion(nums, 0, len(nums)-1, 1) >= 0
    def PredictTheWinner1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.first(nums, 0, len(nums)-1) > self.first(nums, 0, len(nums)-1)

    def first(self, nums, i, j):
        if i == j:
            return nums[i]
        return max(nums[i]+self.second(nums, i+1, j), nums[j]+self.second(nums, i, j-1))

    def second(self, nums, i, j):
        if i == j:
            return 0
        return min(self.first(nums, i+1, j), self.first(nums, i, j-1) )

    def PredictTheWinner_4(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = [[0]*len(nums) for _ in range(len(nums))]
        second = [[0]*len(nums) for _ in range(len(nums))]
        for j in range(len(nums)):
            first[j][j] = nums[j]
            for i in range(j-1, -1, -1):
                first[i][j] = max(nums[i]+second[i+1][j], nums[j]+second[i][j-1])
                second[i][j] = min(first[i+1][j],first[i][j-1])
        return first[0][-1] >= second[0][-1]

    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.dp(nums)
        # return self.dp_2(nums)

    def dp(self, nums):
        dp = [[0]*(len(nums)) for _ in range(len(nums)+1)]
        for i in range(len(nums)-1, -1, -1):
            dp[i][i] = nums[i]
            for j in range(i, len(nums)):
                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][-1] >= 0

    def dp_2(self, nums):
        dp = [0]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            dp[i] = nums[i]
            for j in range(i+1, len(nums)):
                print(i,j, end=" ,")
                dp[j] = max(nums[i]-dp[j], nums[j]-dp[j-1])
            print()
            print(dp)
        return dp[-1] >= 0

def main():
    s = Solution()
    # print(s.PredictTheWinner([1,5,2,4,6]))
    # print(s.PredictTheWinner([5,1]))
    print(s.PredictTheWinner([1,3,2]))


if __name__ == "__main__":
    main()
