# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        x, y = toBeRemoved
        for interval in intervals:
            left, right = interval
            if interval[1] <= toBeRemoved[0] or interval[0] >=toBeRemoved[1]:
                ret.append(interval)
            if x <= left <= y:
                if right > y:
                    ret.append([y, right])
            if x <= right <= y:
                if left < x:
                    ret.append([left, x])
            if left < x < y < right:
                ret.append([left, x])
                ret.append([y, right])
        return ret


def main():
    s = Solution()
    print(s.removeInterval(intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]))
    print(s.removeInterval(intervals = [[0,5]], toBeRemoved = [2,3]))
    print(s.removeInterval([[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], [-1,4]))


if __name__ == "__main__":
    main()
