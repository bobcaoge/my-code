# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dp = [[1<<31 for i in range(len(arr)) ] for j in range(len(arr))]
        for j in range(len(arr)):
            dp[j][j] = arr[j]
            for i in range(j-1, -1, -1):
                for k in range(i, j):
                    dp[i][j] = min(max(arr[i:k+1])*max(arr[k+1:j+1])+dp[i][k]+dp[k+1][j], dp[i][j])

        return dp[0][-1] - sum(arr)



def main():
    s = Solution()
    print(s.mctFromLeafValues([6,2,4]))


if __name__ == "__main__":
    main()
