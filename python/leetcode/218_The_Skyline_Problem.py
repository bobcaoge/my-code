# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import bisect


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        buildings.sort()
        intervals = []
        i = 0
        while i < len(buildings):
            interval = buildings.pop(0)
            if not intervals:
                intervals.append(interval)
            else:
                a,b,h1 = interval
                x,y,h2 = intervals[-1]
                if a >= y:
                    intervals.append(interval)
                elif  x <= a<= b<= y and h1 > h2:
                    intervals.pop()
                    intervals.append([x, a, h2])
                    intervals.append(interval)
                    buildings.insert(bisect.bisect(buildings, [b, y, h2]), [b, y, h2])
                elif  x <= a <= y <= b and h1 <= h2:
                    buildings.insert(bisect.bisect(buildings, [y, b, h1]), [y, b, h1])
                elif x <= a<= y<= b and  h1 >= h2:
                    intervals.pop()
                    intervals.append([x, a, h2])
                    intervals.append(interval)
        buff = []
        for interval in intervals:
            if interval[0] == interval[1]:
                continue
            if  buff and interval[0] == buff[-1][1] and buff[-1][2] == interval[2]:
                a, b, h = buff.pop()
                buff.append([a, interval[1], h])
            else:
                buff.append(interval)
        ret = []
        for i, (a, b, h) in enumerate(buff):
            if not ret :
                ret.append([a, h])
            else:
                if ret[-1] == [a, h]:
                    continue
                if buff[i-1][1] < a:
                    ret.append([buff[i-1][1], 0])
                ret.append([a, h])
        ret.append([buff[-1][1], 0])
        return ret









def main():
    s = Solution()
    print(s.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8], [1, 100, 1]]))
    print(s.getSkyline([[1,2,1], [2,3,1]]))
    print(s.getSkyline([[0,2,3],[2,4,3],[4,6,3]]))


if __name__ == "__main__":
    main()
