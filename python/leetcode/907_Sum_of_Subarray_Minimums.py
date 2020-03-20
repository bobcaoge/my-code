# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import bisect


class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        temp = 1000000007
        info = sorted([[num, i] for i, num in enumerate(A)])
        managed = [-1, len(A)]
        ret = 0
        for num, i in info:
            index = bisect.bisect(managed, i)
            ret = (ret + num*(i - managed[index-1])*(managed[index]-i) % temp)%temp
            managed.insert(index, i)
        return ret % temp







def main():
    s = Solution()
    print(s.sumSubarrayMins([3,1,2,4]))
    print(s.sumSubarrayMins([3,1,2,4,3,4,5,7,45,3,3,5,76,5,3,34,5,67,8,65,4,3,2,3,4,5,7,8,9,7,6,5,4,4]))


if __name__ == "__main__":
    main()
