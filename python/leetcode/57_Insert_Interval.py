# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()
        ret = []
        for interval in intervals:
            if not ret:
                ret.append(interval)
            else:
                if interval[0] <= ret[-1][1]:
                    back = ret.pop()
                    ret.append([back[0], max(interval[1], back[1])])
                else:
                    ret.append(interval)
        return ret


def main():
    s = Solution()
    print(s.insert([[1,3], [6,9]], [2,5]))
    print(s.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,60]))


if __name__ == "__main__":
    main()
