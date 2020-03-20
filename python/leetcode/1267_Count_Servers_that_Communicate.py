# /usr/bin/python3.6
# -*- coding:utf-8 -*-

class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])

        def dfs(i, j):
            if grid[i][j] == 0:
                return 0
            count = 1
            grid[i][j] = 0
            for x in range(row):
                count += dfs(x, j)
            for y in range(col):
                count += dfs(i, y)
            return count
        ret = 0
        for i in range(row):
            for j in range(col):
                cur = dfs(i, j)
                ret += cur if cur > 1 else 0
        return ret


def main():
    s = Solution()
    print(s.countServers([[1,0], [0,1]]))
    print(s.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))


if __name__ == "__main__":
    main()
