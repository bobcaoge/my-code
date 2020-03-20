# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        visited = [False]*len(arr)
        def dfs(i):
            if i < 0 or i >= len(arr) or visited[i]:
                return
            visited[i] = True
            dfs(i-arr[i])
            dfs(i+arr[i])
        dfs(start)
        for i, num in enumerate(arr):
            if num == 0 and visited[i]:
                return True
        return 0 not in arr



def main():
    s = Solution()
    # print(s.canReach([4,2,3,0,3,1,2],5))
    print(s.canReach([0,3,0,6,3,3,4],6))


if __name__ == "__main__":
    main()
