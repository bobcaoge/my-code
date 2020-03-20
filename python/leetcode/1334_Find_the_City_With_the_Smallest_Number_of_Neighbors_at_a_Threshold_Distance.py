# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for fro, to, weight in edges:
            graph[fro].append([to, weight])
            graph[to].append([fro, weight])

        def bfs(city):
            visited = [1<<31 for _ in range(n)]
            visited[city] = True
            cur = [[city, 0]]
            while cur:
                buff = []
                for i, w in cur:
                    for j, dw in graph[i]:
                        if w + dw <= distanceThreshold and w+dw < visited[j]:
                            visited[j] = dw + w
                            buff.append([j, w+dw])
                cur = buff
            return sum([d <= distanceThreshold for d in visited])
        ret = []
        for city in range(n):
            ret.append([bfs(city), city])
        print(ret)
        city, neighbor = -1, n+1
        for cur_neighbor, cur_city in ret:
            if cur_neighbor < neighbor:
                neighbor = cur_neighbor
                city = cur_city
            elif cur_neighbor == neighbor:
                if city < cur_city:
                    city = cur_city
        return city


def main():
    s = Solution()
    print(s.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))
    print(s.findTheCity(8,
                        [[3,5,9558],[1,2,1079],[1,3,8040],[0,1,9258],[4,7,7558],[5,6,8196],[3,4,7284],[1,5,6327],[0,4,5966],[3,6,8575],[2,5,8604],[1,7,7782],[4,6,2857],[3,7,2336],[0,6,6],[5,7,2870],[4,5,5055],[0,7,2904],[1,6,2458],[0,5,3399],[6,7,2202],[0,2,3996],[0,3,7495],[1,4,2262],[2,6,1390]]
    ,7937))


if __name__ == "__main__":
    main()
