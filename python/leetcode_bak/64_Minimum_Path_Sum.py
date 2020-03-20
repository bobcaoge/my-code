# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    row = 0
    column = 0
    grid = None
    min_sum_of_depth = 2 ** 32

    def buffer(self, x, y, sum_of_path):
        if x < self.row and y < self.column:
            sum_of_path += self.grid[x][y]

        if x == self.row-1 and y == self.column-1:
            self.min_sum_of_depth = min(self.min_sum_of_depth, sum_of_path)
        elif x < self.row-1 and y < self.column-1:
            self.buffer(x + 1, y, sum_of_path)
            self.buffer(x, y + 1, sum_of_path)
        elif x < self.row-1:
            for i in range(x + 1, self.row):
                sum_of_path += self.grid[i][y]
            self.min_sum_of_depth = min(self.min_sum_of_depth, sum_of_path)
            # print(sum_of_path)
        elif y < self.column-1:
            sum_of_path += sum(self.grid[x][y + 1:])
            self.min_sum_of_depth = min(self.min_sum_of_depth, sum_of_path)
            # print(sum_of_path)

    def minPathSum1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.row = len(grid)
        self.column = len(grid[0])
        self.min_sum_of_depth = 2 ** 32
        self.buffer(0, 0, 0)
        return self.min_sum_of_depth

    def minPathSum2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        column = len(grid[0])
        ret = []
        for i in range(row):
            ret.append([[] for x in range(column)])
        last = 0
        for i in range(column):
            last += grid[0][i]
            ret[0][i] = [last]
        last = 0
        for j in range(row):
            last += grid[j][0]
            ret[j][0] = [last]
        for i in range(1, row):
            for j in range(1, column):
                up = ret[i-1][j]
                left = ret[i][j-1]
                ret[i][j] += [grid[i][j]+x for x in up]
                ret[i][j] += [grid[i][j]+x for x in left]
                ret[i][j] = [min(ret[i][j])]
        return min(ret[-1][-1])

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        column = len(grid[0])
        last = 0
        for i in range(column):
            last += grid[0][i]
            grid[0][i] = last
        last = 0
        for j in range(row):
            last += grid[j][0]
            grid[j][0] = last

        for i in range(1, row):
            for j in range(1, column):
                up = grid[i-1][j]
                left = grid[i][j-1]
                grid[i][j] += min(up, left)
        return grid[-1][-1]



def main():
    s = Solution()
    print(s.minPathSum([
                          [1,3,1],
                          [1,5,1],
                          [4,2,1]
                        ]))
    print(s.minPathSum([[0]]))
    print(s.minPathSum([[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]))


if __name__ == "__main__":
    main()
