# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp1 = [1]*len(nums)
        dp2 = [[0]*len(nums) for _ in range(len(nums)+1)]
        longest_length = 1
        for i in range(len(nums)):
            dp2[i][1] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    dp2[i][dp1[j]+1] += dp2[j][dp1[j]]
                    dp1[i] = max(dp1[i], dp1[j]+1)
                    longest_length = max(longest_length, dp1[i])
        return sum([x[longest_length] for x in dp2])


def main():
    s = Solution()
    print(s.findNumberOfLIS([1,3,5,4,7]))
    print(s.findNumberOfLIS([1,3,5,4,7,3,4,5,4,7,3,5,9,1,4,2,9,5]))
    print(s.findNumberOfLIS([1,2,1,2,1,2]))


if __name__ == "__main__":
    main()
