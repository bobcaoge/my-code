# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def remove_island(self, grid, x, y, row, column):
        grid[x][y] = "0"
        if 0 <= x-1 and grid[x-1][y] == "1":
            self.remove_island(grid, x-1, y, row, column)
        if x+1 < row and grid[x+1][y] == "1":
            self.remove_island(grid, x+1, y, row, column)
        if 0 <= y-1 and grid[x][y-1] == "1":
            self.remove_island(grid, x, y-1, row, column)
        if y+1 < column and grid[x][y+1] == "1":
            self.remove_island(grid, x, y+1, row, column)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        ret = 0
        row = len(grid)
        column = len(grid[0])
        for i in range(row):
            for j in range(column):
                if grid[i][j] == "1":
                    ret += 1
                    self.remove_island(grid, i, j, row, column)
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
