# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        s = 0
        ret = 0
        m = {}
        for i, num in enumerate(hours):
            s += (1 if num > 8 else -1)
            if s > 0:
                ret = i+1
            else:
                ret = max(ret, i-m.get(s-1, i))
            if m.get(s, -2) == -2:
                m[s] = i
        return ret


def main():
    s = Solution()
    print(s.longestWPI([1,1,1,9,9]))
    print(s.longestWPI([1,9,9,9,1]))
    print(s.longestWPI([9,9,1,1,1,1,9]))
    print(s.longestWPI([1,1,9]))
    print(s.longestWPI([1,1,8]))
    print(s.longestWPI([2,9,9]))
    print(s.longestWPI([9, 6, 9]))
    print(s.longestWPI([10,5,9,7,9,9,5,5,7,10]))
    print(s.longestWPI([10,5,9,7,9,9,5,5,7,10, 10]))
    print(s.longestWPI([12,8,7,7,9,10,8,7,9,7,8,11]))


if __name__ == "__main__":
    main()
