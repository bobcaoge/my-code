# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import heapq

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        cur_nums = 0
        heap = [] # 用以存储车上的人数，以及到的站
        def compare(a, b):
            if a[1] > b[1]:
                return 1
            elif a[1] == b[1]:
                return 0
            return -1
        trips.sort(compare)
        for num, start, end in trips:
            if cur_nums > capacity:
                return False
            while heap and heap[0][0] <= start:
                _, nums = heapq.heappop(heap)
                cur_nums -= nums
            heapq.heappush(heap, [end, num])
            cur_nums += num
        return cur_nums <= capacity


def main():
    s = Solution()
    print(s.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4))
    print(s.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 5))
    print(s.carPooling(trips = [[2,1,5],[3,5,7]], capacity = 3))
    print(s.carPooling( trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11))


if __name__ == "__main__":
    main()
