# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import datetime


class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        year, month, day = [int(x) for x in date1.split('-')]
        a = datetime.date(year, month, day)
        year, month, day = [int(x) for x in date2.split('-')]
        b = datetime.date(year, month, day)
        return abs(a.toordinal()-b.toordinal())



def main():
    s = Solution()
    print(s.daysBetweenDates( date1 = "2019-06-29", date2 = "2019-06-30"))


if __name__ == "__main__":
    main()
