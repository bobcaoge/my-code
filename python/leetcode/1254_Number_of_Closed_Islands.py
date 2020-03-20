# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.row = len(grid)
        self.col = len(grid[0])

        def dfs(x, y):
            if 0 <= x < self.row and 0 <= y < self.col and grid[x][y] == 0:
                grid[x][y] = 1
                for dx, dy in ((-1, 0), (1, 0),(0, -1),(0, 1)):
                    dfs(x+dx, y+dy)
                return 1
            return 0
        for i in range(self.row):
            dfs(i, 0)
            dfs(i, self.col-1)
        for j in range(self.col):
            dfs(0, j)
            dfs(self.row-1, j)
        ret = 0
        for i in range(self.row):
            for j in range(self.col):
                ret += dfs(i, j)
        return ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
