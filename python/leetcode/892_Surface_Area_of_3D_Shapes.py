# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def surfaceArea(self, grid):
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
            yz += sum([abs(cubes[i]-cubes[i-1]) for i in range(1, len(cubes))]) + cubes[0] + cubes[-1]
            length = max(length, length_of_cubes)
        xz = 0
        for column in range(length):
            old = 0
            for row in range(len(grid)):
                xz += abs(grid[row][column]-old)
                old = grid[row][column]
            xz += grid[len(grid)-1][column]
        return 2*xy + xz + yz

    def surfaceArea1(self, grid):
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
            buffer = [0]+cubes+[0]
            yz += sum([abs(buffer[i]-buffer[i-1]) for i in range(1, len(buffer))])
            length = max(length, length_of_cubes)
        xz = 0
        for column in range(length):
            old = 0
            for row in range(len(grid)):
                xz += abs(grid[row][column]-old)
                old = grid[row][column]
            xz += grid[len(grid)-1][column]
        return 2*xy + xz + yz
def main():
    s = Solution()
    print(s.surfaceArea([[2]]))
    print(s.surfaceArea([[1,2],[3,4]]))
    print(s.surfaceArea([[1,0],[0,2]]))
    print(s.surfaceArea([[1,1,1],[1,0,1],[1,1,1]]))
    print(s.surfaceArea([[2,2,2],[2,1,2],[2,2,2]]))

if __name__ == "__main__":
    main()
