# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)

        if len(connections) < n-1:
            return -1
        visited = [False]*n

        def dfs(i):
            if visited[i]:
                return 0
            visited[i] = True
            for j in graph[i]:
                dfs(j)
            return 1
        ret = 0
        for i in range(n):
            ret += dfs(i)
        return ret-1



def main():
    s = Solution()


if __name__ == "__main__":
    main()
