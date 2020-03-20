# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        last = len(graph)-1

        def dfs(path):
            if path[-1] == last:
                ret.append([_ for _ in path])
            for j in graph[path[-1]]:
                path.append(j)
                dfs(path)
                path.pop()
        dfs([0])
        return ret


def main():
    s = Solution()
    print(s.allPathsSourceTarget([[1,2], [3], [3], []] ))


if __name__ == "__main__":
    main()
