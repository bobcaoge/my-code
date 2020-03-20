# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        visited = [0]*len(nums)

        def dfs(i):
            if visited[i] == -1:
                return True, 0
            if visited[i] == 1:
                return False, 0
            visited[i] = -1
            flag, ret = dfs(nums[i])
            visited[i] = 1
            if flag:
                return True, ret+1
            return 0
        ret = 0
        for i in range(len(nums)):
            ret = max(ret, dfs(i)[1])
        return ret


def main():
    s = Solution()
    print(s.arrayNesting([5,4,0,3,1,6,2]))


if __name__ == "__main__":
    main()
