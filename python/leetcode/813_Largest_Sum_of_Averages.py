# /usr/bin/python3.6
# -*- coding:utf-8 -*-

class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        dp = [[0.0]*(K) for _ in range(len(A))]

        sums = [0]*len(A)
        old = 0
        for i, num in enumerate(A):
            old += num
            sums[i] = old
        for i in range(len(A)):
            dp[i][0] = sums[i]/(i+1)
            for j in range(K):
                if i+1 < j:
                    continue
                for k in range(i):
                    if dp[k][j-1] > 0:
                        dp[i][j] = max(dp[i][j], dp[k][j-1]+(sums[i]-sums[k])/(i-k))

        return dp[len(A)-1][K-1]


def main():
    s = Solution()
    print(s.largestSumOfAverages([1,2,3,4,5,6,7], 4))
    print(s.largestSumOfAverages([9,1,2,3,9], 3))
    print(s.largestSumOfAverages([9,1,2,3,9,3,4,2,7,5,9,3,3], 5))
    print(s.largestSumOfAverages([9,1,2,3,9, 3,4,2,7,5,9,3,3,3,4,6,7,8,3,3,2,4,6,7,5,6,5,4,4,6], 5))


if __name__ == "__main__":
    main()
