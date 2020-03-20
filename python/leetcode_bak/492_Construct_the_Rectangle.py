# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import math


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        for i in range(int(math.sqrt(area)), 0, -1):
            if area % i == 0:
                return [int(area/i), i]


def main():
    s = Solution()


if __name__ == "__main__":
    main()
