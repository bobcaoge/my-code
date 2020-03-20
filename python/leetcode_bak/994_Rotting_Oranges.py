# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import copy

class Solution(object):
    def is_there_rot_orange(self, grid, x, y, row, column):
        if 0<= x-1 < row and grid[x-1][y] == 2:
            return True
        if 0<= y-1 < column and grid[x][y-1] == 2:
            return True
        if 0<= y+1 < column and grid[x][y+1] == 2:
            return True
        if 0<= x+1 < row and grid[x+1][y] == 2:
            return True
        return False

    def step(self, grid):
        ret = copy.deepcopy(grid)
        row = len(grid)
        column = len(grid[0])
        plus = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1 and self.is_there_rot_orange(grid, i, j, row, column):
                    ret[i][j] = 2
                    plus += 1
        return ret, plus

    def scan_cell(self, grid):
        row = len(grid)
        column = len(grid[0])
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    return False
        return True

    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        minutes = 0
        if self.scan_cell(grid):
            return 0
        new_plus = 1
        while new_plus != 0:
            grid, new_plus = self.step(grid)
            # print(grid)
            minutes += 1
        if self.scan_cell(grid):
            return minutes-1
        return -1




def main():
    s = Solution()
    print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))


if __name__ == "__main__":
    main()
