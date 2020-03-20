# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        visited = [[False for j in range(col)] for i in range(row)]
        nodes = []

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    nodes.append([i, j])
                    visited[i][j] = True
        if not nodes:
            return -1
        i = -1
        while nodes:
            buff = []
            for x, y in nodes:
                for dx, dy in [[-1, 0],[1, 0],[0, -1],[0, 1]]:
                    if 0<= dx+x < row and 0<= dy+y < col and (not visited[dx+x][dy+y]):
                        buff.append([dx+x, dy+y])
                        visited[x+dx][y+dy] = True
            nodes = buff
            i += 1

        return -1 if i == 0 else i





def main():
    s = Solution()
    print(s.maxDistance([[1,0,1],[0,0,0],[1,0,1]]))
    print(s.maxDistance([[1,0,0],[0,0,0],[0,0,0]]))
    print(s.maxDistance([[1,1,1],[1,1,1],[1,1,1]]))


if __name__ == "__main__":
    main()
