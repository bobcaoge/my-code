# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        dp = [[0 for j in range(len(B))] for i in range(len(A))]
        if A[0] == B[0]:
            dp[0][0] = 1
        for i in range(1, len(A)):
            if A[i] == B[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i-1][0]
        for j in range(1, len(B)):
            if A[0] == B[j]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j-1]

        for i in range(1, len(A)):
            for j in range(1, len(B)):
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        return dp[-1][-1]


def main():
    s = Solution()
    print(s.maxUncrossedLines([1,2,4], [1,4,2]))
    print(s.maxUncrossedLines( A = [2,5,1,2,5], B = [10,5,2,1,5,2]))
    print(s.maxUncrossedLines(A = [1,3,7,1,7,5], B = [1,9,2,5,1]))


if __name__ == "__main__":
    main()
