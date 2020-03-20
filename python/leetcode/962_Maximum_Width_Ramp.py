# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import heapq


class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        buff = sorted([[x, i] for i, x in enumerate(A)], reverse=True)
        ret = 0
        right = -1
        for num, i in buff:
            ret = max(right-i, ret)
            right = max(right, i)
        return ret



def main():
    s = Solution()
    print(s.maxWidthRamp([6,0,8,2,1,5]))


if __name__ == "__main__":
    main()
