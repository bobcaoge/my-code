# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        visited = [0]*len(graph)
        nodes = [False]*len(graph)

        def dfs(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return nodes[i]
            visited[i] = -1
            flag = True
            for j in graph[i]:
                if not dfs(j):
                    flag = False
            nodes[i] = flag
            visited[i] = 1
            return flag
        for i in range(len(graph)):
            dfs(i)
        return [index for index, x in enumerate(nodes) if x]


def main():
    s = Solution()
    print(s.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))


if __name__ == "__main__":
    main()
