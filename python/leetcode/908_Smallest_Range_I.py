# /usr/bin/python2.7
# -*- coding:utf-8 -*-


class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        min_num = min(A)
        max_num = max(A)
        if max_num - K <= min_num + K:
            return 0
        return max_num-K - min_num - K




def main():
    s = Solution()


if __name__ == "__main__":
    main()
