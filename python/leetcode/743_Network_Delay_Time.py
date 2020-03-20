# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import heapq


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = {}
        for start, end, time in times:
            if not graph.get(start, None):
                graph[start] = []
            graph[start].append([end, time])

        record = [1<<30]*(N+1)
        record[0] = 0

        heap = []
        heapq.heappush(heap, [0, K, K])
        visited = [10000]*(N+1)
        visited[0] = 0
        while heap:
            delay, cur, n = heapq.heappop(heap)
            if visited[n] != 10000:
                continue
            visited[n] = delay
            for node, d in graph.get(n, []):
                if visited[node] == 10000:
                    heapq.heappush(heap, [d+delay, n, node])
        return max(visited) if max(visited) < 10000 else -1


def main():
    s = Solution()
    print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1],[4,1,1],[3,2,1]], 4, 2))


if __name__ == "__main__":
    main()
