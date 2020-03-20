# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def judge(self, grid, x, y):
        # if sum(grid[x][y-1:y+2]) + sum(grid[x-1][y-1:y+2]) + sum(grid[x+1][y-1:y+2]) != 45:
        #     return False
        s = set()
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                buffer = grid[i][j]
                if buffer > 9 or buffer < 1:
                    return False
                s.add(grid[i][j])
        if len(s) != 9:
            return False

        if sum(grid[x][y-1:y+2]) == sum(grid[x-1][y-1:y+2]) == sum(grid[x+1][y-1:y+2]) == \
                grid[x-1][y-1]+grid[x][y-1]+grid[x+1][y-1] == \
                grid[x-1][y]+grid[x][y]+grid[x+1][y] == \
                grid[x-1][y+1]+grid[x][y+1]+grid[x+1][y+1] == \
                grid[x-1][y-1]+grid[x][y]+grid[x+1][y+1] == \
                grid[x+1][y-1]+grid[x][y]+grid[x-1][y+1]:
            return True
        return False
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        row = len(grid)
        column = len(grid[0])
        for i in range(1, row-1):
            for j in range(1, column-1):
                ret += self.judge(grid, i, j)
        return ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
