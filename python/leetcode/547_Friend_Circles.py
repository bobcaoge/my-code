# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        n = len(M)
        visited = [False]*n

        def dfs(i):
            if visited[i]:
                return 0
            visited[i] = True
            for j in range(n):
                if M[i][j] == 1:
                    dfs(j)
            return 1
        ret = 0
        for i in range(n):
            ret += dfs(i)
        return ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
