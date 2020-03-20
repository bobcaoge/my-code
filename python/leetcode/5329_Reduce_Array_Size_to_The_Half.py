# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        info = sorted([[count, num] for num, count in collections.Counter(arr).items()], reverse=True)
        half = len(arr) - len(arr)//2
        ret = 0
        for count, num in info:
            ret += 1
            half -= count
            if half <= 0:
                return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
