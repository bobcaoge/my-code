# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        dp = [0]*(len(A)+1)
        for i in range(1, len(A)+1):
            for j in range(max(0, i-K), i):
                dp[i] = max(dp[i], dp[j] + max(A[j:i])*(i-j))

        return dp[len(A)]


def main():
    s = Solution()
    print(s.maxSumAfterPartitioning([1,15,7,9,2,5,10], K = 3))


if __name__ == "__main__":
    main()
