# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        ret = len(intervals)
        last_interval = [-1, -1]
        intervals.sort()
        for interval in intervals:
            if interval[1] <= last_interval[1]:
                ret -= 1
            else:
                last_interval = interval
        return ret


def main():
    s = Solution()
    print(s.removeCoveredIntervals(intervals = [[1,4],[3,6],[2,8]]))


if __name__ == "__main__":
    main()
