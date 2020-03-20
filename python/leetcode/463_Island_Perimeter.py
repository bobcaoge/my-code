# /usr/bin/python3.6
# -*- coding:utf-8 -*-

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        width = len(grid)
        column = len(grid[0])
        for row in grid:
            for block in row:
                if block == 1:
                    ret += 4
            # 检查行相邻
            for index in range(1, column):
                if row[index] == row[index-1] == 1:
                    ret -= 2
        # 检查列相邻
        for i in range(column):
            for j in range(width-1):
                if grid[j][i] == grid[j+1][i] == 1:
                    ret -= 2
        return ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
