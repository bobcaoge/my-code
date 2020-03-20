# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        visited = [0]*(len(edges)+1)
        circle_vertex = set()
        graph = {}
        for start, end in edges:
            if not graph.get(start, None):
                graph[start] = []
            graph[start].append(end)
            if not graph.get(end, None):
                graph[end] = []
            graph[end].append(start)

        def dfs(v, old):
            if visited[v] == -1:
                circle_vertex.add(v)
                visited[v] = 0
                return True
            if visited[v] == 1:
                return False
            visited[v] = -1
            for node in graph.get(v, []):
                if node != old:
                    if dfs(node, v):
                        if visited[v] == 0:
                            visited[v] = 1
                            return False
                        circle_vertex.add(v)
                        visited[v] = 1
                        return True
            visited[v] = 1
            return False
        for i in range(1, len(edges)+1):
            dfs(i, -1)
        ret = []
        for x, y in edges:
            if x in circle_vertex and y in circle_vertex:
                ret = [x, y]
        return ret


def main():
    s = Solution()
    # print(s.findRedundantConnection([[1,2],[1,3],[2,3]]))
    # print(s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
    print(s.findRedundantConnection([[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]))


if __name__ == "__main__":
    main()
