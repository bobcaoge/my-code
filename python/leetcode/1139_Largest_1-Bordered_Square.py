# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        if max([max(x) for x in grid]) == 1:
            ret = 1
        row = len(grid)
        col = len(grid[0])
        dp1 = [[[0, 0] for j in range(col)] for i in range(row)] # left up
        dp1[0][0] = [grid[0][0], grid[0][0]]

        for i in range(1, col):
            dp1[0][i] = [dp1[0][i-1][0] + 1, 1] if grid[0][i] == 1 else [0, 0]
        for i in range(1, row):
            dp1[i][0] = [1, dp1[i-1][0][1]+1] if grid[i][0] == 1 else [0, 0]

        for i in range(1, row):
            for j in range(1, col):
                if grid[i][j] == 1:
                    dp1[i][j][0] = dp1[i][j-1][0] + 1
                    dp1[i][j][1] = dp1[i-1][j][1] + 1

        dp2 = [[[0,0] for j in range(col)] for i in range(row)] # right, down
        dp2[row-1][col-1] = [grid[row-1][col-1], grid[row-1][col-1]]

        for i in range(col-2, -1, -1):
            dp2[row-1][i] = [dp2[row-1][i+1][0] + 1, 1] if grid[row-1][i] == 1 else [0, 0]
        for i in range(row-2, -1, -1):
            dp2[i][col-1] = [1, dp2[i+1][col-1][1] + 1] if grid[i][col-1] == 1 else [0, 0]

        for i in range(row-2, -1, -1):
            for j in range(col-2, -1, -1):
                if grid[i][j] == 1:
                    dp2[i][j][0] = dp2[i][j+1][0] + 1
                    dp2[i][j][1] = dp2[i+1][j][1] + 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] != 1:
                    continue
                length = min(dp2[i][j])
                dx, dy = 1, 1
                while i+dx < row and j+dy < col and dx < length :
                    if dp1[i+dx][j+dy][0] > dx and dp1[i+dx][j+dy][1] > dy:
                        ret = max(ret, dx+1)
                    dx += 1
                    dy += 1
        return ret*ret


def main():
    s = Solution()
    print(s.largest1BorderedSquare([[1,1,1],[1,0,1],[1,1,1]]))
    print(s.largest1BorderedSquare([[1,1,1,1,1,0,0,0,0]]))
    print(s.largest1BorderedSquare([[1,1,0],[1,1,1],[1,1,1],[1,1,1]]))


if __name__ == "__main__":
    main()
