# /usr/bin/python3.6
# -*- coding:utf-8 -*-

class MyCalendar(object):

    def __init__(self):
        self.intervals = []


    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for s, e in self.intervals:
            if s<= start < e or s < end < e or start <= s < end or start < e < end:
                return False
        self.intervals.append([start, end])
        return True




def main():
    s = Solution()


if __name__ == "__main__":
    main()
