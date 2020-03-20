# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections
import heapq


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        s_list = list(s)
        graph = [[] for _ in range(len(s))]

        for x, y in pairs:
            graph[x].append(y)
            graph[y].append(x)
        visited = [False]*len(s_list)
        self.indexes = []
        self.letters = []

        def dfs(i):
            if not visited[i]:
                visited[i] = True
                self.indexes.append(i)
                self.letters.append(s[i])
                for j in graph[i]:
                    dfs(j)

        for i in range(len(s)):
            self.indexes.clear()
            self.letters.clear()
            dfs(i)
            self.indexes.sort()
            self.letters.sort()
            for index, j in enumerate(self.indexes):
                s_list[j] = self.letters[index]
        return "".join(s_list)


def main():
    s = Solution()
    print(s.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2]]))
    print(s.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]]))
    print(s.smallestStringWithSwaps(s = "cba", pairs = [[0,1],[1,2]]))
    print(s.smallestStringWithSwaps(s = "cba", pairs =[]))


if __name__ == "__main__":
    main()
