# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        self.row = len(A)
        self.col = len(A[0])

        def dfs(x, y):
            if A[x][y] == 0:
                return
            A[x][y] = 0
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if 0<= x+dx < self.row and 0 <= y+dy < self.col:
                    dfs(x+dx, y+dy)

        for i in range(self.row):
            dfs(i, 0)
            dfs(i, self.col-1)

        for j in range(self.col):
            dfs(0, j)
            dfs(self.row-1, j)

        return sum([sum(x) for x in A])


def main():
    s = Solution()
    print(s.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))


if __name__ == "__main__":
    main()
