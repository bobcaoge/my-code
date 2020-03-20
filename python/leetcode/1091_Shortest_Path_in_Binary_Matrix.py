# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import heapq


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return -1
        N = len(grid)
        heap = [[1, 0, 0]] # step, x, y
        visited = [[False for j in range(N)] for i in range(N)]
        visited[0][0] = True
        while heap:
            step, x, y = heapq.heappop(heap)
            if x == N-1 and y == N-1:
                return step

            for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                if 0<= x+dx < N and 0<= y+dy < N and grid[x+dx][y+dy] == 0 and not visited[x+dx][y+dy]:
                    visited[x+dx][y+dy] = True
                    heapq.heappush(heap, [step+1, x+dx, y+dy])
        return -1


def main():
    s = Solution()
    print(s.shortestPathBinaryMatrix([[0,1],[1,0]]))
    print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))


if __name__ == "__main__":
    main()
