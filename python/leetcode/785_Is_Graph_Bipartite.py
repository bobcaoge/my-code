# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        s = {
                True: set(),
                False: set()
            }
        for k in range(len(graph)):
            cur = set()
            cur.add(k)
            while cur:
                buff = set()
                for i in cur:
                    to_del = []
                    for j in graph[i]:
                        if j in cur:
                            return False
                        buff.add(j)
                        to_del.append([i, j])
                    for x, y in to_del:
                        graph[x].remove(y)
                        graph[y].remove(x)
                cur = buff
        return True





def main():
    s = Solution()
    print(s.isBipartite([[1,3],[0,2],[1,3],[0,2]]))
    print(s.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
    print(s.isBipartite([[4,1],[0,2],[1,3],[2,4],[3,0]]))


if __name__ == "__main__":
    main()
