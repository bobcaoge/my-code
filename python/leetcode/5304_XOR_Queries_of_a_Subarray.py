# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        dp = [0]
        for num in arr:
            dp.append(dp[-1] ^ num)
        ret = []
        for L, R in queries:
            ret.append(dp[R+1]^dp[L])
        return ret


def main():
    s = Solution()
    print(s.xorQueries(arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]))
    print(s.xorQueries(arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]))


if __name__ == "__main__":
    main()
