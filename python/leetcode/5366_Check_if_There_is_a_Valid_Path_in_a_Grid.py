# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        move = {1:[(0,-1), (0, 1)],
                2:[(1, 0), (-1, 0)],
                3:[(0, -1),(1, 0)],
                4:[(1, 0), (0, 1)],
                5:[(0, -1), (-1, 0)],
                6:[(-1, 0), (0, 1)]}
        visited = set()
        def valid(x, y, a, b):
            if 0 <= x < len(grid) and 0 <= a < len(grid) and 0 <= y < len(grid[0]) and 0 <= b < len(grid[0]):
                flag1 = False
                for dx, dy in move[grid[x][y]]:
                    if (x+dx, y+dy) == (a, b):
                        flag1 = True
                        break
                flag2 = False
                for da, db in move[grid[a][b]]:
                    if (a+da, b+db) == (x, y):
                        flag2 = True
                        break
                return flag1 and flag2
            return False

        def dfs(x, y):
            if (x, y) == (len(grid)-1, len(grid[0])-1):
                return True
            if (x, y) in visited:
                return False
            visited.add((x, y))
            ret = False
            for dx, dy in move[grid[x][y]]:
                if valid(x, y, x+dx, y+dy):
                    ret = ret or dfs(x+dx, y+dy)
            return ret
        return dfs(0, 0)






def main():
    s = Solution()


if __name__ == "__main__":
    main()
