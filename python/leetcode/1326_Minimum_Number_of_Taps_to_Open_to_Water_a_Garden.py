# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        for i, r in enumerate(ranges):
            l = max(0, i-r)
            ranges[l] = max(ranges(l), i+r)

        res = 0
        lo = 0
        hi = 0
        while hi < n:
            lo, hi = hi, max(ranges[lo:hi+1])
            if lo == hi:
                return -1
            res += 1
        return res



def main():
    s = Solution()


if __name__ == "__main__":
    main()
