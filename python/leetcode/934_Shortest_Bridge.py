# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        islands = set()
        x = 0
        y = 0
        for i in range(len(A)):
            flag = False
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    x, y = i, j
                    flag = True
                    break
            if flag:
                break
        row = len(A)
        col = len(A[0])

        def dfs(i, j):
            if 0 <= i < row and 0 <= j < col:
                if A[i][j] == 1:
                    islands.add((i, j))
                    A[i][j] = 0
                    for di, dj in [(0, 1), (0, -1), (1, 0),(-1, 0)]:
                        dfs(i+di, j+dj)
        dfs(x, y)

        ret = 0
        visited = set(islands)
        while True:
            buff = set()
            for x, y in islands:
                for dx, dy in [(0, 1), (0, -1), (1, 0),(-1, 0)]:
                    if 0 <= x + dx < row and 0 <= y + dy < col and (x+dx, y+dy) not in visited:
                        if A[x+dx][y+dy] == 0:
                            buff.add((x+dx, y+dy))
                            visited.add((x+dx, y+dy))
                        else:
                            return ret
            ret += 1
            islands = buff


def main():
    s = Solution()
    print(s.shortestBridge([[0,1],[1,0]]))
    print(s.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
    print(s.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))


if __name__ == "__main__":
    main()
