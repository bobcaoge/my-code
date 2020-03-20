# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        bottom_top = [max([grid[i][j] for i in range(len(grid))]) for j in range(len(grid[0]))]
        left_right = [max(row) for row in grid]
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret += min(left_right[i], bottom_top[j])-grid[i][j]
        return ret



def main():
    s = Solution()
    print(s.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))


if __name__ == "__main__":
    main()
