# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxSizeSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def dp(i, j, k, cycle=0):
            if k == 1:
                return max(A[i:j+1])
            if j-i+1 < 2*k-1:
                return -(1<<31)
            return max(dp(i+cycle, j-2, k-1)+A[j], dp(i, j-1, k))
        return dp(0, len(A)-1, len(A)//3, 1)


def main():
    s = Solution()
    print(s.maxSizeSlices([x for x in range(50)]))


if __name__ == "__main__":
    main()
