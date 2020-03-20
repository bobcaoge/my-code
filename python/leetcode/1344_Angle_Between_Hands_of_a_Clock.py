# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        ret = abs(6*minutes-minutes/2.0-hour*30)

        return min(ret, 360-ret)


def main():
    s = Solution()
    print(s.angleClock(12, 0))
    print(s.angleClock(4, 50))
    print(s.angleClock(3, 15))
    print(s.angleClock(3, 30))
    print(s.angleClock(12,30))


if __name__ == "__main__":
    main()
