# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ret = 0
        for i in range(1, len(points)):
            ret += max(abs(points[i][0]-points[i-1][0]), abs(points[i][1]-points[i-1][1]))
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
