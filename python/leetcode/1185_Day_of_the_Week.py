# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        days = {
            31: {1,3, 5, 7, 8, 10, 12},
            30: {4, 6, 9, 11},
            28: {2}
        }
        duration = 0
        def is_leap_year(year):
            return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

        for i in range(1970, year):
            duration += 366 if is_leap_year(i) else 365

        for i in range(1, month):
            for d, m in days.items():
                if i in m:
                    duration += d
                    break
        duration += 1 if month > 2 and is_leap_year(year) else 0
        duration += day
        names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return names[(duration%7+3)%7]


def main():
    s = Solution()
    print(s.dayOfTheWeek(2,1,1970))
    print(s.dayOfTheWeek(27, 10, 2019))
    print(s.dayOfTheWeek( day = 31, month = 8, year = 2019))


if __name__ == "__main__":
    main()
