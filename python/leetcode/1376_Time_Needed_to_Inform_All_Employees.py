# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for employee, employer in enumerate(manager):
            if employer != -1:
                graph[employer].append(employee)
        def dfs(i):
            if graph[i] is None:
                return 0
            ret = 0
            for employee in graph[i]:
                ret = max(dfs(employee), ret)
            return ret + informTime[i]
        return dfs(headID)




def main():
    s = Solution()
    print(s.numOfMinutes(n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]))
    print(s.numOfMinutes(n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))


if __name__ == "__main__":
    main()
