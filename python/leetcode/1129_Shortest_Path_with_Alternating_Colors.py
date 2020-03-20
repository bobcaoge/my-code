# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        visited = [-1]*n
        red = []
        blue = []
        visited[0] = 0
        for i, j in red_edges:
            if i == 0:
                red.append([i, j, 1])
        for i, j in blue_edges:
            if i == 0:
                blue.append([i, j, 1])

        def go(cur, edges):
            blue_buff = []
            for i, j, step in cur:
                b_del = []
                visited[j] = step if visited[j] == -1 else min(visited[j], step)
                for x, y in edges:
                    if x == j:
                        blue_buff.append([x, y, step+1])
                        b_del.append([x, y])
                for item in b_del:
                    edges.remove(item)
            return blue_buff, edges

        while red or blue:
            first = go(red,blue_edges)
            second = go(blue, red_edges)
            blue, blue_edges = first
            red, red_edges = second

        return visited


def main():
    s = Solution()
    print(s.shortestAlternatingPaths(n = 3, red_edges = [[0,1],[1,2]], blue_edges = []))
    print(s.shortestAlternatingPaths(n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]))
    print(s.shortestAlternatingPaths(n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]))
    print(s.shortestAlternatingPaths(n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]))
    print(s.shortestAlternatingPaths(5,[[0,1],[1,2],[2,3],[3,4]],[[1,2],[2,3],[3,1]]))

if __name__ == "__main__":
    main()
