# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def dfs(x, y):
            if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]):
                return 0
            if grid[x][y] == 0:
                return 0
            ret = 1
            grid[x][y] = 0
            for dx, dy in {(-1, 0), (1, 0),(0, -1),(0, 1),}:
                ret += dfs(x+dx, y+dy)
            return ret
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret = max(ret, dfs(i, j))
        return ret





def main():
    s = Solution()


if __name__ == "__main__":
    main()
