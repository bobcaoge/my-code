# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda Interval: Interval.start)
        ret = []
        for interval in intervals:
            if not ret or interval.start > ret[-1].end:
                ret.append(interval)
            elif interval.start <= ret[-1].end < interval.end:
                ret[-1].end = interval.end
        return ret

    def merge1(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda Interval: Interval.start)
        # for i in intervals:
        #     print(i.start, i.end)
        ret = []
        for interval in intervals:
            if not ret:
                ret.append(interval)
            else:
                if interval.start > ret[-1].end:
                    ret.append(interval)
                elif interval.start <= ret[-1].end:
                    if interval.end > ret[-1].end:
                        ret[-1].end = interval.end
        return ret



def main():
    s = Solution()
    s.merge([Interval(1,2),Interval()])


if __name__ == "__main__":
    main()
