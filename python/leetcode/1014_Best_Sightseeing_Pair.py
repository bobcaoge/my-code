# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        keep = A[-1]+len(A)-1
        ret = 0
        for i in range(len(A)-2, -1, -1):
            ret = max(ret, keep-i+A[i])
            keep = max(keep, A[i]+i)
        return ret





def main():
    s = Solution()


if __name__ == "__main__":
    main()
