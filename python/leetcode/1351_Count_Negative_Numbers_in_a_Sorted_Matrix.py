# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        ret = row * col
        for i in range(row):
            for j in range(col):
                if grid[i][j] <0:
                    break
                ret -= 1
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
