# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for pre, n in prerequisites:
            graph[pre].append(n)

        def dfs(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


def main():
    s = Solution()
    print(s.canFinish(2, [[0, 1]]))


if __name__ == "__main__":
    main()
