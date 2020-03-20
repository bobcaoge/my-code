# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import heapq
import collections

class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        heap = []
        heapq.heappush(heap, [0, 0])
        visited = [False]*len(arr)
        end= len(arr)-1
        m = collections.defaultdict(list)
        for i, num in enumerate(arr):
            m[num].append(i)
        while True:
            step, pos = heapq.heappop(heap)
            if visited[pos]:
                continue
            if pos == end:
                return step
            visited[pos] = True
            for j in (pos-1, pos+1):
                if 0 <= j < len(arr) and visited[j] is False:
                    heapq.heappush(heap, [step+1, j])
            for j in m[arr[pos]]:
                if visited[j] is False:
                    heapq.heappush(heap, [step+1, j])
            del m[arr[pos]]


def main():
    s = Solution()
    print(s.minJumps([100,-23,-23,404,100,23,23,23,3,404]))
    print(s.minJumps([7]))
    print(s.minJumps([7,6,9,6,9,6,9,7]))
    print(s.minJumps([6,1,9]))
    print(s.minJumps([11,22,7,7,7,7,7,7,7,22,13]))


if __name__ == "__main__":
    main()
