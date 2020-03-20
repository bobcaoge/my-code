# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import heapq


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        intervals = [[intervals[i][0], intervals[i][1], i] for i in range(len(intervals))]
        intervals.sort()
        ret = [-1]*len(intervals)
        heap = []
        for msg in intervals:
            while heap and heap[0][0] <= msg[0]:
                ret[heap[0][-1]] = msg[-1]
                heapq.heappop(heap)
            heapq.heappush(heap, [msg[1], msg[0], msg[-1]])

        return ret




def main():
    s = Solution()
    print(s.findRightInterval([ [3,4], [2,3], [1,2] ]))


if __name__ == "__main__":
    main()
