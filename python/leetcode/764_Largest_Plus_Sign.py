# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        grid = [[[1,1,1,1] for i in range(N)] for j in range(N)]
        s = set([(x, y) for x, y in mines])
        for mine in mines:
            grid[mine[0]][mine[1]] = [0,0,0,0]
        # up left down right
        for i in range(1, N):
            # up
            if (i, 0) not in s:
                grid[i][0][0] += grid[i-1][0][0]
            # left
            if (0, i) not in s:
                grid[0][i][1] += grid[0][i-1][1]
            # down
            if (N-1-i, N-1) not in s:
                grid[N-1-i][N-1][2] += grid[N-i][N-1][2]
            # right
            if (N-1, N-1-i) not in s:
                grid[N-1][N-1-i][3] += grid[N-1][N-i][3]
        for i in range(1, N):
            for j in range(1, N):
                if (i, j) not in s:
                    grid[i][j][0] += grid[i-1][j][0]
                    grid[i][j][1] += grid[i][j-1][1]
                if (N-1-i, N-1-j) not in s:
                    grid[N-1-i][N-1-j][2] += grid[N-i][N-j-1][2]
                    grid[N-1-i][N-1-j][3] += grid[N-i-1][N-j][3]
        ret = 0
        for i in range(N):
            for j in range(N):
                ret = max(ret, min(grid[i][j]))
        return ret


def main():
    s = Solution()
    print(s.orderOfLargestPlusSign(N = 5, mines = [[4, 2]]))


if __name__ == "__main__":
    main()
