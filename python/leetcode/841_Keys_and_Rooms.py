# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [False]*len(rooms)
        def dfs(i):
            if visited[i]:
                return
            visited[i] = True
            for j in rooms[i]:
                dfs(j)
        dfs(0)
        return all(visited)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
