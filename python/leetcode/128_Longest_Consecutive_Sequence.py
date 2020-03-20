# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums = set(nums)
        self.record = {}
        def dfs(item):
            if item not in nums:
                return 0
            if item not in self.record:
                self.record[item] = 1+dfs(item-1)
            return self.record[item]
        return max([dfs(num) for num in nums])



def main():
    s = Solution()
    print(s.longestConsecutive([4,3,1,2,111,222]))
    print(s.longestConsecutive([100,4,200,5,1,3,2]))
    print(s.longestConsecutive([4,2,1,5,3]))
    print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))


if __name__ == "__main__":
    main()
