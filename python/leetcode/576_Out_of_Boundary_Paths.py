# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    count = 0
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        # memo = {}
        # return self.recursion(m,n,N,i,j,memo) % (10**9+7)
        grid = [[0]*n for _ in range(m)]
        grid[i][j] = 1
        ret = 0
        for i in range(N):
            buff = [[0]*n for _ in range(m)]
            for row in range(m):
                for col in range(n):
                    grid[row][col] %= 10**9+7
                    ret += self.move(m, n, row, col, grid, buff)
            grid = buff
            # print(grid)
        return ret % (10**9+7)

    def move1(self, m, n, i, j, grid, buff):
        # move to left
        ret = 0
        if i == 0:
            ret += grid[i][j]
        else:
            buff[i-1][j] += grid[i][j]
        # move to right
        if i == m-1:
            ret += grid[i][j]
        else:
            buff[i+1][j] += grid[i][j]
        # move to down
        if j == n-1:
            ret += grid[i][j]
        else:
            buff[i][j+1] += grid[i][j]
        if j == 0:
            ret += grid[i][j]
        else:
            buff[i][j-1] += grid[i][j]
        return ret

    def move(self, m, n, i, j, grid, buff):
        ret = 0
        if i == 0:
            ret += grid[i][j]
        if i == m-1:
            ret += grid[i][j]
        if j == n-1:
            ret += grid[i][j]
        if j == 0:
            ret += grid[i][j]
        buff[i][j] = (grid[i-1][j] if i > 0 else 0) + \
                     (grid[i+1][j] if i < m-1 else 0) + \
                     (grid[i][j-1] if j > 0 else 0) + \
                     (grid[i][j+1] if j < n-1 else 0)
        return ret

def main():
    s = Solution()
    print(s.findPaths(2,2,2,0,0))
    print(s.findPaths(1,3,3,0,1))
    print(s.findPaths(2,2,6,0,0))
    print(s.findPaths(2,2,10,0,0))
    print(s.findPaths(2,2,50,0,0))


if __name__ == "__main__":
    main()
