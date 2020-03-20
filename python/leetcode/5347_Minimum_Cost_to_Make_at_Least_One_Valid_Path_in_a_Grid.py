# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import heapq

class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        heap = [[0,[0, 0]]]
        row = len(grid)
        col = len(grid[0])
        m = {1 : [0, 1],
             2: [0, -1],
             3: [1, 0],
             4: [-1, 0]}
        visited = [[10000 for i in range(col)] for j in range(row)]
        while heap:
            cost, [x, y] = heapq.heappop(heap)
            if 0 <= x < row and 0 <= y < col:
                if visited[x][y] <= cost:
                    continue
                visited[x][y] = cost
                if [x, y] == [row-1, col-1]:
                    return cost
                ddx, ddy = m[grid[x][y]]
                heapq.heappush(heap, [cost, [x+ddx, y+ddy]])
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    if [dx, dy] != [ddx, ddy]:
                        heapq.heappush(heap, [cost+1, [x+dx, y+dy]])






def main():
    s = Solution()
    print(s.minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))


if __name__ == "__main__":
    main()
