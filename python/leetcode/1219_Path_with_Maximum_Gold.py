# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.row = len(grid)
        self.col = len(grid[0])

        def dfs(i, j):
            if 0 <= i < self.row and 0 <= j < self.col and grid[i][j] > 0:
                cur = grid[i][j]
                grid[i][j] = 0
                res = cur + max(dfs(i, j+1), dfs(i,j-1), dfs(i-1, j), dfs(i+1, j))
                grid[i][j] = cur
                return res
            return 0
        ret = 0
        for i in range(self.row):
            for j in range(self.col):
                ret = max(ret, dfs(i, j))
        return ret



def main():
    s = Solution()
    print(s.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))


if __name__ == "__main__":
    main()
