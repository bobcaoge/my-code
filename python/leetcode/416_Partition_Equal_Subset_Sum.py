# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    flag = False
    values = {} # 记忆已经查找过的数据
    # (start, cur_value)
    def recursion(self, nums, start, total):
        if self.flag or total < 0:
            return
        if total == 0:
            self.flag = True
        for i in range(start, len(nums)):
            if not self.values.get((i, total), False):
                self.values[(i, total)] = 1
                self.recursion(nums, i+1, total)
            if not self.values.get((i, total-nums[i]), False):
                self.values[(i, total-nums[i])] = 1
                self.recursion(nums, i+1, total-nums[i])

    def canPartition1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_of_sum = sum(nums)
        if num_of_sum % 2 != 0:
            return False
        total = num_of_sum / 2

        values = set()
        values.add((total, 0))
        while values:
            cur_total, start = values.pop()
            print(cur_total, start)
            if cur_total > 0 and start < len(nums):
                next_total = cur_total-nums[start]
                if next_total == 0 or total == 0:
                    return True
                values.add((next_total, start+1))
                values.add((cur_total, start+1))
        return False

    def canPartition2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_of_sum = sum(nums)
        if num_of_sum % 2 != 0:
            return False
        total = num_of_sum / 2
        dp = [[False]*(total+1) for _ in range(len(nums)+1)]

        for i in range(len(nums)+1):
            dp[i][0] = True
        for i in range(1, len(nums)+1):
            for j in range(1, total+1):
                if dp[i-1][j] or j-nums[i-1] >= 0 and dp[i-1][j-nums[i-1]]:
                    dp[i][j] = True

        return dp[len(nums)][total]

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_of_sum = sum(nums)
        if num_of_sum % 2 != 0:
            return False
        total = num_of_sum / 2
        print(total)
        dp = [False]*(total+1)
        dp[0] = True
        for num in nums:
            for j in range(total, -1, -1):
                if j>=num:
                    dp[j] = dp[j] or dp[j-num]
        return dp[total]







def main():
    s = Solution()
    # print(s.canPartition([1,2,5]))
    print(s.canPartition([1,5,5,11]))
    print(s.canPartition([1,3,3,3]))
    print(s.canPartition([1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11,1,5,5,11]))
    print(s.canPartition([18,40,62,33,83,64,10,92,67,31,42,51,10,97,41,7,82,71,80,81,41,38,88,25,38,89,24,89,90,12,97,21,22,85,11,59,83,6,51,47,32,82,83,100,29,78,36,32,1,31,36,19,35,3,36,21,24,93,42,33,10,26,2,39,36,62,85,24,41,5,66,53,7,1,59,53,40,59,41,95,7,67,20,29,80,59,49,49,51,90,13,52,6,90,5,6,31,81,95,26]))
    print(s.canPartition([20,68,68,11,48,18,50,5,3,51,52,11,13,11,38,100,30,87,1,56,85,63,14,96,7,17,54,11,32,61,94,13,85,10,78,57,69,92,66,28,70,20,3,29,10,73,89,86,28,48,69,54,87,11,91,32,59,4,88,20,81,100,29,75,79,82,6,74,66,30,9,6,83,54,54,53,80,94,64,77,22,7,22,26,12,31,23,26,65,65,35,36,34,1,12,44,22,73,59,99]))

if __name__ == "__main__":
    main()
