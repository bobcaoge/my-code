# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import bisect
import heapq


class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        engineers = sorted([[efficiency[i],speed[i]] for i in range(n)], reverse=True)
        speeds = []
        cur_sum_of_speed = 0
        ret = 0
        for i in range(n):
            e,s = engineers[i]
            if len(speeds) < k:
                heapq.heappush(speeds, s)
                cur_sum_of_speed += s
            else:
                if s > speeds[0]:
                    cur_sum_of_speed += s-speeds[0]
                    heapq.heappop(speeds)
                    heapq.heappush(speeds, s)
            ret = max(ret, cur_sum_of_speed*e)
        return ret %(10**9+7)





def main():
    s = Solution()
    print(s.maxPerformance( n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3))
    print(s.maxPerformance(3,
                           [2,8,2],
                           [2,7,1],
    2))


if __name__ == "__main__":
    main()
