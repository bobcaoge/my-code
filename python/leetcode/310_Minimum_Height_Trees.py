# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[set[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        graph = [set() for _ in range(n)]
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        while True:
            next_leaves = []
            for node in leaves:
                for neighbor in graph[node]:
                    graph[neighbor].remove(node)
                    if len(graph[neighbor]) == 1:
                        next_leaves.append(neighbor)
            if len(next_leaves) == 0:
                return leaves
            leaves = next_leaves

def main():
    s = Solution()
    print(s.findMinHeightTrees(n = 2, edges=[[1, 0]]))
    print(s.findMinHeightTrees(n = 4, edges = [[1, 0], [1, 2], [1, 3]]))
    print(s.findMinHeightTrees(n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))


if __name__ == "__main__":
    main()
