# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    count = 0
    def recursion(self, nums, pos, cur_sum, S):
        if pos == len(nums):
            if cur_sum == S:
                self.count += 1
            return
        self.recursion(nums, pos+1, cur_sum+nums[pos], S)
        self.recursion(nums, pos+1, cur_sum-nums[pos], S)

    def findTargetSumWays2(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.count = 0
        self.recursion(nums, 0, 0, S)
        return self.count

    def findTargetSumWays1(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        memo = {}
        memo[0] = 1
        for num in nums:
            buff = {}
            for cur_sum, count in memo.items():
                buff[cur_sum+num] = buff.get(cur_sum+num, 0) + count
                buff[cur_sum-num] = buff.get(cur_sum-num, 0) + count
            memo = buff
        return memo.get(S, 0)

    def findTargetSumWays4(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = [[0]*2001 for _ in range(len(nums))]
        dp[0][-nums[0]+1000] = 1
        dp[0][nums[0]+1000] += 1
        for i in range(1, len(nums),1):
            for j in range(-1000, 1001,1):
                if dp[i-1][j+1000] > 0:
                    dp[i][j+nums[i]+1000] += dp[i-1][j+1000]
                    dp[i][j-nums[i]+1000] += dp[i-1][j+1000]
        return 0 if S > 1000 else dp[len(nums)-1][S+1000]

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = [0]*2001
        dp[-nums[0]+1000] = 1
        dp[nums[0]+1000] += 1
        for i in range(1, len(nums), 1):
            buff = [0]*2001
            for j in range(-1000, 1001, 1):
                if dp[j+1000] > 0:
                    buff[j+nums[i]+1000] += dp[j+1000]
                    buff[j-nums[i]+1000] += dp[j+1000]
            dp = buff
        return 0 if S > 1000 else dp[S+1000]



def main():
    s = Solution()
    print(s.findTargetSumWays([1,1,1,1,1], 3))
    print(s.findTargetSumWays([45,18,27,39,42,19,1,35,32,16,7,6,25,41,27,18,38,6,42,10], 49))


if __name__ == "__main__":
    main()
