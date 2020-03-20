# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import math


class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        s = {(x, y) for x, y in points}

        def get(p1, p2, p3):
            d12 = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
            d13 = (p1[0]-p3[0])**2 + (p1[1]-p3[1])**2
            d23 = (p3[0]-p2[0])**2 + (p3[1]-p2[1])**2

            if d12 + d23 == d13:
                x, y = p1[0]+p3[0] - p2[0], p1[1]+p3[1] - p2[1],
                if (x, y) in s:
                    return math.sqrt(d12*d23)
            if d12 + d13 == d23:
                x, y = p2[0]+p3[0] - p1[0], p2[1]+p3[1] - p1[1],
                if (x, y) in s:
                    return math.sqrt(d12*d13)

            return 1<<31

        points.sort()
        ret = 1<<31
        for i, p1 in enumerate(points):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    ret = min(get(p1, points[j], points[k]), ret)
        return ret if ret < 1<<31 else 0


def main():
    s = Solution()
    print(s.minAreaFreeRect([[1,2],[2,1],[1,0],[0,1]]))


if __name__ == "__main__":
    main()
