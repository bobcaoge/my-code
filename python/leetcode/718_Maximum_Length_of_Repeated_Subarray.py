# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]
        ret = 0
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
                    ret = max(ret, dp[i][j])
        return ret


def main():
    s = Solution()
    print(s.findLength([5,6,3,2,1],[3,2,1,3,3]))


if __name__ == "__main__":
    main()
