# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def recursion(self, vertexes):
        if len(vertexes) < 3:
            return 0
        ret = 2000000
        if len(vertexes) == 3:
            ret = 1
            for v in vertexes:
                ret *= v
        else:
            for i in range(1, len(vertexes)-1):
                ret = min(ret, vertexes[0]*vertexes[-1]*vertexes[i]+self.recursion(vertexes[0:i+1])+self.recursion(vertexes[i:]))
            # print(vertexes, ret)
        return ret
    def minScoreTriangulation1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return self.recursion(A)
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = [[2000000]*len(A) for _ in range(len(A))]
        for i in range(len(A)-1, -1, -1):
            for j in range(i, len(A)):
                if j - i < 2:
                    dp[i][j] = 0
                if j-i == 2:
                    dp[i][j] = A[i]*A[j]*A[i+1]
                else:
                    for k in range(i+1, j):
                        dp[i][j] = min(dp[i][j], A[i]*A[j]*A[k]+dp[i][k]+dp[k][j])
        return dp[0][-1]


def main():
    s = Solution()
    print(s.minScoreTriangulation([1,3,1,4,1,5]))
    print(s.minScoreTriangulation([1,3,4,3,3]))


if __name__ == "__main__":
    main()
