# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        old = [-1<<31, -1<<31]
        ret = 0
        for x, y in intervals:
            if x>= old[1]:
                old = x, y
                ret += 1
            else:
                if y < old[1]:
                    old = x, y
        return len(intervals) - ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
