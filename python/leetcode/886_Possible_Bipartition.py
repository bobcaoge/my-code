# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(N+1)]
        for x, y in dislikes:
            graph[x].append(y)
            graph[y].append(x)

        def bfs(i):
            a = set()
            a.add(i)
            while a:
                b = set()
                for cur in a:
                    to_remove = []
                    for j in graph[cur]:
                        if j not in a:
                            b.add(j)
                        else:
                            return False
                        to_remove.append(j)
                    for j in to_remove:
                        graph[cur].remove(j)
                        graph[j].remove(cur)
                a = b
            return True
        for i in range(1, N+1):
            if not bfs(i):
                return False
        return True


def main():
    s = Solution()
    print(s.possibleBipartition(N = 4, dislikes = [[1,2],[1,3],[2,4]]))
    print(s.possibleBipartition(N = 3, dislikes = [[1,2],[1,3],[2,3]]))


if __name__ == "__main__":
    main()
