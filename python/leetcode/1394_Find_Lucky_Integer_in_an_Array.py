# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        m = collections.Counter(arr)
        ret = -1
        for num, count in m.items():
            if num == count:
                ret = max(ret, num)
        return ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
