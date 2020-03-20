# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class MyCalendarTwo(object):

    def __init__(self):
        self.intervals = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        commons = []
        for s, e in self.intervals:
            if start <= s:
                if s < end < e:
                    commons.append([s, end])
                elif end >= e:
                    commons.append([s, e])
            elif s < start:
                if end < e:
                    commons.append([start, end])
                elif end >= e:
                    commons.append([start, e])
        commons.sort()
        for i in range(1, len(commons)):
            if commons[i][0] < commons[i-1][1]:
                return False
        self.intervals.append([start, end])
        return True


def main():
    s = Solution()


if __name__ == "__main__":
    main()
