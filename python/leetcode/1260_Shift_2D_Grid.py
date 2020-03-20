# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        row = len(grid)
        col = len(grid[0])
        ret = [[0 for j in range(col)] for i in range(row)]
        length = row*col
        for i in range(row):
            for j in range(col):
                pos = (i*col+j+k) % length
                x, y = divmod(pos, col)
                ret[x][y] = grid[i][j]
        return ret



def main():
    s = Solution()
    print(s.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], k = 9))


if __name__ == "__main__":
    main()
