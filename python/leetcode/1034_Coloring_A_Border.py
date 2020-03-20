# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        self.row = len(grid)
        self.col = len(grid[0])
        origen = grid[r0][c0]
        def dfs(x, y, target):
            if 0<= x < self.row and 0 <= y < self.col and grid[x][y] == target:
                grid[x][y] = -1
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    dfs(x+dx, y+dy, target)

        dfs(r0, c0, grid[r0][c0])

        def count(x, y):
            ret = 0
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0<= x+dx < self.row and 0<= y+dy < self.col and grid[x+dx][y+dy] == -1:
                    ret += 1
            return ret
        keep = []
        rev = []
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j] == -1:
                    if count(i, j) < 4:
                        keep.append([i, j])
                    else:
                        rev.append([i, j])

        for i, j in keep:
            grid[i][j] = color
        for i, j in rev:
            grid[i][j] = origen
        return grid



def main():
    s = Solution()


if __name__ == "__main__":
    main()
