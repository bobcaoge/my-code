# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        rows = {}
        cols = {}
        for x, y in stones:
            if not rows.get(x, None):
                rows[x] = []
            if not cols.get(y, None):
                cols[y] = []
            rows[x].append((x, y))
            cols[y].append((x, y))
        ret = 0
        visited = set()

        def dfs(x, y):
            cur = 0
            if (x, y) not in visited:
                visited.add((x, y))
                cur = 1
                for i, j in rows[x]:
                    cur += dfs(i, j)
                for i, j in cols[y]:
                    cur += dfs(i, j)
            return cur

        for x, y in stones:
            ret += max(dfs(x, y) -1, 0)
            # print(ret)

        return ret


def main():
    s = Solution()
    print(s.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
    print(s.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
    print(s.removeStones([[0,0],[0,1],[1,0],[1,1],[2,1],[2,2],[3,2],[3,3],[3,4],[4,3],[4,4]]))


if __name__ == "__main__":
    main()
