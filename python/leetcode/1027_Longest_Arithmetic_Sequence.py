# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = [[2]*len(A) for _ in range(len(A))]
        for i in range(len(A)):
            index = {}
            for j in range(i):
                if index.get(2*A[j]-A[i], -1) != -1:
                    dp[j][i] = max(dp[index[2*A[j]-A[i]]][j]+1, dp[j][i])
                index[A[j]] = j
        return max(max(x) for x in dp)


def main():
    s = Solution()
    # print(s.longestArithSeqLength([20,1,15,3,10,5,8]))
    print(s.longestArithSeqLength([24,13,1,100,0,94,3,0,3]))



if __name__ == "__main__":
    main()
