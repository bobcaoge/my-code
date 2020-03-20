# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, -1, -1]
        for num in nums:
            shift =  num % 3
            if shift == 0:
                dp[0] += num
                if dp[1] != -1:
                    dp[1] += num
                if dp[2] != -1:
                    dp[2] += num
            elif shift == 1:
                buff = [x for x in dp]
                buff[1] = max(dp[1], dp[0]+num)
                buff[0] = max(dp[0], dp[2]+num if dp[2] != -1 else -1)
                buff[2] = max(dp[2], dp[1]+num if dp[1] != -1 else -1)
                dp = buff
            else:
                buff = [x for x in dp]
                buff[1] = max(dp[1], dp[2]+num if dp[2] != -1 else -1)
                buff[0] = max(dp[0], dp[1]+num if dp[1] != -1 else -1)
                buff[2] = max(dp[2], dp[0]+num if dp[0] != -1 else -1)
                dp = buff
        return dp[0]


def main():
    s = Solution()
    print(s.maxSumDivThree([1,2,3,4,4]))
    print(s.maxSumDivThree([3,6,5,1,8]))
    print(s.maxSumDivThree([4]))


if __name__ == "__main__":
    main()
