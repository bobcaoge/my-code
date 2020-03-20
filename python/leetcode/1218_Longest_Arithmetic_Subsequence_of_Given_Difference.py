# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections
import bisect


class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        m = collections.defaultdict(list)
        for i, num in enumerate(arr):
            m[num].append(i)
        visited = [-1]*len(arr)

        def dfs(i):
            if visited[i] == -1:
                j = bisect.bisect(m[arr[i] + difference], i)
                cur = 1
                if j < len(m[arr[i]+difference]):
                    cur = 1 + dfs(m[arr[i]+difference][j])
                visited[i] = cur
            return visited[i]
        ret = 0
        for i in range(len(arr)):
            ret = max(ret, dfs(i))
        return ret


def main():
    s = Solution()
    print(s.longestSubsequence([1,2,3,4], 1))
    print(s.longestSubsequence(arr = [1,3,5,7], difference = 1))
    print(s.longestSubsequence(arr = [1,5,7,8,5,3,4,2,1], difference = -2))


if __name__ == "__main__":
    main()
