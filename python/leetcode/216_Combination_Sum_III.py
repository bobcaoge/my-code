# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    ret = []
    def dfs(self, k, nums, target, sum_of_before, depth):
        if k == 0:
            if sum_of_before == target:
                self.ret.append(depth)
            return
        for index, num in enumerate(nums):
            if num + sum_of_before <= target:
                self.dfs(k-1, nums[index+1:], target, sum_of_before+num, depth+[num])

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.ret = []
        nums = [x+1 for x in range(9)]
        self.dfs(k, nums, n, 0, [])
        return self.ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
