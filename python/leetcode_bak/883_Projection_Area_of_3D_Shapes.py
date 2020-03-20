# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        xy = 0
        yz = 0
        length = 0
        for cubes in grid:
            length_of_cubes = len(cubes)
            xy += sum([1 for x in cubes if x != 0])
            yz += max(cubes)
            length = max(length, length_of_cubes)
        xz = 0
        for column in range(length):
            max_ = 0
            for row in range(len(grid)):
                max_ = max(max_, grid[row][column])
            xz += max_
        return xy + xz + yz





def main():
    s = Solution()


if __name__ == "__main__":
    main()
